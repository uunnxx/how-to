import matplotlib.pyplot as pyplot


labels = ('Python', 'Ruby', 'Julia', 'Java')
sizes = [45, 30, 15, 10]

pyplot.pie(sizes,
           labels=labels,
           autopct='%1.f%%',
           counterclock=False,
           startangle=90)

pyplot.show()
