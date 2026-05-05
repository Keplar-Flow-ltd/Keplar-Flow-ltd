param(
    [Parameter(Mandatory=$false)]
    [ValidateSet("Generate","Decode")]
    [string]$Mode = "Generate",
    [string]$Base64String,
    [int]$Length = 12
)

# Generate a strong password for ArgoCD that meets typical password complexity requirements:
# - At least 12 characters long
# - Contains at least one uppercase letter
# - Contains at least one lowercase letter
# - Contains at least one digit
# - Contains at least one special character

function Generate-StrongPassword {
    param (
        [int]$Length = 12
    )

    # Define character sets
    $upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    $lower = 'abcdefghijklmnopqrstuvwxyz'
    $digits = '0123456789'
    $special = '!@#$%^&*()-_=+[]{}|;:,.<>?'

    # Ensure at least one of each type
    $passwordChars = @()
    $passwordChars += $upper[(Get-Random -Maximum $upper.Length)]
    $passwordChars += $lower[(Get-Random -Maximum $lower.Length)]
    $passwordChars += $digits[(Get-Random -Maximum $digits.Length)]
    $passwordChars += $special[(Get-Random -Maximum $special.Length)]

    # Fill the rest with random characters from all sets
    $allChars = $upper + $lower + $digits + $special
    for ($i = 4; $i -lt $Length; $i++) {
        $passwordChars += $allChars[(Get-Random -Maximum $allChars.Length)]
    }

    # Shuffle the array to randomize order
    $passwordChars = $passwordChars | Sort-Object { Get-Random }

    # Join into a string
    $password = -join $passwordChars

    return $password
}

if ($Mode -eq "Generate") {
    # Generate and output the password
    $generatedPassword = Generate-StrongPassword -Length $Length
    Write-Output "Generated ArgoCD Password: $generatedPassword"
} elseif ($Mode -eq "Decode") {
    if (-not $Base64String) {
        Write-Output "Error: Base64String parameter is required for Decode mode."
    } else {
        # Decode the Base64 string
        try {
            $decodedString = [System.Text.Encoding]::UTF8.GetString([System.Convert]::FromBase64String($Base64String))
            Write-Output "Decoded Password: $decodedString"
        } catch {
            Write-Output "Error: Invalid Base64 string."
        }
    }
}

Read-Host "Press Enter to exit"