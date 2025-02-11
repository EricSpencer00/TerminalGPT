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
