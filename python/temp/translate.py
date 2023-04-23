import pyperclip
import subprocess
import time


def translate():
    clipboard = pyperclip.paste()
    subprocess.run(['trans', '-t', 'ru', clipboard], check=True)


while True:
    current_clipboard = pyperclip.paste()
    while current_clipboard == pyperclip.paste():
        time.sleep(3)
    translate()
