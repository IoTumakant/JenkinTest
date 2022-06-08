import os
import sys
if sys.platform.startswith("linux"):  # could be "linux", "linux2", "linux3", ...
   #linux code
   clear=lambda:os.system('clear')
elif sys.platform == "darwin":
   #Mac code
   clear=lambda:os.system('clear')
elif sys.platform == "win32":
   #windows code
   clear=lambda:os.system('cls')
#Function for front page
def menu_frontPage():
    print("________________________________________________")
    print("M: Mathamatics\nG: Geometry\nS: String\nQ: Quit")
    print("________________________________________________")



import Geometry_Umakant as G
clear()
print("This is front page")

while True: #"quit","QUIT","Exit","exit"):
    menu_frontPage()
    choise_frontPage=input("Enter your choice:")
    clear()
    if choise_frontPage in ('q','Q'):
        print("Thanks!!!\n")
        break
    elif choise_frontPage in ('m','M'):
        print("Maths Function")
    elif choise_frontPage in ('G','g'):
        G.operation_Geo()
    elif choise_frontPage in ('S','s'):
        print("Text functions")
    else:
        print("Wrong Choice")
