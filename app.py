import os
import time
from random_team import get_random_pairs, get_students
from get_name import student_selector

clear = lambda: os.system('clear')

def intro():
    print("Welcome to the app!\n")
    choosing = True
    choice = input("Would you like to:\n1) Select a student?\n2) Select a random pair of students?\n3) Exit app\nUse the number to make your selection.\n")
    while choice:
        # print('choice is ', choice)
        if choice == "1":
            student_selector()
            clear()
            choice = ' '
        elif choice == "2":
            students = get_students()
            group_number = input('How many students per group? \nOr press enter for 2 \n')
            while type(group_number) != int:
                if group_number == "":
                    group_number = 2
                try:
                    group_number = int(group_number)
                    # group = get_random_pairs(students, group_number)
                    # print(group)
                except ValueError:
                    print('Not an integer')
                    group_number = input('How many students per group? \nOr press enter for 2 \n')
            get_random_pairs(students, group_number)
            clear()
            choice = ' '
        elif choice == "3":
            print('Thanks for using the app!')
            # choice = False
            break
        else:
            print('Please enter a number.')
            choice = input("Would you like to:\n1) Select a student?\n2) Select a random pair of students?\n3) Exit app\nUse the number to make your selection.\n")
            clear()

if __name__ == "__main__":
    intro()


