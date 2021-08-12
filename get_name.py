import os
import random
import time

# Set to True to Testing
do_print = False

# Clear the screen
clear = lambda: os.system('clear')

students = []

# Getting all the students from the student_list.txt
with open('student_list.txt') as student_list:
    read_students = student_list.read()
    split_students = read_students.split()
    for each in split_students:
        students.append(each)

def student_selector():
    clear()
    # Updated after the random choice
    completed_students = []

    print('Loading the previously saved students')

    # Getting the list of already called on students from saved_students.txt. If there is not a saved_students.txt a exception will print.
    try:
        with open('saved_students.txt') as chosen_already:
            students_read = chosen_already.read()
            split_students = students_read.split()
            # print(split_students)
            for each_student in split_students:
                completed_students.append(each_student)
    except:
        print('No saved_students.txt found?')

    students_left = []
    half = []
    quarter = []

    # Update the students_left list based on which students havent been called yet.
    for student in students:
        if student not in completed_students:
            students_left.append(student)
    
    # If all the students have already been called on and stored in the saved_students.txt this will show up:
    if len(students_left) == 0:
        print('All students have already gone, check saved_students.txt.\n')
        choice = input('Would you like to: \n1) Clear the saved list and run this again \n2) Exit \n')
        if choice == 'c':
            clear_chosen()
            student_selector()
        else:
            print('Exiting, thanks for using the app!')
            return

    # If there is only one student left we default to that student and give the input options.
    if len(students_left) == 1:
        print(f'\nAnd the final winner is: {students_left[0]} \n')
        completed_students.append(students_left[0])
        save_chosen(completed_students)
        print('All students have already been chosen once. \n')
        choice = input('Would you like to: \n1) Clear the saved list and run this again \n2) Exit \n')
        if choice == '1':
            clear_chosen()
            student_selector()
        else:
            print('Exiting, thanks for using the app!')
            return
    else:
        for i in range(0, len(students_left) // 2 ):
            student_entered = False
            while not student_entered:
                random_student = random.choice(students_left)
                if do_print: print(random_student)
                if random_student in half:
                    if do_print: print('Student Already there.  Getting another one')
                    continue
                else:
                    half.append(random_student)
                    student_entered = True

        print(f'\n\n***** Here is who is left: {students_left}')
        # time.sleep(3)

        print(f'\n\n***** Cutting Down the Choices: {half}')
        # time.sleep(3.5)
        if len(half) == 1:
            quarter.append(half[0])
        else:
            for i in range(0, len(half) // 2 ):
                student_entered = False
                while  not student_entered:
                    random_student = random.choice(half)
                    if do_print:  print(random_student)
                    if random_student in quarter:
                        if do_print:  print('Student Already there.  Getting another one')
                        continue
                    else:
                        quarter.append(random_student)
                        student_entered = True

        print(f'\n\n***** Down a few more: {quarter}')
        print('\n\n*****Pausing for Dramatic Effect!!!*****')
        time.sleep(2)
        chosen = random.choice(quarter)
        print(f'\nAnd the winner is: {chosen} \n')
        completed_students.append(chosen)
        print(f'Already chosen students = {completed_students}')
        # update_chosen_file(completed_students)
        save_chosen(completed_students)
        print('saved_students.txt has been updated.')

        save_or_choose = input('Would you like to: \n1) Choose a new student\n2) Clear the saved list and run this again\n3) Exit\n')
        if save_or_choose == '1':
            student_selector()
        elif save_or_choose == '2':
            student_selector()
        else:
            print('Exiting')
            
            return


## Save the list of students that have already gone

def save_chosen(save_students):
    with open('saved_students.txt', 'w') as to_save:
        students_to_save = ''
        for each in save_students:
            students_to_save += f'{each} '
        to_save.write(students_to_save)

def clear_chosen():
    with open('saved_students.txt', 'w') as chosen_already:
        already_called = ''
        chosen_already.write(already_called)
