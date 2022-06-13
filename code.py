#!/usr/bin/env python3

# Created by Noah McCaskill
# Created June 2022
# This program calculates the volume of a
# triangular prism given the two bases and the height.


def main():
    # this function calculates the volume of a triangular prism

    # input
    base = float(input("Enter the base of the Triangular prism (mm): "))
    length = float(input("Enter the length of the Triangular prism (mm): "))
    height = float(input("Enter the height of the Triangular prism (mm): "))

    # process
    volume = 0.5 * base * height * length

    # output
    print("\nThe volume will be {0:.0f} mm³.".format(volume))
    print("\nDone.")


if __name__ == "__main__":
    main()
