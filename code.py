#!/usr/bin/env python3

# Created by Noah McCaskill
# Created June 2022
# This program calculates the area of a
# trapezoid given the two bases and the height.


def main():
    # this function calculates the area of a trapezoid

    # input
    bottom_side = float(input("Enter the Bottom Side of the Trapezoid (mm): "))
    top_side = float(input("Enter the Top Side of the Trapezoid (mm): "))
    height = float(input("Enter the Bottom Side of the Trapezoid (mm): "))

    # process
    area = ((bottom_side + top_side) / 2) * height

    # output
    print("\nThe area will be {0:.0f} mm².".format(area))
    print("\nDone.")


if __name__ == "__main__":
    main()
    
