#!/bin/bash

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "Python is not installed. Installing..."
    brew install python3
fi

# Install required Python packages
pip install -r requirements.txt

# Move the app to Applications
mv dist/your_script.app /Applications/MyApp.app

echo "Installation complete! You can find MyApp in the Applications folder."
