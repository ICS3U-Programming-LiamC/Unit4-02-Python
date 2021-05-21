#!/usr/bin/env python3

# Created by: Liam Csiffary
# Created on: May 21, 2021
# This program calculates the factorial of the users number


# main function
def main():

    # vars
    user_num = input("what is the number: ")

    # make sure the users num can be an integer
    try:
        user_num = int(user_num)

        if (user_num >= 0):
            if (user_num != 0):

                # resetting vars
                factorial_num = 1
                counter = 0

                while True:
                    counter = counter + 1
                    factorial_num = factorial_num * counter

                    if (counter >= user_num):
                        print("{:,} factorial is {:,}".format
                              (user_num, factorial_num))
                        break
            else:
                print("0 factorial is 1")
        else:
            print("{} is not positive".format(user_num))

    except ValueError:
        print("Not valid input")


if __name__ == "__main__":
    main()
