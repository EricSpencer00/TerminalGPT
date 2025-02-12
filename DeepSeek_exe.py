import os
import re
import subprocess
from openai import OpenAI
from termcolor import colored
from dotenv import load_dotenv

load_dotenv()

# Configuration: Set to False if you want to disable automatic error handling
AUTO_RETRY_ERRORS = True  
MAX_RETRIES = 3  

# Initialize OpenAI client using the new key and base URL (OpenRouter endpoint)
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY")
)

MODEL = "deepseek/deepseek-chat:free"

def sanitize_command(command):
    """
    Sanitizes the command(s) by removing extra newlines/spaces
    and disallowing '..'.
    Returns a list of command lines or None if blocked.
    """
    lines = command.strip().split('\n')
    cleaned_lines = []
    for line in lines:
        line = line.strip()
        if not line:
            continue
        if '..' in line:
            return None
        cleaned_lines.append(line)
    return cleaned_lines if cleaned_lines else None

def is_command_safe(commands):
    """
    Basic check for certain dangerous keywords.
    Expand or tighten as you see fit.
    """
    dangerous_keywords = ["rm", "sudo", "chmod", "chown", "curl", "wget"]
    for cmd in commands:
        lowered = cmd.lower()
        for keyword in dangerous_keywords:
            if keyword in lowered:
                return False
    return True

def run_command(commands):
    """
    Executes each command in sequence using subprocess.
    Returns output and error messages.
    """
    all_output = ""
    all_errors = ""
    
    for cmd in commands:
        try:
            print(colored(f"\nRunning: {cmd}", "yellow", attrs=["bold"]))
            result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
            
            if result.stdout:
                print(colored("Output:\n", "green") + result.stdout)
                all_output += result.stdout

            if result.stderr:
                print(colored("Errors:\n", "red") + result.stderr)
                all_errors += result.stderr

        except Exception as e:
            error_msg = f"Error executing command: {e}"
            print(colored(error_msg, "red", attrs=["bold"]))
            all_errors += error_msg

    return all_output.strip(), all_errors.strip()

def interact_with_chatgpt(messages):
    """
    Sends the conversation history to the OpenRouter API and gets the next response.
    """
    try:
        response = client.chat.completions.create(
            # Optional: include extra headers for OpenRouter (adjust or remove as needed)
            extra_headers={
                "HTTP-Referer": os.getenv("YOUR_SITE_URL", ""),
                "X-Title": os.getenv("YOUR_SITE_NAME", "")
            },
            extra_body={},
            model=MODEL,
            messages=messages,
            temperature=0,
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        print(colored(f"Error calling OpenAI API: {e}", "red", attrs=["bold"]))
        return None

def main():
    print(colored("Welcome to your AI-powered CLI companion!", "green", attrs=["bold"]))
    print(colored("Type 'quit' or 'exit' to stop.", "yellow"))
    print(colored(f"Automatic Error Handling: {'Enabled' if AUTO_RETRY_ERRORS else 'Disabled'}", "cyan"))

    # Start with an initial system message
    messages = [
        {
            "role": "system",
            "content": (
                "You are a highly capable shell command generator that converts plain-English requests "
                "into fully self-contained, executable shell commands for a Unix-like environment. "
                "You must produce all necessary commands so that the user never needs to perform any manual steps. "
                
                "Completeness: Generate complete commands that include any prerequisite steps "
                "(e.g., if a referenced folder does not exist, include a command such as `mkdir -p` to create it). "
                
                "Clarity & Safety: If the request is ambiguous, incomplete, or potentially dangerous "
                "(e.g., commands that could result in data loss or system instability), ask for clarification before proceeding. "
                
                "No Placeholders: Do not use placeholders like `/path/to/folder` or `<argument>`. "
                "All paths and arguments must be explicitly specified. "
                
                "Formatting: Output only the final command(s) without any extra commentary, "
                "markdown formatting, code fences, or additional text. "
                
                "Multiple Commands: If more than one command is required, list each command on a separate line in the correct execution order. "
                
                "Edge Cases: Always consider dependencies, file/directory existence, and command safety "
                "(e.g., using flags for non-interactive execution if needed). "
                
                "Your response should consist solely of the final command(s) ready for execution."
            )
        }
    ]

    while True:
        user_request = input(colored("\nEnter your request: ", "blue")).strip()
        if user_request.lower() in ["quit", "exit"]:
            print(colored("Exiting...", "magenta", attrs=["bold"]))
            break

        # Add the user's initial request to the conversation
        messages.append({"role": "user", "content": user_request})

        retry_count = 0  # Track retries

        while retry_count < MAX_RETRIES:
            # Interact with ChatGPT (via OpenRouter)
            response = interact_with_chatgpt(messages)
            if not response:
                print(colored("No response from the AI or an error occurred.", "red"))
                break

            # Display the response and check if it's a follow-up question
            print(colored("\nAI Response:", "cyan", attrs=["bold"]))
            print(colored(response, "cyan"))

            if "?" in response or "clarification" in response.lower():
                clarification = input(colored("\nYour clarification: ", "blue")).strip()
                messages.append({"role": "assistant", "content": response})
                messages.append({"role": "user", "content": clarification})
                continue  # Continue the loop for further clarification

            # If the response contains commands, sanitize and process them
            commands = sanitize_command(response)
            if not commands:
                print(colored("Command could not be sanitized or was blocked.", "red"))
                break

            # Show the sanitized commands
            print(colored("\nProposed command(s):", "yellow", attrs=["bold"]))
            for c in commands:
                print(colored(c, "yellow"))

            # Check for dangerous keywords
            if not is_command_safe(commands):
                print(colored("WARNING: The command seems to contain potentially dangerous keywords.", "red", attrs=["bold"]))
                confirm = input(colored("Are you sure you want to run this? (yes/no): ", "blue")).strip().lower()
                if confirm != "yes":
                    print(colored("Command canceled.", "red", attrs=["bold"]))
                    break

            # Final confirmation
            proceed = input(colored("Do you want to run these commands? (y/n): ", "blue")).strip().lower()
            if proceed == 'y':
                output, errors = run_command(commands)

                if errors and AUTO_RETRY_ERRORS:
                    retry_count += 1
                    print(colored(f"\nRetrying... (Attempt {retry_count}/{MAX_RETRIES})", "yellow"))

                    # Feed the error message back to ChatGPT
                    messages.append({"role": "assistant", "content": response})
                    messages.append({"role": "user", "content": f"The command failed with this error:\n{errors}\nPlease correct it and provide a new command."})
                    continue  # Retry with AI-generated fix
                else:
                    break  # Exit retry loop if no errors
            else:
                print(colored("Command execution canceled.", "red"))
                break  # Exit loop

if __name__ == "__main__":
    main()
