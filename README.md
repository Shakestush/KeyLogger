# KeyLogger
This is a simple Python-based keylogger that captures keyboard input and sends it to an email. The keylogger runs in the background and logs keystrokes, then periodically sends them to your specified email address.
# Features
- Captures keystrokes in real-time.
- Logs alphanumeric characters and special keys (e.g., space, enter).
- Periodically sends the captured keystrokes to an email address.
- Lightweight and runs in the background.
# Prerequisites
Make sure you have the following installed:
- Python 3
- pynput library for capturing keystrokes.

# Setting Up the Keylogger
1. Clone or Download the Project
Download the project files to your local machine.

_git clone https://github.com/shakestush/keylogger.git_

2. Modify the Script
Open the keylogger.py script and update the following:

- Sender Email: Replace with your email address.
- Recipient Email: Replace with the email where you want to receive the keystrokes.
- App Password: If using Gmail, you will need to generate an App Password instead of using your regular email password (due to Google’s 2-step verification).
3. Run the Script
Execute the script in your terminal:

_python keylogger.py_
- The script will now capture keystrokes and send the logs to the specified email periodically.

# How It Works
1. Keystroke Logging: The pynput library is used to listen for key presses. Each key is logged and stored in the log variable.
2. Sending Logs: Every 60 seconds, the captured keystrokes are sent to the specified email via Gmail's SMTP server.
3. Email Credentials: The email login details (sender's email and app password) are required to send the logs.

# Ethical Usage
- This tool should only be used in environments where you have explicit consent. You are responsible for the legal and ethical implications of using this software.
- Do not use this tool on machines or networks without permission. Unauthorized use is illegal.

# Limitations
- The keylogger works only on the machine it's running on.
- It uses SMTP to send logs, which may be blocked by some email providers if flagged as suspicious.
- This keylogger is not designed to capture all types of input (e.g., mouse movements, clipboard content).

# Troubleshooting
- Gmail Login Error: If Gmail rejects the login attempt, ensure that you've enabled 2-Step Verification and generated an App Password. Do not use your regular email password.
- Antivirus Software: Some antivirus programs may flag the keylogger as malicious. Disable antivirus software only for testing purposes, but be aware of the security risks.

# Contributions
Feel free to submit issues or pull requests if you'd like to contribute to this project.

# License
- This project is for educational use only. Use it at your own risk.
