
from die import Die



import pygal
sides1 = input("Enter how many sides you want on the first die\n")
sides2 = input("Enter how many sides you want on the second die\n")
rolls = input("Enter how many rolls you would like to do\n")

die = Die(int(sides1))
die2 = Die(int(sides2))

results = []
for roll_num in range(int(rolls)):
    result = die.roll() + die2.roll()
    results.append(result)
    
print(results)

frequencies = []
max_result = die.num_sides + die2.num_sides
for value in range(2, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)
    
print(frequencies)


hist = pygal.Bar()

hist.title = 'Results of rolling a D'+str(die.num_sides)+' and a D'+str(die2.num_sides)+ " "+ str(rolls)+' times'
x_stuff = []
for value in range(2,max_result+1):
    x_stuff.append(str(value))
hist.x_labels = x_stuff
hist.x_title = 'Result'
hist.y_title = 'Frequency of Result'

hist.add('D'+str(die.num_sides)+'+D'+str(die2.num_sides), frequencies)
hist.render_to_file('die_visual.svg')
