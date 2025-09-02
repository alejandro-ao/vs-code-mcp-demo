# MCP Server Example for VS Code Crash Course

> This repository is support material for the **MCP for VS Code Crash Course** available on YouTube. It demonstrates how to create and implement Model Context Protocol (MCP) servers, specifically for integration with Visual Studio Code.
>
> YouTube Video here: 

## Purpose

This project provides a minimal, practical example of an MCP server. Its main goal is to help developers understand:
- How MCP servers work
- How to implement and run an MCP server
- How to integrate MCP servers with VS Code

## What is MCP?

Model Context Protocol (MCP) is a protocol designed to enable context-aware AI and automation in development environments. MCP servers provide context, data, and services to clients like VS Code extensions.

## Repository Contents

- `main.py`: Entry point for the MCP server
- `server.py`: Core server logic
- `mock_confluence_service.py`: Example/mock integration for context services
- `pyproject.toml`: Python project configuration
- `uv.lock`: Dependency lock file

## How to Use

1. **Clone the repository:**
   ```sh
   git clone https://github.com/your-username/2025-06--3-mcp-python-vs-code.git
   cd 2025-06--3-mcp-python-vs-code
   ```
2. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   # or use poetry if preferred
   poetry install
   ```
3. **Run the MCP server:**
   ```sh
   python main.py
   ```
4. **Integrate with VS Code:**
   - Follow the crash course on YouTube for step-by-step instructions on connecting this server to VS Code.

## Crash Course Video

Watch the full crash course on YouTube for a guided walkthrough:
- [MCP for VS Code Crash Course](https://www.youtube.com/playlist?list=YOUR_PLAYLIST_ID)

## License

MIT License

## Contributing

This repository is for educational purposes. Contributions, issues, and suggestions are welcome!