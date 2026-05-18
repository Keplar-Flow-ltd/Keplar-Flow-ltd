Here is the complete configuration detail and technical specification of my current GitHub Copilot capabilities within this VS Code environment. This document is formatted strictly as a data-feed for your external FinOps and architectural deep research.

***

# GitHub Copilot & VS Code Environment Specification
**System Context:** Keplar Flow Operations Center
**Architecture Paradigm:** Model Context Protocol (MCP) enabled, Multi-Agent Swarm, Tool-Augmented

## 1. Core Environment Specifications
- **Operating System Platform:** Windows (executing `PowerShell 5.1` by default)
- **Model Framework:** Liquid/Gemini logic equivalents bridged via GitHub Copilot
- **Memory Architecture (RAG):**
  - **User Scope:** Persistent cross-workspace memory (`/memories/`)
  - **Session Scope:** Ephemeral context for active tasks (`/memories/session/`)
  - **Repo Scope:** Workspace-bound facts and configurations (`/memories/repo/`)
- **Agentic Capability:** Supports autonomous multi-step reasoning, self-correction, parallel tool execution, and invoking sandboxed sub-agents.

## 2. Currently Enabled Tools & Capabilities (Built-In)
These are native capabilities that *do not require external API costs or separate subscriptions*. Leveraging these heavily will optimize your FinOps by reducing third-party SaaS dependencies.

### A. Terminal & Process Operations
- **`run_in_terminal`**: Full capability to execute `PowerShell` commands interactively, asynchronously (background daemons, servers), or synchronously with timeouts. 
- **`send_to_terminal` / `get_terminal_output`**: Can interact with long-running processes (e.g., passing auth strings, responding to CLI prompts) without human intervention.
- **`create_and_run_task`**: Can dynamically generate and execute `tasks.json` structures for build, deploy, or pipeline commands.

### B. Workspace & File System Manipulation
- **Read & Search**: `read_file`, `list_dir`, `file_search` (glob patterns), `grep_search` (Regex text search), `semantic_search` (NLP-based codebase querying).
- **Write & Refactor**: `create_file`, `create_directory`, `replace_string_in_file` (AST and literal-safe replacements). Can autonomously scaffold entirely new workspaces.
- **Git Integration**: `get_changed_files` to monitor diffs, staged, and unstaged states.

### C. Browser Automation & Data Ingestion (Cost-Saver vs. Firecrawl)
*Note: This native module can replace expensive data-scraping API subscriptions.*
- **DOM Interaction**: `navigate_page`, `click_element`, `type_in_page`, `hover_element`, `drag_element`, `handle_dialog`.
- **Parsing & Scraping**: `read_page` (accessibility tree snapshot), `screenshot_page`, `fetch_webpage` (direct HTML/text extraction).
- **Custom Playwright Execution**: `run_playwright_code` allows me to execute sandboxed JS/Playwright scripts to bypass scraping blocks and interact with complex web-apps directly.

### D. Advanced Code Structure & VS Code API
- **Symbols & Intellisense**: `vscode_listCodeUsages`, `vscode_renameSymbol`.
- **VS Code Extension Interaction**: `run_vscode_command`, `install_extension`, `vscode_searchExtensions_internal`.
- **Diagnostics**: `get_errors` (captures linter, compiler, and workspace errors directly).
- **User Interview Engine**: `vscode_askQuestions` (can halt execution to poll you for specific missing variables or API keys via native UI modals).

### E. Python, Jupyter & NotebookLM Workflows
- **Notebook Management**: `create_new_jupyter_notebook`, `edit_notebook_file`, `copilot_getNotebookSummary`, `run_notebook_cell`, `read_notebook_cell_output`.
- **Python Env Control**: `configure_python_environment`, `get_python_environment_details`, `install_python_packages`.
- **Pylance/Analysis Integration**: Instant execution of Python snippets in memory, syntax checking, and type annotation modifications.

### F. Specialized Sub-Agents (The "Swarm")
- **`runSubagent`**: Can spawn stateless child agents (e.g., `keplar-flow-orchestrator`, `Explore`) with specific contexts to parallelize research, codebase mapping, or isolated problem-solving without polluting the main conversation token limit.

---

## 3. Expandable Interoperability (MCP & Spoke Integrations)
Based on your agentic research, VS Code's core mechanism for interoperability is the **Model Context Protocol (MCP)**. This is how we map the "Spokes" (Notion, Drive, etc.). 

To enable seamless flow *without* losing custom capabilities, we can enable/configure these via `mcp.json` or native VS Code MCP configuration:

- **Notion Interoperability (The Knowledge Base)**
  - *Current Pathway:* Using the official `@modelcontextprotocol/server-notion`.
  - *FinOps Optimization:* Leverage my Python/Terminal tools to write a very lightweight, direct `requests`-based local script if the MCP server proves too heavy or misaligned. I can execute python scripts that push JSON directly to Notion using your `.env` key.
- **Google Drive / NotebookLM (The Analyst)**
  - *Current Pathway:* `@modelcontextprotocol/server-filesystem` mapped to your local sync folder OR a custom python Google Workspace MCP.
  - *FinOps Optimization:* I have native `list_dir` and `read_file` capabilities. If you install Google Drive Desktop mirroring, I do *not* need an API or MCP server to push to NotebookLM. I can natively write `markdown` nodes directly to the local Drive sync directory using `create_file`, triggering Google Drive's auto-sync. **Cost: $0.**
- **Firecrawl / Web Research (The Senses)**
  - *Current Pathway:* `firecrawl-mcp`.
  - *FinOps Optimization:* Using my built-in `fetch_webpage` and `run_playwright_code` tools, I can natively crawl and parse websites. Only configure the Firecrawl MCP if proxy-rotation/captchas become an insurmountable bottleneck.

---

## 4. Custom Skill & Instruction Loading
The system dynamically loads domain knowledge via YAML/Markdown frontmatter based on folder structure matching:
- **Instructions:** copilot-instructions.md establishes my foundational rules.
- **Skills:** SKILL.md files (e.g., `initiative-onboarding`, `agent-customization`) are pulled dynamically into my context depending on user intent. 
- *To scale workflows,* you can define entirely new operational protocols (like the Gom Chambers legal logic) within `.github/skills/gom-chambers-logic/SKILL.md`.

## FinOps & Operations Summary for External Research
To achieve your goal of **Unified Agentic Interoperability** with minimum investment:
1. **Bypass paid scraping (Firecrawl) initially:** Tell your external research system to map scraping requests to my native `run_playwright_code` and `fetch_webpage` tools.
2. **Bypass heavy Google Drive APIs:** Utilize the local Filesystem MCP or my native `create_file` targeting a mirrored desktop cloud folder.
3. **Use Notion REST API via Terminal:** Instead of running an always-on Node.js MCP server consuming local RAM/CPU, I can be instructed to generate and execute ephemeral Python scripts that parse `.env`, build the JSON schema, and `POST` to Notion APIs natively.
4. **Agent Orchestration:** Use my `mcp_pylance_mcp_s_pylanceRunCodeSnippet` to execute high-speed, zero-file data transformations (e.g., legal tenancy countdown calculations) entirely in RAM.

Provide this spec sheet directly to the external deep research system to allow it to architect the exact configuration `.json` files, `.env` mappings, and Python glue-scripts required for the upcoming Gom Chambers requires, with the aim of establishing the minimum value creation system we will build on for our enterprise operations.