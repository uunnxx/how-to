class Instructors:
    company_name = 'Bluelime'

    def __init__(self, course, duration=None):
        self.course = course
        self.duration = duration

    def printinfo(self):
        # print(f'My company name is {Instructors.company_name}')
        # print(f'My company name is {self.company_name}')
        print(f'My company name is {self.__class__.company_name}')

    def __str__(self):
        if not self.duration:
            return f'Name of the course: {self.course}'

        return (
            f'Name of the course: {self.course} '
            f'and duration of the course is {self.duration} hours'
        )


ins = Instructors('Django for Beginners', 40)

ins.printinfo()

print(ins)

