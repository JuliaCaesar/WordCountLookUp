
import keyboard

print("Press 1 for more information or any other key to continue...")

while True:
    if keyboard.is_pressed('1'):
        print("Showing more information...")
        break
    elif keyboard.is_pressed():
        print("Continuing...")
        break