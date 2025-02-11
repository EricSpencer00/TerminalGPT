
# AI-Powered Terminal Tools

This repository contains two powerful terminal-based applications that integrate with OpenAI's API:

1. **terminalGPT** - A ChatGPT-powered interactive terminal chatbot.
2. **AI Shell Assistant** - An AI-assisted terminal application that translates natural language requests into shell commands and executes them safely.

## Table of Contents
- [AI Shell Assistant](#ai-shell-assistant)
  - [Features](#features)
  - [Installation](#installation)
  - [Usage](#usage)
- [terminalGPT](#terminalgpt)
  - [Features](#features-1)
  - [Installation](#installation-1)
  - [Usage](#usage-1)
- [Environment Variables](#environment-variables)
- [License](#license)

---

## AI Shell Assistant

AI Shell Assistant is a CLI tool that converts natural language instructions into shell commands. It ensures safety by filtering dangerous commands and requires user confirmation before execution.

### Features
- Converts plain-English requests into shell commands.
- Ensures safe execution by sanitizing commands.
- Asks for confirmation before running potentially harmful operations.
- Uses OpenAI's GPT model to generate shell commands.

### Installation
Ensure you have Python installed, then install dependencies:

```sh
pip install openai termcolor
```

Clone the repository:

```sh
git clone https://github.com/yourusername/repository.git
cd repository
```

### Usage
Run the AI Shell Assistant:

```sh
python ai_shell_assistant.py
```

Then enter your request in natural language, and it will suggest safe shell commands.

---

## terminalGPT

terminalGPT is an interactive chatbot that allows real-time conversations with OpenAI's models directly from your terminal.

### Features
- Provides a real-time chat experience in the terminal.
- Supports streaming responses for smooth conversation.
- Handles termination gracefully with Ctrl+C.
- Maintains conversation history during the session.

### Installation
Install dependencies:

```sh
pip install openai termcolor python-dotenv
```

Clone the repository:

```sh
git clone https://github.com/yourusername/repository.git
cd repository
```

### Usage
Run the chatbot:

```sh
python terminalGPT.py
```

Simply type your messages and get instant responses from GPT.

---

## Environment Variables

Both applications require an OpenAI API key. Create a `.env` file in the project directory and add:

```sh
OPENAI_API_KEY_ENV=your_openai_api_key
```

Alternatively, export the key in your terminal session:

```sh
export OPENAI_API_KEY_ENV=your_openai_api_key
```

---

## License
This project is open-source. You can modify and distribute it freely.

---

Enjoy using AI in your terminal! 🚀