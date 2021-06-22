import os
import random
import time

# Set to True to Testing
do_print = False

# Clear the screen
os.system('clear')

# Students who have already gone. Manual at this point.
completed_students = [
    'Matt',
    'Kassie', 

]

# Students who have not yet gone.
students = [
    'Glen',
    'Daniel',
    'Garfield',
    'Michael H',
    'Kevin',
    'Marie',
    'Tony',
    'Michael R',
    'Lauren',
    'Prabin',
    'Davee',
    'Wondwosen',
    'Anthony W',
    ]

half = []
quarter = []

for i in range(0, len(students) // 2 ):
    student_entered = False
    while not student_entered:
        random_student = random.choice(students)
        if do_print: print(random_student)
        if random_student in half:
            if do_print: print('Student Already there.  Getting another one')
            continue
        else:
            half.append(random_student)
            student_entered = True

print(f'\n\n***** Here is who is left: {students}')
time.sleep(3)

print(f'\n\n***** Cutting Down the Choices: {half}')
time.sleep(3.5)

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
time.sleep(5)
print('\nAnd the winner is: ' + random.choice(quarter) + "\n")