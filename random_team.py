import os
import random
import re

clear = lambda: os.system('clear')

prev_groups = []

# Getting all the students from the student_list.txt
def get_students():
    students = []

    with open('student_list.txt') as student_list:
        read_students = student_list.read()
        split_students = read_students.split()
        for each in split_students:
            students.append(each)
    
    return students

with open("prev_group.txt") as prev_group:
    read_group = prev_group.read()
    regex = re.findall(r"\[[^\]]*\]", read_group)
    
    for each in regex:
        prev_groups.append(each)

def stringify(L: list[list[str]]) -> str:
    """Format the given list of lists of string values into the string that has those items printed as a group of values divided with ' - ' with each group starting from the new line

    Args:
        L (list[list[str]]): List of lists of grouped values

    Returns:
        str: Final string with the given values printed as groups
    """
    output = ''
    for group in L:
        output += ' - '.join(group) + '\n'

    return output


def get_random_pairs(students: list, students_per_group: int = 4) -> str:
    """Divide the given list of students into groups where each group contains the given number of students. All extra students will be added to the last group. 

    Args:
        students (list): List of students
        students_per_group (int, optional): Number of students per group. Defaults to 2.

    Returns:
        str: Students divided into groups
    """
    clear()

    random.shuffle(students)
    number_of_groups = len(students) // students_per_group - 1
    output = []
    group = 0

    while group <= number_of_groups:
        if group != number_of_groups:
            to_group = students[group * students_per_group:(group * students_per_group) + students_per_group]
            if str(to_group) not in prev_groups:
                output.append(to_group)
        else:
            output.append(students[group * students_per_group:])
        group += 1

    save_group(output)
    print(stringify(output))
    choice = input('Would you like to:\n1) Choose new groups\n2) Exit?\n')
    if choice == '1':
        get_random_pairs(students, 2)
    else:
        return

def save_group(save_students):
    with open('prev_group.txt', 'w') as to_save:
        groups_to_save = ''
        for each in save_students:
            groups_to_save += f'{each}'
        to_save.write(groups_to_save)

