#!/usr/bin/env python3
# Created By: Volodymyr Kryzhanovskyi
# Date: 03 27, 2025
# This program  solves quadratic equations and converts into vertex form.
import math  # Importing the math library for mathematical operations


def main():
    # Taking input for the coefficients of the quadratic equation
    a_str = input("Enter first variable in formula.")
    b_str = input("Enter second variable in formula.")
    c_str = input("Enter third variable for formula.")

    try:
        # Attempting to convert input strings to floats
        a_int = float(a_str)
        b_int = float(b_str)
        c_int = float(c_str)

        # Asking user if they want to calculate the parabola using vertex formula
        question_2 = input(
            "Do you want to calculate the parabola in vertex formula? Types yes if you want and no if you don't want.")

        if question_2 == "yes":
            # Print the original quadratic formula
            print(f"Your formula looks like, {a_int}x**2 + {b_int}x + {c_int}")
            e_int = b_int / a_int  # Calculate vertex x-coordinate
            # Calculate half of the coefficient for vertex form
            d_int = (e_int / 2)**(2)
            if b_int < 0:
                c_int = a_int * -d_int + c_int  # Adjust constant if b is negative
                print(
                    f"Your formula looks like {a_int} (x - {math.sqrt(d_int)}) + {c_int}")
            elif b_int > 0:
                c_int = a_int * -e_int + c_int  # Adjust constant if b is positive
            print(
                f"Your formula in vertex looks like {a_int}(x + {math.sqrt(d_int)}) {c_int}")

        elif question_2.lower() == "no":
            # Asking if the quadratic has a power
            question_1 = input(
                "Is your quadratic equation in power of something? If it is, type yes, if it is not then type no")
            if question_1.lower() == "yes":
                # Taking input for the power of the quadratic equation
                power = input(
                    "Enter to what power will your quadratic equation be.")
                try:
                    power = float(power)  # Convert power input to float
                    a_int**(power) + b_int**(power) + \
                        c_int**(power)  # Placeholder calculation
                    x_power = 2**(power)  # Calculate resulting power
                    print(
                        f"The formula will look like,{a_int**(power)}x**{x_power} + {b_int**(power)}x**{power} + {c_int**(power)}")

                    # Simplifying the coefficients based on the given power
                    a_int = a_int ** (1/power)
                    b_int = b_int ** (1/power)
                    c_int = c_int ** (1/power)
                    print(
                        f"The simplified formula will look like {power}√ over each number {a_int}x**2 + {b_int}x + {c_int}")
                    print(
                        "We will use the discriminant theory to find the roots of equation.")

                    discriminant = b_int**2 - 4*a_int*c_int  # Calculate the discriminant
                    try:
                        discriminant >= 0  # Ensure discriminant is non-negative
                        if discriminant > 0:
                            if discriminant == 0:
                                # If discriminant is zero, handle the case
                                if b_int < 0:
                                    # Square root for negative b
                                    a_int = math.sqrt(a_int)
                                    c_int = math.sqrt(c_int)
                                    print(
                                        f"Your quadratic equation will look like, ({a_int} - {c_int})**2")
                                elif b_int > 0:
                                    # Square root for positive b
                                    a_int = math.sqrt(a_int)
                                    c_int = math.sqrt(c_int)
                                    print(
                                        f"Your quadratic equation will look like, ({a_int}+{b_int})**2")
                            # Calculate the roots of the quadratic equation
                            x_one = (-b_int + math.sqrt(discriminant))/(2*a_int)
                            x_two = (-b_int - math.sqrt(discriminant))/(2*a_int)
                            print(
                                f"The roots of quadratic problem are {x_one} and {x_two}")
                    except Exception:
                        # Handle negative discriminant exception
                        print("Discriminant can't be negative.")

                except ValueError:
                    print("Enter the float.")  # Handle invalid float input

            elif question_1.lower() == "no":
                # Printing the standard form of the quadratic equation
                print(
                    f"Your formula looks like, {a_int}x**2 + {b_int}x + {c_int}")
                print(
                    "We will use the discriminant theory to find the roots of equation.")

                # Calculate discriminant again
                discriminant = (b_int**2) + -4*(a_int*c_int)
                try:
                    discriminant >= 0  # Ensure discriminant is non-negative
                    if discriminant > 0:
                        if discriminant == 0:
                            # Handle the zero discriminant case
                            if b_int < 0:
                                a_int = math.sqrt(a_int)
                                c_int = math.sqrt(c_int)
                                print(
                                    f"Your quadratic equation will look like, ({a_int} - {c_int})**2")
                            elif b_int > 0:
                                a_int = math.sqrt(a_int)
                                c_int = math.sqrt(c_int)
                                print(
                                    f"Your quadratic equation will look like, ({a_int}+{b_int})**2")
                    # Calculate roots based on the discriminant
                    x_one = (-b_int + math.sqrt(discriminant))/(2*a_int)
                    x_two = (-b_int - math.sqrt(discriminant))/(2*a_int)
                    print(
                        f"The roots of quadratic problem are {x_one} and {x_two}")
                except Exception:
                    # Handle negative discriminant exception
                    print("Discriminant can't be negative.")

    except ValueError:
        # Handle case for invalid input
        print("Correct input needed, look through comments or code to determine what variable you need.")


if __name__ == "__main__":
    main()  # Entry point of the program
