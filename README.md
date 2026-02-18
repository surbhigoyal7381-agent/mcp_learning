# LinkedIn MCP Learning Project

Complete Model Context Protocol (MCP) implementation for LinkedIn automation using Python on Windows.

## 🎯 What This Does

This project enables you to:
- Navigate your LinkedIn feed programmatically
- Search and apply for jobs automatically
- Read messages and notifications
- Extract profile data
- Automate LinkedIn browsing through MCP

Based on the [LinkedIn Assistant Navigation skill](https://mcpmarket.com/tools/skills/linkedin-assistant-navigation) and [Hritik003's LinkedIn MCP Server](https://github.com/hritik003/linkedin-mcp).

## 📋 Prerequisites

- Python 3.10 or higher
- Windows 10/11
- LinkedIn account
- Git installed

## 🚀 Quick Start

### Step 1: Clone This Repository

```powershell
git clone https://github.com/surbhigoyal7381-agent/mcp_learning.git
cd mcp_learning
```

### Step 2: Run Auto-Setup Script

```powershell
python setup_linkedin_mcp.py
```

This will automatically:
- Clone the LinkedIn MCP server
- Create virtual environment
- Install all dependencies
- Create configuration template

### Step 3: Configure LinkedIn Credentials

Edit the `.env` file:

```env
LINKEDIN_EMAIL=your_email@example.com
LINKEDIN_PASSWORD=your_password_here
```

⚠️ **NEVER commit `.env` to GitHub!**

### Step 4: Start LinkedIn MCP Server

Open a new PowerShell terminal:

```powershell
cd mcp_learning
.\.venv\Scripts\activate
cd linkedin-mcp-server
uv run --directory . linkedin.py
```

The server will start on `http://127.0.0.1:8000/mcp`

### Step 5: Run Client Examples

In another PowerShell terminal:

```powershell
cd mcp_learning
.\.venv\Scripts\activate
python run_linkedin_mcp.py
```

## 📁 Project Structure

```
mcp_learning/
├── linkedin_mcp/              # Python MCP client package
│   ├── __init__.py
│   ├── client.py             # MCP client implementation
│   ├── config.py             # Configuration management
│   └── examples.py           # Usage examples
├── linkedin-mcp-server/       # LinkedIn MCP server (cloned)
├── .env                       # LinkedIn credentials (DO NOT COMMIT)
├── .gitignore                 # Git ignore file
├── requirements.txt           # Python dependencies
├── setup_linkedin_mcp.py      # Auto-setup script
├── run_linkedin_mcp.py        # Main execution script
└── README.md                  # This file
```

## 🔧 Manual Installation

If auto-setup doesn't work, follow these manual steps:

### 1. Clone LinkedIn MCP Server

```powershell
git clone https://github.com/hritik003/linkedin-mcp.git linkedin-mcp-server
```

### 2. Create Virtual Environment

```powershell
python -m venv .venv
.\.venv\Scripts\activate
```

### 3. Install Dependencies

```powershell
pip install -r requirements.txt
cd linkedin-mcp-server
pip install -r requirements.txt
cd ..
```

### 4. Install UV Package Manager

```powershell
pip install uv
```

## 💻 Usage Examples

### Get Your LinkedIn Profile

```python
import asyncio
from linkedin_mcp.client import LinkedInMCPClient

async def main():
    async with LinkedInMCPClient() as client:
        profile = await client.get_profile()
        print(f"Name: {profile.get('name')}")
        print(f"Headline: {profile.get('headline')}")

asyncio.run(main())
```

### Search for Jobs

```python
import asyncio
from linkedin_mcp.client import LinkedInMCPClient

async def main():
    async with LinkedInMCPClient() as client:
        jobs = await client.search_jobs(
            keywords="Python Developer",
            location="Remote",
            job_type="full-time",
            limit=10
        )
        for job in jobs.get('jobs', []):
            print(f"{job['title']} at {job['company']}")

asyncio.run(main())
```

### Get Feed Posts

```python
import asyncio
from linkedin_mcp.client import LinkedInMCPClient

async def main():
    async with LinkedInMCPClient() as client:
        feed = await client.get_feed_posts(limit=5)
        for post in feed.get('posts', []):
            print(f"Post by {post['author']}: {post['text'][:100]}...")

asyncio.run(main())
```

## 🔐 Security Notes

1. **Never commit `.env` file** - It contains your LinkedIn credentials
2. **Use app-specific passwords** if you have 2FA enabled
3. **Be respectful** of LinkedIn's terms of service
4. **Rate limiting** - Don't spam requests

## 🐛 Troubleshooting

### Server Won't Start

```powershell
# Check if UV is installed
uv --version

# If not, install it
pip install uv
```

### Authentication Errors

- Verify credentials in `.env` file
- If you have 2FA, use an app password
- Check LinkedIn for security notifications

### Connection Refused

- Ensure the MCP server is running
- Check if port 8000 is available
- Verify `MCP_SERVER_PORT` in `.env`

## 📚 Additional Resources

- [Model Context Protocol Documentation](https://modelcontextprotocol.io/)
- [LinkedIn MCP Server Repository](https://github.com/hritik003/linkedin-mcp)
- [MCP Market - LinkedIn Navigation Skill](https://mcpmarket.com/tools/skills/linkedin-assistant-navigation)
- [Unofficial LinkedIn API Docs](https://linkedin-api.readthedocs.io/)

## 🤝 Contributing

Feel free to open issues or submit pull requests to improve this project!

## 📝 License

MIT License - Feel free to use this for learning and personal projects.

## ⚠️ Disclaimer

This project uses unofficial LinkedIn APIs. Use at your own risk and ensure compliance with LinkedIn's terms of service.
