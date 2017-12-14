# -*- coding: utf-8 -*-
"""
Created on Fri Oct 20 14:47:14 2017

@author: JennieG
"""
# Import modules required for the ABM
import random
import matplotlib.pyplot
import csv

# Import code required for the ABM
import agentframework

# Create list that will hold the environment data
environment = []

# Open CSV file for modelling the environment
f = open('in.txt', newline='')
reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)

for row in reader:
# A new rowlist generated each time the loop runs.
    rowlist = []		
    
    for value in row:	
        rowlist.append(value)
             
    environment.append(rowlist)
f.close()

# Set the variables as arguments for runnig the ABM via command prompt
#num_of_agents = int(sys.argv[1])
#num_of_iterations = int(sys.argv[2])
#neighbourhood = int(sys.argv[3])

# Create variables for the number of agents within the ABM, their number of movements within the
# environment, and the specified size of an agent's neighbourhood.
num_of_agents = 15
num_of_iterations = 100
neighbourhood = 35

# Create a list for agents
agents =[]

# Create for loop for creating random starting coordinates for agents, within 
# the given environment
for i in range(num_of_agents):
    agents.append(agentframework.Agent(environment, agents))

# Due to the for loop and agent framework, we can now refer to each agent as agents[i]
# Due to the Agent class, we can refer to the x coordinate as agents[i].x
# and we can refer to the y coordinate as agents[i].y


# Create for loop for the movement of agents (sheep), and their subsequent 
# eating/grazing throughout the environment. If the sheep are within close proximity
# to one another (neighbourhood), the sheep will share their store!
for j in range(num_of_iterations):
# Ramdomise the agent's iterations    
    random.shuffle(agents)
    for i in range(num_of_agents):
        agents[i].move()
        agents[i].eat()
        agents[i].sick()
        agents[i].share_with_neighbours(neighbourhood)
        agents[i].consumption()
                
        
# Create a graph to show the current location of the sheep within the environment
# displaying where the sheep have been grazing 

# Write so that any .csv environment could be added and the code will still run
# The length of the environment's first index (x coordinates)
matplotlib.pyplot.xlim(0, len(environment[0]))
# The length of the environment (y coordinates)
matplotlib.pyplot.ylim(0, len(environment))
matplotlib.pyplot.imshow(environment)
for i in range(num_of_agents):
    matplotlib.pyplot.scatter(agents[i].x,agents[i].y, color='gray')
matplotlib.pyplot.show()


## Zoom in to the agents on the map
matplotlib.pyplot.xlim(0, (agents[i].x))
matplotlib.pyplot.ylim(0, (agents[i].y))
matplotlib.pyplot.imshow(environment)
for i in range(num_of_agents):
    matplotlib.pyplot.scatter(agents[i].x,agents[i].y, color='gray')
matplotlib.pyplot.show()

# Write out the environment as a file
f2 = open('dataout.csv', 'w', newline='') 
writer = csv.writer(f2, delimiter=',')
for row in environment:		
	writer.writerow(row)		
f2.close()

# Print the class instances of agents
print(agents[i])

