import os
import subprocess
import sys
from PyQt6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QTextEdit
)
from PyQt6.QtCore import Qt
from openai import OpenAI
from termcolor import colored
from dotenv import load_dotenv

load_dotenv()

# Configuration
AUTO_RETRY_ERRORS = True  
MAX_RETRIES = 3  

MODEL = "deepseek/deepseek-chat:free"

def start_terminal():
    """Launches the app in a new terminal window."""
    if sys.platform == "darwin":  # macOS
        subprocess.run(["open", "-a", "Terminal", sys.executable, __file__])
    elif sys.platform == "win32":  # Windows
        subprocess.run(["start", "cmd", "/k", f"python {__file__}"], shell=True)
    else:  # Linux
        subprocess.run(["gnome-terminal", "--", "python3", __file__])

class CLIApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("AI-Powered CLI Companion")
        self.setGeometry(100, 100, 500, 400)

        layout = QVBoxLayout()

        # Label and Input for OpenAI API Key
        self.api_key_label = QLabel("Enter OpenAI API Key:")
        layout.addWidget(self.api_key_label)
        self.api_key_input = QLineEdit()
        self.api_key_input.setEchoMode(QLineEdit.EchoMode.Password)
        layout.addWidget(self.api_key_input)

        # Start Terminal Button
        self.terminal_button = QPushButton("Launch Terminal")
        self.terminal_button.clicked.connect(self.launch_terminal)
        layout.addWidget(self.terminal_button)

        # Command Input and Output
        self.command_label = QLabel("Enter Command Request:")
        layout.addWidget(self.command_label)
        self.command_input = QLineEdit()
        layout.addWidget(self.command_input)

        self.run_button = QPushButton("Run Command")
        self.run_button.clicked.connect(self.run_command)
        layout.addWidget(self.run_button)

        self.output_area = QTextEdit()
        self.output_area.setReadOnly(True)
        layout.addWidget(self.output_area)

        self.setLayout(layout)

    def launch_terminal(self):
        os.environ['OPENROUTER_API_KEY'] = self.api_key_input.text()
        start_terminal()

    def run_command(self):
        os.environ['OPENROUTER_API_KEY'] = self.api_key_input.text()
        user_request = self.command_input.text()
        if user_request.strip():
            messages = [
                {"role": "system", "content": (
                    "You are a highly capable shell command generator that converts plain-English requests "
                    "into fully self-contained, executable shell commands for a Unix-like environment. "
                    "You must produce all necessary commands so that the user never needs to perform any manual steps. "
                    "\n\nCompleteness: Generate complete commands that include any prerequisite steps "
                    "(e.g., if a referenced folder does not exist, include a command such as `mkdir -p` to create it). "
                    "\n\nClarity & Safety: If the request is ambiguous, incomplete, or potentially dangerous "
                    "(e.g., commands that could result in data loss or system instability), ask for clarification before proceeding. "
                    "\n\nNo Placeholders: Do not use placeholders like `/path/to/folder` or `<argument>`. "
                    "All paths and arguments must be explicitly specified. "
                    "\n\nFormatting: Output only the final command(s) without any extra commentary, "
                    "markdown formatting, code fences, or additional text. "
                    "\n\nMultiple Commands: If more than one command is required, list each command on a separate line in the correct execution order. "
                    "\n\nEdge Cases: Always consider dependencies, file/directory existence, and command safety "
                    "(e.g., using flags for non-interactive execution if needed). "
                    "Your response should consist solely of the final command(s) ready for execution."
                )},
                {"role": "user", "content": user_request}
            ]
            response = self.get_ai_command(messages)
            if response:
                commands = self.sanitize_command(response)
                if commands:
                    output, errors = self.execute_command(commands)
                    self.output_area.setText(f"Output:\n{output}\nErrors:\n{errors}")

    def get_ai_command(self, messages):
        """Interacts with OpenAI to generate a shell command."""
        try:
            client = OpenAI(
                base_url="https://openrouter.ai/api/v1",
                api_key=os.getenv("OPENROUTER_API_KEY")
            )
            response = client.chat.completions.create(
                model=MODEL,
                messages=messages,
                temperature=0,
            )
            return response.choices[0].message.content.strip()
        except Exception as e:
            return f"Error: {e}"

    def sanitize_command(self, command):
        """Sanitizes the command(s) by removing extra spaces and blocking dangerous ones."""
        lines = command.strip().split('\n')
        cleaned_lines = []
        dangerous_keywords = ["rm", "sudo", "chmod", "chown", "curl", "wget"]
        for line in lines:
            line = line.strip()
            if not line or any(keyword in line for keyword in dangerous_keywords):
                return None
            cleaned_lines.append(line)
        return cleaned_lines if cleaned_lines else None

    def execute_command(self, commands):
        """Runs the sanitized shell command(s)."""
        all_output, all_errors = "", ""
        for cmd in commands:
            try:
                print(colored(f"\nRunning: {cmd}", "yellow", attrs=["bold"]))
                result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
                if result.stdout:
                    all_output += result.stdout
                if result.stderr:
                    all_errors += result.stderr
            except Exception as e:
                all_errors += str(e)
        return all_output.strip(), all_errors.strip()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CLIApp()
    window.show()
    sys.exit(app.exec())
