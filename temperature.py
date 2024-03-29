#!/usr/bin/env python3

# Created by: Jacob Bonner
# Created on: November 2019
# This program converts Celcius to Farenheit


def conversion():
    # This program converts Celcius to Farenheit

    # Input
    temperature_celcius = int(input("Enter a temperature in Celcius here: "))

    # Process
    temperature_farenheit = (9/5)*temperature_celcius+32

    # Output
    print("{0}°C is {1}° in Farenheit".format
          (temperature_celcius, temperature_farenheit))


def main():
    # This function calls other functions

    # Function calls
    conversion()


if __name__ == "__main__":
    main()
