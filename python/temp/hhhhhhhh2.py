class SemesterGrades:
    def __init__(self):
        self.num_subjects = 0
        self.grades_sum = 0

    def run(self):
        self.num_subjects = int(input("Введите количество предметов: "))
        for i in range(self.num_subjects):
            while True:
                try:
                    grade = int(input(f"Введите оценку за предмет {i+1}: "))
                    if grade < 0 or grade > 10:
                        raise ValueError
                    break
                except ValueError:
                    print("Ошибка! Введите корректное значение (число от 0 до 10)")

            self.grades_sum += grade

        average_grade = self.grades_sum / self.num_subjects
        print(f"Средняя оценка за семестр: {average_grade:.2f}")


semester = SemesterGrades()
semester.run()
