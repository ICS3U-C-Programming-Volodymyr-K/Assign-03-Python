#!/usr/bin/env python3
# Created By: Volodymyr Kryzhanovskyi
# Date: 03 27, 2025
# This program  solves quadratic equations and converts into vertex form.
import math  # Importing the math library for mathematical operations


def main():
    #welcomes user
    print("Welcome user, today we will calculate quadratic problems and other problems associated with them.")
    # Taking input for the variables of the quadratic equation
    a_str = input("Enter first variable in formula.")
    b_str = input("Enter second variable in formula.")
    c_str = input("Enter third variable for formula.")
    try:
        # Attempting to convert input strings to floats
        a_int = float(a_str)
        b_int = float(b_str)
        c_int = float(c_str)
        # Asking user if they want to calculate the parabola using vertex formula
        question_1 = input(
            "Do you want to calculate the parabola in vertex formula? Types yes if you want and no if you don't want."
        )
        if question_1.lower() == "yes":
            # Print the original quadratic formula
            print(f"Your formula looks like, {a_int}x**2 + {b_int}x + {c_int}")
             # Calculate vertex x-coordinate
            e_int = b_int / a_int 
            # Calculate half of th coefficient for vertex form
            d_int = (e_int / 2) ** (2)
            d_int = round(d_int, 2)
            if b_int < 0:
                c_int = a_int * -d_int + c_int  # Adjust constant if b is negative
                print(
                    f"Your formula looks like {a_int} (x + {math.sqrt(d_int)})**2 + {c_int}"
                )
            elif b_int > 0:
                c_int = a_int * -e_int + c_int  # Adjust constant if b is positive
            print(
                f"Your formula in vertex looks like {a_int}(x - {math.sqrt(d_int)})**2 {c_int}"
            )
        elif question_1.lower() == "no":
            # Asking if the quadratic has a power
            question_2 = input(
                "Is your quadratic equation in power of something? If it is, type yes, if it is not then type no"
            )
            if question_2.lower() == "yes":
                # Taking input for the power of the quadratic equation
                power = input("Enter to what power will your quadratic equation be.")
                try:
                    power = float(power)  # Convert power input to float and checks if it is convertable
                    x_power = 2 ** (power)  # Calculate resulting power
                    print(
                        f"The formula will look like,{a_int**(power)}x**{x_power} + {b_int**(power)}x**{power} + {c_int**(power)}"
                    )
                    # Simplifying the coefficients based on the given power
                    a_int = a_int ** (1 / power)
                    b_int = b_int ** (1 / power)
                    c_int = c_int ** (1 / power)
                    print(
                        f"The simplified formula will look like {power}√ over each number {a_int}x**2 + {b_int}x + {c_int}"
                    )
                    print(
                        "We will use the discriminant theory to find the roots of equation."
                    )
                    discriminant = b_int**2 -(4 * a_int * c_int)  # Calculate the discriminant
                    try:
                        discriminant >= 0.0  # Ensure discriminant is non-negative
                    # Handle the zero discriminant case
                        if discriminant == 0.0:
                            if b_int < 0.0:
                                a_int = math.sqrt(a_int)
                                c_int = math.sqrt(c_int)
                                a_int = round(a_int, 2)
                                c_int = round(c_int, 2)
                                print(
                                f"Your quadratic equation will look like, ({a_int}x - {c_int})**2"
                                )
                            elif b_int > 0.0:
                                a_int = math.sqrt(a_int)
                                c_int = math.sqrt(c_int)
                                a_int = round(a_int, 2)
                                c_int = round(c_int, 2)
                                print(
                                f"Your quadratic equation will look like, ({a_int}x + {c_int})**2"
                            )
                        # Calculate roots based on the discriminant
                        elif discriminant > 0.0:
                                    x_one = (-b_int +
                                     math.sqrt(discriminant)) / (2 * a_int)
                                    x_two = (-b_int -
                                     math.sqrt(discriminant)) / (2 * a_int)
                                    x_one = round(x_one, 2)
                                    x_two = round(x_two, 2)
                                    print(
                                    f"The roots of quadratic problem are {x_one} and {x_two}")
                    except Exception:
                        # Handle negative discriminant exception
                        print("Discriminant can't be negative.")
                except ValueError:
                    print("Enter the float.")  # Handle invalid float input
            elif question_2.lower() == "no":
                # Printing the standard form of the quadratic equation
                print(f"Your formula looks like, {a_int}x**2 + {b_int}x + {c_int}")
                print(
                    "We will use the discriminant theory to find the roots of equation."
                )
                # Calculate discriminant again
                discriminant = (b_int**2) + -(4 * a_int * c_int)
                try:
                    discriminant >= 0.0  # Ensure discriminant is non-negative
                    # Handle the zero discriminant case
                    if discriminant == 0.0:
                                # Calculate roots based on the discriminant
                                if discriminant > 0.0:
                                    x_one = (-b_int +
                                         math.sqrt(discriminant)) / (2 * a_int)
                                    x_two = (-b_int -
                                         math.sqrt(discriminant)) / (2 * a_int)
                                    x_one = round(x_one, 2)
                                    x_two = round(x_two, 2)
                                    print(
                                    f"The roots of quadratic problem are {x_one} and {x_two}")
                    if b_int < 0.0:
                            a_int = math.sqrt(a_int)
                            c_int = math.sqrt(c_int)
                            a_int = round(a_int, 2)
                            c_int = round(c_int, 2)
                            print(
                            f"Your quadratic equation will look like, ({a_int}x - {c_int})**2"
                            )
                    elif b_int > 0:
                            a_int = math.sqrt(a_int)
                            c_int = math.sqrt(c_int)
                            a_int = round(a_int, 2)
                            c_int = round(c_int, 2)
                            print(
                            f"Your quadratic equation will look like, ({a_int}x+{b_int})**2"
                            )
                except Exception:
                    # Handle negative discriminant exception
                    print("Discriminant can't be negative.")
    except ValueError:
        # Handle case for invalid input
        print(
            "Correct input needed, look through code to determine what variable you need."
        )
if __name__ == "__main__":
    main()

# cites https://www.sololearn.com/en/Discuss/3288381/how-to-round-to-2-decimal-places-in-python
