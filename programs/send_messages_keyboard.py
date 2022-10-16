import pyautogui as spam
import time

length = int(input('Enter the limit: '))
Msg = input('Enter your message: ')

i = 0
time.sleep(10)

while i < length:
    spam.typewrite(Msg)
    spam.press('Enter')
    i = i + 1