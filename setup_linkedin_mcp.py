#!/usr/bin/env python3
"""Auto-setup script for LinkedIn MCP Learning Project."""

import os
import subprocess
import sys
from pathlib import Path

class LinkedInMCPSetup:
    """Setup manager for LinkedIn MCP project."""
    
    def __init__(self):
        self.root_dir = Path(__file__).parent
        self.venv_dir = self.root_dir / ".venv"
        self.linkedin_mcp_dir = self.root_dir / "linkedin-mcp-server"
        self.package_dir = self.root_dir / "linkedin_mcp"
        
    def print_header(self, text):
        """Print formatted header."""
        print("\n" + "="*60)
        print(f"  {text}")
        print("="*60 + "\n")
    
    def run_command(self, cmd, cwd=None, shell=False):
        """Run shell command."""
        try:
            result = subprocess.run(
                cmd if shell else cmd.split(),
                cwd=cwd or self.root_dir,
                check=True,
                capture_output=True,
                text=True,
                shell=shell
            )
            return result.stdout
        except subprocess.CalledProcessError as e:
            print(f"Error: {e.stderr}")
            return None
    
    def create_file(self, path, content):
        """Create file with content."""
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content)
        print(f"✓ Created: {path.relative_to(self.root_dir)}")
    
    def step_1_clone_linkedin_mcp(self):
        """Clone LinkedIn MCP server repository."""
        self.print_header("Step 1: Cloning LinkedIn MCP Server")
        
        if self.linkedin_mcp_dir.exists():
            print(f"LinkedIn MCP server already exists at {self.linkedin_mcp_dir}")
            return
        
        print("Cloning Hritik003/linkedin-mcp...")
        result = self.run_command(
            f"git clone https://github.com/hritik003/linkedin-mcp.git {self.linkedin_mcp_dir}"
        )
        
        if result is not None:
            print("✓ LinkedIn MCP server cloned successfully")
        else:
            print("✗ Failed to clone. Please run manually:")
            print(f"  git clone https://github.com/hritik003/linkedin-mcp.git {self.linkedin_mcp_dir}")
    
    def step_2_create_venv(self):
        """Create Python virtual environment."""
        self.print_header("Step 2: Creating Virtual Environment")
        
        if self.venv_dir.exists():
            print(f"Virtual environment already exists at {self.venv_dir}")
            return
        
        print("Creating virtual environment...")
        self.run_command(f"python -m venv {self.venv_dir}")
        print("✓ Virtual environment created")
    
    def step_3_create_project_files(self):
        """Create all project files."""
        self.print_header("Step 3: Creating Project Files")
        
        # requirements.txt
        requirements = """# MCP and LinkedIn dependencies
mcp>=1.0.0
httpx>=0.27.0
python-dotenv>=1.0.0
linkedin-api>=2.0.0
uv>=0.1.0
"""
        self.create_file(self.root_dir / "requirements.txt", requirements)
        
        # .env template
        env_template = """# LinkedIn Credentials
LINKEDIN_EMAIL=your_email@example.com
LINKEDIN_PASSWORD=your_password_here

# MCP Server Configuration
MCP_SERVER_HOST=127.0.0.1
MCP_SERVER_PORT=8000
MCP_SERVER_PATH=/mcp
"""
        self.create_file(self.root_dir / ".env", env_template)
        
        # .gitignore
        gitignore = """.env
.venv/
__pycache__/
*.pyc
*.pyo
*.pyd
.Python
*.so
*.egg
*.egg-info/
dist/
build/
.DS_Store
.vscode/
.idea/
"""
        self.create_file(self.root_dir / ".gitignore", gitignore)
        
        # Create linkedin_mcp package
        self.package_dir.mkdir(exist_ok=True)
        
        # linkedin_mcp/__init__.py
        init_content = """\"\"\"LinkedIn MCP Client Package.\"\"\"\n__version__ = \"1.0.0\"
"""
        self.create_file(self.package_dir / "__init__.py", init_content)
        
        # Continue in next part due to character limit...
