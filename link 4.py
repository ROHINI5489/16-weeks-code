if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    
    # Getting the marks of the queried student
    marks = student_marks[query_name]
    
    # Calculating the average of the marks
    average_marks = sum(marks) / len(marks)
    
    # Printing the average marks to two decimal places
    print("{:.2f}".format(average_marks))
