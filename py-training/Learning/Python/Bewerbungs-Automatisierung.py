
from utils.funktions import *
import sys
import time
import keyboard

while True:
    clear()
    print("Drücke 1 um Vorlage anzusehen.")
    print("Drücke 2 um die Lücken zu füllen und sie zu speichern.")
    print("Drücke 3 für exit.")
    print("\n")
    menu = input("> ")

    for i in range(3):

        if menu == "1":

            clear()
            templ()
            time.sleep(10)
            break

        elif menu == "2":

            clear()
            out()
            clear()
            if keyboard.press_and_release("q"):
                break

        else:
            clear()
            sys.exit()