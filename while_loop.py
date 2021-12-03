#!/usr/bin/env python3

# Created by: Abdul Basit
# Created on: Dec 2021
# this program is for adding loops

def main():
    # this is a function for adding while loop

    # variables
    counter = 0
    sum_num = 0

    # input
    number = input("Enter a positive integer: ")
    number = int(number)

    # process
    while counter < number:
        counter += 1
        sum_num += counter

    # output
    print(f"The sum of all positive numbers from 1 to {number} is {sum_num}.")
    print("\nDone.")


if __name__ == "__main__":
    main()