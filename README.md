<<<<<<< HEAD

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
=======
# TerminalGPT

TerminalGPT is a command-line interface (CLI) application that allows you to interact with OpenAI's GPT models. This tutorial provides instructions on how to set up and run the application, including creating an OpenAI API key and configuring environment variables.

## Prerequisites
- Python 3.6 or higher
- pip (Python package installer)

## Installation

### Clone the Repository:
```bash
git clone <repository-url>
cd <repository-directory>
```

### Install the Required Packages:
```bash
pip install -r requirements.txt
```

## Setting up an OpenAI API Key

1. **Create an OpenAI API Key:**
   - Go to the [OpenAI API Key page](https://platform.openai.com/api-keys) and sign up or log in.
   - Navigate to the API keys section in your account settings.
   - Create a new API key and copy it.

2. **Store the API Key in an Environment Variable:**
   - Create a `.env` file in the root directory of your project:
     ```bash
     touch .env
     ```
   - Open the `.env` file and add your API key:
     ```bash
     echo OPENAI_API_KEY_ENV="sk-proj..." >> .env
     ```

## Usage

### 1. Set up your Python Environment:
```bash
python3 -m venv venv
source venv/bin/activate
```

### 2. Install Necessary Packages:
```bash
pip install -r requirements.txt
```

### 3. Run the Application:
```bash
python gpt.py
```

### 4. Interact with TerminalGPT:
- The application will prompt you to enter a message.
- Type your message and press Enter.
- Type `exit` to quit the application.

## Example Interaction
```plaintext
$ python gpt.py
Welcome to TerminalGPT!
Type 'exit' to quit.

You: Hello, how are you?
ChatGPT: I'm an AI language model, so I don't have feelings, but I'm here to help you!

You: exit
Goodbye!
```

## Code Overview

### `gpt.py`
- This script initializes the OpenAI client using the API key from the `.env` file.
- Provides a user-friendly CLI to interact with the GPT model.
- Includes streaming functionality for real-time responses.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any changes.

---

This README provides a comprehensive guide to setting up and using TerminalGPT, including creating an OpenAI API key and configuring environment variables.
>>>>>>> 692694e (Initial commit)
