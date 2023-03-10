import matplotlib.pyplot as pyplot


labels = ('Python', 'Ruby', 'Julia', 'Java', 'PHP')
index = (1, 2, 3, 4, 5)  # provides locations on x axis
sizes = [45, 30, 15, 10, 22]

# Set up the bark chart
pyplot.bar(index, sizes, tick_label=labels)

# Configure the layout
pyplot.ylabel('Usage')
pyplot.xlabel('Programming Languages')

# Display the chart
pyplot.show()
