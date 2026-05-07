---
name: initiative-onboarding
description: "Onboard tools to initiatives like liluts - migrate code, rebrand, add community structures, initialize git. Use when: onboarding a tool to an initiative with parameters like source repo, target name, branding details."
---

# Initiative Onboarding Skill

This skill handles the process of onboarding a tool to a Keplar Flow initiative.

## Workflow Steps

1. **Clone Source**: If source is a GitHub URL, clone the repository locally.
2. **Explore Source**: Use subagents to explore the cloned/local repository and understand the codebase.
3. **Plan Migration**: Determine migration strategy, rebranding needs, and required structures.
4. **Create Target Repo**: Initialize local repository with migrated code.
5. **Rebrand**: Update names, titles, documentation, and code strings as needed.
6. **Add Structures**: Add community files (README, CONTRIBUTING, LICENSE, issue/PR templates, .env.example).
7. **Initialize Git**: Set up git repository, configure user, commit changes.
8. **Validate**: Run tests or basic validation to ensure functionality.

## Parameters
- Source repository URL (GitHub) or local path
- Target initiative name (e.g., liluts)
- Tool name
- Branding details (new names, emails, etc.)
- Platform targets (web, desktop, iOS)

## Tools Used
- run_in_terminal for git clone/operations
- semantic_search, grep_search for exploration
- create_directory, create_file for setup
- replace_string_in_file for rebranding
- Subagents for complex tasks

## Future Enhancements
- Automated GitHub repo creation
- Web UI generation for CLI tools
- Deployment setup (GitHub Pages, Actions)
- Integration with Liquid AI LEAP for on-device