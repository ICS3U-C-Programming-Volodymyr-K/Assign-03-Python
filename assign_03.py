#!/usr/bin/env python3
# Created By: Volodymyr Kryzhanovskyi
# Date: 03 27, 2025
# This program creates the date answers.

import math

def main():
    a_str = input("Enter first variable in formula.")
    b_str= input("Enter second variable in formula.")
    c_str= input("Enter third variable for formula.")
    try:
        a_int = float(a_str)
        b_int = float(b_str)
        c_int = float(c_str)
        question_1 = input(
        "Is your quadratic equation in power of something? If it is, type yes, if it is not then type no")
        if question_1.lower() == "yes":
                power = input("Enter to what power will your quadratic equation be.")
                try:
                    power =float(power)
                    print(f"Your formula looks like, ({a_int}**{power}**{power} + {b_int}**{power}x**{power} + {c_int}**{power})")
                except ValueError:
                    print("Enter the float.")
        elif question_1.lower() == "no":
            print(f"Your formula looks like, {a_int}x**2 + {b_int}x + {c_int}")
            print("We will use the discriminant theory to find the roots of equation.")
            discriminant = b_int**2 -4*a_int*c_int
            try:
                discriminant >= 0
                x_one = (-b_int + math.sqrt(discriminant))/2*a_int
                x_two = (-b_int - math.sqrt(discriminant))/2*a_int
                print(f"The roots of quadratic problem are {x_one} and {x_two}")
            except Exception:
                print("Discriminant can't be negative.")
        question_2 = input("Do you want to calculate the parabola in vertex formula? Types yes if you want and no if you don't want.")
        if question_2.lower() == "yes."
    except ValueError:
        print("Correct input needed, look through comments or code to determine what variable you need.")
if __name__ == "__main__":
    main()
