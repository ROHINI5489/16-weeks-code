if __name__ == '__main__':
    students = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])

    # Sorting the list of students based on grades
    students.sort(key=lambda x: x[1])

    # Finding the second lowest grade
    second_lowest_grade = sorted(set(score for name, score in students))[1]
    # Getting the names of students with the second lowest grade
    second_lowest_students = [name for name, score in students if score == second_lowest_grade]

    # Sorting the names alphabetically
    second_lowest_students.sort()

    # Printing the names of students with the second lowest grade
    for name in second_lowest_students:
        print(name)

