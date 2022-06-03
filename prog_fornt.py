import os
clear=lambda:os.system('cls')
#Function for front page
def Menu_frontPage():
    print("________________________________________________")
    print("M: Mathamatics\nG: Geometry\nS: String\nQ: Quit")
    print("________________________________________________")



import Geometry_Umakant as G
print("This is front page")

while True: #"quit","QUIT","Exit","exit"):
    Menu_frontPage()
    choise_frontPage=input("Enter your choice:")
    clear()
    if choise_frontPage in ('q','Q'):
        break
    elif choise_frontPage=="M":
        print("Maths Function")
    elif choise_frontPage=="G":
        G.operation_Geo()
    elif choise_frontPage=="S":
        print("Text functions")
    else:
        print("Wrong Choice")
