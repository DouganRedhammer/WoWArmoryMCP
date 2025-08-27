# WoW Armory MCP Server

A Model Context Protocol (MCP) server that provides access to World of Warcraft Armory data and functionality.

## Overview

This MCP server enables AI assistants to interact with World of Warcraft character information through Blizzard's Armory website, providing tools for character lookups and reputation tracking.

## Prerequisites

- Python 3.8 or higher
- [uv](https://docs.astral.sh/uv/) package manager
- Git

## Installation

1. **Clone the repository:**

   ```bash
   git clone <repository-url>
   cd wow-armory-mcp
   ```

2. **Set up virtual environment:**

   ```bash
   uv venv
   ```

3. **Install dependencies:**
   ```bash
   uv pip install -r pyproject.toml
   ```

> **Note:** The command installs dependencies from `pyproject.toml` rather than a traditional `requirements.txt` file.

## Configuration

### Claude Desktop Integration

To use this MCP server with Claude Desktop, add the following configuration to your Claude Desktop settings:

**Location of config file:**

- **macOS:** `~/Library/Application Support/Claude/claude_desktop_config.json`
- **Windows:** `%APPDATA%\Claude\claude_desktop_config.json`

**Configuration:**

```json
{
  "mcpServers": {
    "wow-armory": {
      "command": "uv",
      "args": [
        "--directory",
        "/path/to/your/wow-armory-mcp",
        "run",
        "server.py"
      ]
    }
  }
}
```

> **Important:** Replace `/path/to/your/wow-armory-mcp` with the actual absolute path to your cloned repository.

### Environment Variables

If your server requires API credentials or configuration, create a `.env` file in the project root:

```bash
# Add any required environment variables here
# Example:
# WOW_API_KEY=your_api_key_here
```

## Usage

Once configured, restart Claude Desktop. The WoW Armory server will automatically start when Claude needs to access WoW-related information.

### Available Tools

The server provides tools for interacting with WoW Armory data:

- **Character Information** - Get detailed character information including level, class, race, and gear
- **Character Reputation** - Retrieve character reputation standings with various factions

## Development

### Running the Server Manually

For development and testing:

```bash
# Activate the virtual environment
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Run the server
python server.py
```

### Project Structure

```
wow-armory-mcp/
├── server.py          # Main MCP server implementation
├── pyproject.toml      # Project dependencies and metadata
├── .env               # Environment variables (create this)
├── README.md          # This file
└── src/               # Source code directory
    ├── __init__.py
    ├── armory/        # Armory API client
    ├── tools/         # MCP tool implementations
    └── utils/         # Utility functions
```

## Troubleshooting

### Common Issues

1. **"Command not found: uv"**

   - Install uv following the [official documentation](https://docs.astral.sh/uv/)

2. **"Permission denied" errors**

   - Ensure the path in your Claude Desktop config uses forward slashes, even on Windows
   - Verify the absolute path is correct

3. **API authentication failures**

   - Verify any required API credentials are properly configured
   - Check your `.env` file if authentication is required

4. **Server won't start**
   - Verify all dependencies are installed: `uv pip list`
   - Check the server logs for specific error messages

### Debugging

Enable debug logging by setting the environment variable:

```bash
export MCP_LOG_LEVEL=debug
```

## Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature-name`
3. Make your changes and add tests
4. Commit your changes: `git commit -am 'Add some feature'`
5. Push to the branch: `git push origin feature-name`
6. Submit a pull request

## License

MIT License

Copyright (c) 2025 Daniel Franklin

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

## Support

For issues and questions:

- Open an issue on GitHub
- Check the [MCP documentation](https://spec.modelcontextprotocol.io/)
- Review Blizzard's Armory website documentation

## Changelog

### [1.0.0-beta] - 08-27-2025

- Initial release
- Basic character and guild lookup functionality
- Integration with Claude Desktop
