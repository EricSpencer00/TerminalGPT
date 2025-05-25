# AI-Powered Terminal Tools

This repository contains two terminal-based applications that integrate with OpenRouter's Deepseek model:

1. **TerminalGPT (gpt.py)** - An interactive chatbot that allows you to converse with an AI in your terminal.
2. **AI Shell Assistant (exe.py)** - A tool that translates natural language requests into shell commands and executes them safely.

## Table of Contents

- [Features](#features)
- [Installation and Setup](#installation-and-setup)
  - [Prerequisites](#prerequisites)
  - [Cloning the Repository](#cloning-the-repository)
  - [Setting Up the Python Environment](#setting-up-the-python-environment)
  - [Installing Required Packages](#installing-required-packages)
  - [Configuring the OpenRouter Deepseek Key](#configuring-the-openrouter-deepseek-key)
- [Usage](#usage)
  - [TerminalGPT (Chat Interface)](#terminalgpt-chat-interface)
  - [AI Shell Assistant (Command Generator/Executor)](#ai-shell-assistant-command-generatorexecutor)
- [Repository Structure](#repository-structure)
- [License](#license)

## Features

### TerminalGPT (gpt.py)
- Chat with an AI in real time from your terminal.
- Maintains conversation history during the session.

### AI Shell Assistant (exe.py)
- Converts plain-English requests into complete, executable shell commands.
- Sanitizes generated commands and prompts for confirmation before executing.
- Automatically handles errors with a retry mechanism.

## Installation and Setup

These instructions are aimed at Mac users who are new to using the Terminal.

### Prerequisites
- macOS with **Python 3.6** or higher installed.
- **Homebrew** package manager (if not installed, see below).
- Basic familiarity with the Terminal application.

### 1. Install Homebrew (if not already installed)
1. Open Safari and navigate to [https://brew.sh/](https://brew.sh/).
2. Follow the instructions on the website to install Homebrew.

### 2. Open the Terminal
- Press `Cmd + Space`, type **Terminal**, and press `Enter`.

### 3. Install Python 3
In the Terminal, run:
```bash
brew install python
```
This installs the latest version of Python 3 along with pip, Python's package installer.

### 4. Clone the Repository
Choose a directory (for example, your Desktop) and run:
```bash
cd ~/Desktop
git clone https://github.com/EricSpencer00/TerminalGPT.git
cd TerminalGPT
```

### 5. Set Up a Python Virtual Environment
It is recommended to use a virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate
```
Your Terminal prompt should now start with `(venv)`.

### 6. Install the Required Packages
Install the dependencies using:
```bash
pip install -r requirements.txt
```
*If a `requirements.txt` file is not provided, you can create one with at least the following packages:*
```
openai
python-dotenv
termcolor
```

### 7. Configure the OpenRouter Deepseek Key
Both applications require your Deepseek key from OpenRouter.
1. In the project directory, create a file named `.env`:
   ```bash
   touch .env
   ```
2. Open the `.env` file in your preferred text editor (TextEdit, VS Code, etc.) and add:
   ```bash
   OPENROUTER_API_KEY=your_deepseek_key
   ```
   Replace `your_deepseek_key` with your actual key.
3. Save the file.

## Usage

### TerminalGPT (Chat Interface)
To start the chat interface, run:
```bash
python gpt.py
```
- You will see a welcome message.
- Type your messages and press Enter to chat with the AI.
- To exit, type `exit` or `quit`.

### AI Shell Assistant (Command Generator/Executor)
To run the shell command assistant, execute:
```bash
python exe.py
```
- Enter your request in plain English (e.g., "Create a folder called myproject and navigate into it").
- The assistant will generate complete shell commands, display them, and ask for your confirmation before executing.
- Review the output and follow the prompts.

## Repository Structure

```
TerminalGPT/
├── gpt.py               # TerminalGPT chatbot application
├── exe.py               # AI Shell Assistant application
├── requirements.txt     # Python dependenciesV
├── .env                 # Environment file with OPENROUTER_API_KEY (not committed)
└── README.md            # This documentation file
```

## License

This project is open-source and available for modification and distribution. See the [LICENSE](LICENSE) file for details.
