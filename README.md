# Typewriter-Bot

Typewriter-Bot is an automated typing tool designed to interact with the typewriter.at platform. It includes a bot for automated typing, a UI for managing typing speed and error rates across different levels, and an executable for easy access.

## Components

1. `TypewriterBot.py`: The main bot script for automated typing.
2. `Interface.py`: A graphical user interface for managing level data.
3. `typewriteBot.exe`: An executable version of the program for easy use without Python installation.
4. `level_data.json`: The storage for the user-generated information on the levels.
5. `logindata.json`: Saves the user name and password
   
## Features

### TypewriterBot.py

- Automated login to typewriter.at
- Simulates human-like typing with customizable speed and error rates
- Automatically adjusts typing parameters based on the current lesson
- Handles transitions between lessons
- Uses Selenium for web automation

### Interface.py

- Graphical interface for managing level data
- Allows manual input of speed and error rates for each level
- Supports applying mathematical functions to generate speed and error rates across multiple levels
- Saves and loads level data from a JSON file

### TypewriterBot.exe

- Standalone executable version of the program
- Includes all functionality of the Python scripts
- Runs on Windows without requiring Python installation

## Requirements

For running the Python scripts:
- Python 3.x
- Selenium
- ChromeDriver
- win10toast
- tkinter

For the executable:
- Windows operating system

## Setup

### For Python scripts:

1. Install the required Python packages:
   ```
   pip install selenium webdriver_manager win10toast
   ```

2. Ensure you have Google Chrome installed.

3. Create a `logindata.json` file or copy the existent `logindata.json` in the same directory as the scripts with your typewriter.at login credentials:
   ```json
   {
     "username": "your_username",
     "password": "your_password"
   }
   ```

### For executable:

1. Simply download the `TypewriterBot.exe` file.
2. Create a `logindata.json` file or copy the existent `logindata.json` in the same directory as the executable with your login credentials (as shown above).

## Usage

### Python scripts:

1. Run the UI to set up level data:
   ```
   python Interface.py
   ```
   Use this interface to set speed and error rates for different levels, or apply functions to generate these values across multiple levels.

2. Run the bot:
   ```
   python TypewriterBot.py
   ```
   The bot will log in to typewriter.at and start typing automatically based on the configured settings.

### Executable:

1. Double-click on `typewriterBot.exe` to run the program.
2. Follow the on-screen instructions to configure settings and start the bot.

## Customization

- Adjust the `speed` and `error_rate_percent` variables in `typewriterBot.py` to fine-tune the bot's behavior.
- Use the UI to create custom speed and error rate profiles for different levels.

## Disclaimer

This bot is for educational purposes only. Be sure to comply with typewriter.at's terms of service when using automated tools.

## Contributing

Contributions, issues, and feature requests are welcome. Feel free to check [issues page](https://github.com/yourusername/typewriteBot/issues) if you want to contribute.

