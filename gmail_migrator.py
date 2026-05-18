import imaplib
import email
import email.utils
import re
import sys
import os
from dotenv import load_dotenv

load_dotenv()

# ==========================================
# CONFIGURATION
# ==========================================
# Source Account (Your Personal Gmail)
SOURCE_EMAIL = os.getenv("SOURCE_EMAIL", "your.personal.email@gmail.com")
SOURCE_APP_PASSWORD = os.getenv("SOURCE_APP_PASSWORD", "") # See instructions on how to get an App Password

# Destination Account (Your Workspace/Business Email)
DEST_EMAIL = os.getenv("DEST_EMAIL", "you@yourbusiness.com")
DEST_APP_PASSWORD = os.getenv("DEST_APP_PASSWORD", "")

# The top-level label you want to migrate.
# It will catch this label and ALL nested sub-labels.
LABEL_PREFIX_TO_MIGRATE = "keplar-flow-limited"
# ==========================================


def connect_to_imap(email_address, app_password):
    print(f"Connecting to {email_address}...")
    try:
        mail = imaplib.IMAP4_SSL('imap.gmail.com')
        mail.login(email_address, app_password)
        print(f"Successfully connected to {email_address}")
        return mail
    except imaplib.IMAP4.error as e:
        print(f"Failed to connect to {email_address}. Please check your App Password.")
        print(f"Error details: {e}")
        sys.exit(1)

def parse_folder_name(folder_string):
    """
    Parses the raw IMAP folder string to extract the actual folder name.
    Example input: b'(\\HasNoChildren) "/" "keplar-flow-limited/Mental Corner"'
    """
    folder_str = folder_string.decode('utf-8')
    # Regex to extract the name, handling optional quotes around the folder name
    match = re.search(r'\((?P<flags>.*?)\)\s+"(?P<delimiter>.*?)"\s+(?P<name>.*)', folder_str)
    if match:
        name = match.group('name')
        # Strip surrounding quotes if they exist
        if name.startswith('"') and name.endswith('"'):
            name = name[1:-1]
        return name
    return None

def get_email_date(raw_email_bytes):
    """Extracts the original date from the email to preserve it during migration."""
    try:
        parsed_msg = email.message_from_bytes(raw_email_bytes)
        date_str = parsed_msg.get('Date')
        if date_str:
            date_tuple = email.utils.parsedate_tz(date_str)
            if date_tuple:
                timestamp = email.utils.mktime_tz(date_tuple)
                return imaplib.Time2Internaldate(timestamp)
    except Exception:
        pass
    return None

def main():
    src_mail = connect_to_imap(SOURCE_EMAIL, SOURCE_APP_PASSWORD)
    dst_mail = connect_to_imap(DEST_EMAIL, DEST_APP_PASSWORD)

    print("\nFetching labels from source account...")
    status, folders = src_mail.list()

    if status != 'OK':
        print("Failed to retrieve folders from the source account.")
        return

    folders_to_migrate = []
    for folder_data in folders:
        folder_name = parse_folder_name(folder_data)
        if folder_name and folder_name.startswith(LABEL_PREFIX_TO_MIGRATE):
            folders_to_migrate.append(folder_name)

    if not folders_to_migrate:
        print(f"No labels found starting with '{LABEL_PREFIX_TO_MIGRATE}'.")
        print("Please check the exact spelling of the label.")
        return

    print(f"\nFound {len(folders_to_migrate)} nested labels to migrate.")

    for folder in folders_to_migrate:
        print(f"\n--- Processing Label: {folder} ---")
        
        # 1. Automatically build the nested label structure in destination account
        # Gmail uses '/' as the delimiter. We create each level recursively
        # so you don't have to manually create the folders beforehand.
        parts = folder.split('/')
        current_path = ""
        for part in parts:
            if current_path == "":
                current_path = part
            else:
                current_path = f"{current_path}/{part}"
            
            # We attempt to create each level. (If it already exists, IMAP just ignores it)
            dst_mail.create(f'"{current_path}"')
            
        quoted_folder = f'"{folder}"' 
        
        # 2. Select the folder in the source account
        status, messages = src_mail.select(quoted_folder, readonly=True)
        if status != 'OK':
            print(f"Could not select folder {folder} in source. Skipping.")
            continue

        # 3. Search for all emails in this folder
        status, data = src_mail.search(None, 'ALL')
        if status != 'OK' or not data[0]:
            print(f"No emails found in {folder}.")
            continue

        email_ids = data[0].split()
        total_emails = len(email_ids)
        print(f"Found {total_emails} emails. Beginning transfer...")

        # 4. Fetch and append each email
        for index, e_id in enumerate(email_ids, 1):
            # Fetch raw email data and flags (read/unread status)
            typ, msg_data = src_mail.fetch(e_id, '(RFC822 FLAGS)')
            
            if typ != 'OK':
                print(f"  [{index}/{total_emails}] Failed to fetch email ID {e_id.decode()}")
                continue

            # Safely locate the tuple containing the email body and metadata
            raw_email = None
            meta_data = ""
            for response_part in msg_data:
                if isinstance(response_part, tuple):
                    meta_data = response_part[0].decode('utf-8', errors='ignore')
                    raw_email = response_part[1]
                    break
            
            if not raw_email:
                print(f"  [{index}/{total_emails}] Skipped. No valid payload found for ID {e_id.decode()}")
                continue

            # Parse Read/Unread/Starred flags
            flags_match = re.search(r'FLAGS \((.*?)\)', meta_data)
            # Use None instead of empty string to cleanly omit flags in IMAP APPEND
            imap_flags = f'({flags_match.group(1)})' if flags_match else None

            # Parse original date so emails don't all show up as "Today"
            imap_date = get_email_date(raw_email)

            # Append the email to the destination account
            try:
                dst_mail.append(quoted_folder, imap_flags, imap_date, raw_email)
                if index % 10 == 0 or index == total_emails:
                    print(f"  Migrated {index}/{total_emails} emails...")
            except Exception as e:
                print(f"  [{index}/{total_emails}] Error uploading email: {e}")

    print("\n✅ Migration complete! You can safely close this tool.")
    src_mail.logout()
    dst_mail.logout()

if __name__ == "__main__":
    main()