#!/usr/bin/env python3

# Created by: Jacob Bonner
# Created on: November 2019
# This program converts Celcius to Farenheit


def conversion():
    # This program converts Celcius to Farenheit

    # Input
    tc = int(input("Enter a temperature in Celcius here: "))

    # Process
    tf = (9/5)*tc+32

    # Output
    print("{0}°C is {1}° in Farenheit".format(tc, tf))


def main():
    # This function calls other functions

    # Function calls
    conversion()


if __name__ == "__main__":
    main()
