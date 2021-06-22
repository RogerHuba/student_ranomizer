import random


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

    random.shuffle(students)
    number_of_groups = len(students) // students_per_group - 1
    output = []
    group = 0

    while group <= number_of_groups:
        if group != number_of_groups:
            output.append(
                students[group * students_per_group:(group * students_per_group) + students_per_group])
        else:
            output.append(students[group * students_per_group:])
        group += 1

    return stringify(output)


if __name__ == "__main__":
    STUDENTS = [
        # Absent students can be commented out below
        'Karlo',
        'Alexander',
        'Amber',
        'Anthony',
        'Ashley',
        'Audrena',
        'Ben',
        'Bhagirath',
        'Brandon',
        'Grace',
        'Jae',
        'Kim',
        'Logan',
        'Mason',
        'Matthew',
        'Nebiyu',
        'Nick',
        'Samuel',
        'Sean',
        'Sian'
        ]
    group_number = int(input('How many students per group? '))

    print(get_random_pairs(STUDENTS, group_number))
