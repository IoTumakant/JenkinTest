#this is module for Geometry
import os
clear=lambda:os.system('clear')

import math

PI=3.14
# function: area_triange(Sides: a,b,c retn Area)
def area_triangle(side_1,side_2,side_3):
    sumside=side_1+side_2+side_3
    Areatriangle=math.sqrt(sumside*(sumside-side_1)*(sumside-side_2)*(sumside-side_3))
    return Areatriangle
#function: area_square(Side: a; retn Area)
def area_square(side):
    return side**2
#function: area_rectangel(Sides: a,b; retn Area)
def area_rectangle(side_1,side_2):
    return side_1*side_2
#function: area_circle(Radius: r; retn Area)
def area_circle(radius):
    return PI*radius**2

def menu_geometry():
    print("________________________________________________")
    print("T: Triangle\nC: Circle\nS: Square\nR: Rectangle\nQ: Quit")
    print("________________________________________________")


def operation_geo():
    while True: #"quit","QUIT","Exit","exit"):
        menu_geometry()
        choice_geo=input("Enter your choice:")
        clear()
        if choice_geo in ('q','Q'):
            break
        elif choice_geo in ('c','C'):
            radius=float(input("Enter radius of circle:"))
            print("Area:",area_circle(radius))
        elif choice_geo in ('t','T'):
            side_1=float(input("Enter side_1:"))
            side_2=float(input("Enter side_2:"))
            side_3=float(input("Enter side_2:"))
            print("Area:",area_triangle(side_1,side_2,side_3))
        elif choice_Geo in ('r','R'):
            Length=float(input("Enter Length:"))
            Width=float(input("Enter Width:"))
            print("Area:",area_rectangle(Length,Width))
        elif choice_geo in ('s','S'):
            side=float(input("Enter Side:"))
            print("Area:",area_square(side))
        else:
            print("Wrong choice!")


