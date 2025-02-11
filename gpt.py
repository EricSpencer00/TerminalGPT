import os
from openai import OpenAI
from dotenv import load_dotenv
from termcolor import colored
import readline  # For command history navigation
import signal  # For handling termination signals
import sys  # For program termination

# Load environment variables
load_dotenv()

# Initialize OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY_ENV"))
if not client.api_key:
    print(colored("Error: OpenAI API Key is not set.", "red"))
    exit()

<<<<<<< HEAD
# Set the model (comment/uncomment to switch)
# MODEL = "gpt-3.5-turbo"
MODEL = "gpt-4"
# MODEL = "gpt-4-turbo"

=======
>>>>>>> 692694e (Initial commit)
# Flag to handle termination
terminate_request = False
streaming_active = False

def handle_termination(signum, frame):
    global terminate_request, streaming_active
    if streaming_active:
        terminate_request = True
        print(colored("\nAttempting to terminate request...", "yellow"))
    else:
        print(colored("\nGoodbye!", "magenta"))
        sys.exit()  # Exit the program gracefully

# Register signal handler for SIGINT (Ctrl+C)
signal.signal(signal.SIGINT, handle_termination)

def chat_with_streaming():
    global terminate_request, streaming_active
    print(colored("Welcome to terminalGPT!", "green", attrs=["bold"]))
    print(colored("Type 'exit' to quit.", "yellow"))
<<<<<<< HEAD
    print(colored(f"Using model: {MODEL}", "cyan"))
=======
>>>>>>> 692694e (Initial commit)

    # Initialize conversation history
    conversation = []

    while True:
        try:
            user_input = input(colored("\nYou: ", "blue"))
        except KeyboardInterrupt:
            print(colored("\nGoodbye!", "magenta"))
            sys.exit()  # Exit the program gracefully

        # Exit condition
        if user_input.lower() == "exit":
            print(colored("Goodbye!", "magenta"))
            sys.exit()  # Exit the program gracefully

        # Sanitize user input
        user_input = user_input.strip()

        if not user_input:
            print(colored("Please enter a message.", "red"))
            continue

        # Add user input to conversation history
        conversation.append({"role": "user", "content": user_input})

        try:
            # Stream GPT response
            print(colored("\nChatGPT: ", "cyan"), end="", flush=True)
            stream = client.chat.completions.create(
<<<<<<< HEAD
                model=MODEL,
=======
                model="gpt-4",  # Replace with your preferred model
>>>>>>> 692694e (Initial commit)
                messages=conversation,
                stream=True,
            )
            response_content = ""
            streaming_active = True
            for chunk in stream:
                if terminate_request:
                    terminate_request = False
                    streaming_active = False
                    print(colored("\nRequest terminated by user.", "yellow"))
                    break
                # Safely access content attribute
                content = getattr(chunk.choices[0].delta, "content", None)
                if content:
                    print(colored(content, "cyan"), end="", flush=True)
                    response_content += content

            print()  # New line after the response
            streaming_active = False

            # Add ChatGPT's response to conversation history
            if not terminate_request:
                conversation.append({"role": "assistant", "content": response_content})

        except Exception as e:
            print(colored(f"Error: {e}", "red"))

if __name__ == "__main__":
    chat_with_streaming()
