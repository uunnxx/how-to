from collections import deque


class CalculateAveragePoint:
    subjects = deque()
    subject_count = 0
    points = 0

    @classmethod
    def ask_for_subjects(cls):
        count = int(input('Count of the subjects: '))
        cls.subject_count = count
        for i in range(count):
            subject = input(f'Subject {i+1}: ')
            cls.subjects.append(subject.title())


    @classmethod
    def ask_for_points(cls):
        while cls.subjects:
            subject = cls.subjects.popleft()
            try:
                current = int(input(f'Point for {subject}: '))
                if cls.in_range(current, 0, 10):
                    cls.points += current
                else:
                    raise ValueError
            except ValueError:
                cls.subjects.append(subject)
                print('Point from 0 to 10')


    @classmethod
    def calculate_average(cls):
        cls.ask_for_subjects()
        cls.ask_for_points()
        return f"{(cls.points / cls.subject_count):.2f}"


    @staticmethod
    def in_range(target, start, end):
        return start <= target <= end


print(CalculateAveragePoint.calculate_average())
