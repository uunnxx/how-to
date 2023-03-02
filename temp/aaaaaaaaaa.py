if __name__ == '__main__':
    students = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]

    sorted_by_score = sorted(students, key=lambda x: x[1])
    lowest = min(sorted_by_score, key=lambda x: x[1])
    min_count = sorted_by_score.count(lowest)
    temp = sorted_by_score[min_count][1]
    second_lowest = sum(student.count(temp) for student in sorted_by_score)
    sorted_by_name = sorted(sorted_by_score[min_count:second_lowest+1])

    for student in sorted_by_name:
        print(student[0])

