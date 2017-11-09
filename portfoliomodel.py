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
             
        #print(value) 	
    environment.append(rowlist)
f.close()

# Generate a graph to display the environment data
#matplotlib.pyplot.imshow(environment)
#matplotlib.pyplot.show()

# Create variable for number of agents
num_of_agents = 20
# Create variable for number of agent's movements in for loop
num_of_iterations = 150
# Create variable for neighbourhood size
neighbourhood = 20

# Define function to calculate distance between two agents' pairs of coordinates
def distance_between(agent0, agent1):
    return (((agent0.x - agent0.x)**2) + ((agent1.y - agent1.y)**2))**0.5

# Create a list for agents
agents =[]

# Create for loop for creating random starting coordinates for agents, within 
# the given environment
for i in range(num_of_agents):
    agents.append(agentframework.Agent(environment, agents))

# Due to the for loop, we can now refer to each agent as agents[i]
# Due to the Agent class, we can refer to the x coordinate as agents[i].x
# and we can refer to the y coordinate as agents[i].y


# Create for loop for the movement of agents (sheep), and their subsequent 
# eating/grazing throughout the environment. If the sheep are within close proximity
# to one another (neighbourhood), the sheep will share the environment
for j in range(num_of_iterations):
#ramdomise the agents iterations   
    random.shuffle(agents)
    for i in range(num_of_agents):
        agents[i].move()
        agents[i].eat()
        agents[i].share_with_neighbours(neighbourhood)
        

## Use matplotlib.pyplot to plot the current locations of agents
#matplotlib.pyplot.ylim(0, 100)
#matplotlib.pyplot.xlim(0, 100)
#for i in range(num_of_agents):
#    matplotlib.pyplot.scatter(agents[i].x, agents[i].y, color='pink')
#matplotlib.pyplot.show()

# Create a graph to show the current location of the sheep within the environment
# displaying where the sheep have been grazing 
matplotlib.pyplot.xlim(0, 100)
matplotlib.pyplot.ylim(0, 100)
matplotlib.pyplot.imshow(environment)
for i in range(num_of_agents):
    matplotlib.pyplot.scatter(agents[i].x,agents[i].y, color='gray')
matplotlib.pyplot.show()

# Removed distance between code block, as it is now written within agentframework.py
# and so is no longer required. 

# Write out the environment as a file
f2 = open('dataout.csv', 'w', newline='') 
writer = csv.writer(f2, delimiter=',')
for row in environment:		
	writer.writerow(row)		
f2.close()

