---
name: initiative-onboarding
description: "Onboard tools to initiatives like liluts - migrate code, rebrand, add community structures, initialize git. Use when: onboarding a tool to an initiative with parameters like source repo, target name, branding details."
---

# Initiative Onboarding Skill

This skill handles the process of onboarding a tool to a Keplar Flow initiative.

## Workflow Steps

1. **Explore Source**: Use subagents to explore the source repository and understand the codebase.
2. **Plan Migration**: Determine migration strategy, rebranding needs, and required structures.
3. **Create Target Repo**: Initialize local repository with migrated code.
4. **Rebrand**: Update names, titles, documentation, and code strings as needed.
5. **Add Structures**: Add community files (README, CONTRIBUTING, LICENSE, issue/PR templates, .env.example).
6. **Initialize Git**: Set up git repository, configure user, commit changes.
7. **Validate**: Run tests or basic validation to ensure functionality.

## Parameters
- Source repository URL or path
- Target initiative name (e.g., liluts)
- Tool name
- Branding details (new names, emails, etc.)
- Platform targets (web, desktop, iOS)

## Tools Used
- semantic_search, grep_search for exploration
- create_directory, create_file for setup
- replace_string_in_file for rebranding
- run_in_terminal for git operations
- Subagents for complex tasks

## Future Enhancements
- Automated GitHub repo creation
- Web UI generation for CLI tools
- Deployment setup (GitHub Pages, Actions)
- Integration with Liquid AI LEAP for on-device