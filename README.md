#Typewriter-BOT
TypewriterBOT is an automated typing tool designed to interact with the typewriter.at platform. It includes a bot for automated typing and a UI for managing typing speed and error rates across different levels.

##How to use

pywriterPro.py: The main bot script for automated typing.
UI.py: A graphical user interface for managing level data.

Features
pywriterPro.py

Automated login to typewriter.at
Simulates human-like typing with customizable speed and error rates
Automatically adjusts typing parameters based on the current lesson
Handles transitions between lessons
Uses Selenium for web automation

UI.py

Graphical interface for managing level data
Allows manual input of speed and error rates for each level
Supports applying mathematical functions to generate speed and error rates across multiple levels
Saves and loads level data from a JSON file

Requirements

Python 3.x
Selenium
ChromeDriver
win10toast
tkinter

Setup

Install the required Python packages:
Copypip install selenium webdriver_manager win10toast

Ensure you have Google Chrome installed.
Create a logindata.json file in the same directory as the scripts with your typewriter.at login credentials:
jsonCopy{
  "username": "your_username",
  "password": "your_password"
}


Usage

Run the UI to set up level data:
Copypython UI.py
Use this interface to set speed and error rates for different levels, or apply functions to generate these values across multiple levels.
Run the bot:
Copypython pywriterPro.py
The bot will log in to typewriter.at and start typing automatically based on the configured settings.

Customization

Adjust the speed and error_rate_percent variables in pywriterPro.py to fine-tune the bot's behavior.
Use the UI to create custom speed and error rate profiles for different levels.

Disclaimer
This bot is for educational purposes only. Be sure to comply with typewriter.at's terms of service when using automated tools.
Contributing
Contributions, issues, and feature requests are welcome. Feel free to check issues page if you want to contribute.
License
MIT
