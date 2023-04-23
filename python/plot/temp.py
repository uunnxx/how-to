import matplotlib.pyplot as pyplot


# Set up the data

x = list(range(7))
y = [0, 2, 6, 14, 30, 43, 75]

# Set teh axes headings
pyplot.ylabel('Speed', fontsize=12)
pyplot.xlabel('Time', fontsize=12)

# Set the title
pyplot.title('Speed v Time')

# Plot and display the graph
# Using blue circles for markers ('bo')
# and a solid line ('-')
pyplot.plot(x, y, 'bo-')
pyplot.show()
