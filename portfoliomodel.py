# -*- coding: utf-8 -*-
"""
Created on Fri Oct 20 14:47:14 2017

@author: JennieG
"""
# Import modules required for the ABM
import random
import matplotlib.pyplot

# Create variable for number of agents
num_of_agents = 10
# Create variable for number of agent's movements in foor loop
num_of_iterations = 100

# Define function to calculate distance between two agents' pairs of coordinates
def distance_between(agent0, agent1):
    return (((agent0[0] - agent1[0])**2) + ((agent0[1] - agent1[1])**2))**0.5

# Create a list for agents
agents =[]

# Create for loop for creating random starting coordinates for agents
for i in range(num_of_agents):
    agents.append([random.randint(0,100), random.randint(0,100)])

# Due to the for loop, we can now refer to each agent as agents[i]
# So the x coordinate would be agents[i][0] and y coord, agents[i][1]

# Create for loop for the movement of agent's one by one, with num_of_iterations variable
# 
for j in range(num_of_iterations):
    for i in range(num_of_agents):
        
        if random.random() < 0.5:
            agents[i][0] = (agents[i][0] + 1) % 100
        else:
            agents[i][0] = (agents[i][0] - 1) % 100
    
        if random.random() < 0.5:
            agents[i][1] = (agents[i][1] + 1) % 100
        else:
            agents[i][1] = (agents[i][1] - 1) % 100
        
print("Current agents' locations are", " ", agents)


# Work out the pythagorous distance between the two sets of x's and y's
#answer = ((agents[0][0] - agents[1][0])**2) + ((agents[0][1] - agents[1][1])**2)** 0.5
#print("The distance between the two agents is", " ", answer)



# Use matplotlib.pyplot to plot the current locations of agents
matplotlib.pyplot.ylim(0, 100)
matplotlib.pyplot.xlim(0, 100)
for i in range(num_of_agents):
    matplotlib.pyplot.scatter(agents[i][0],agents[i][1], color='pink')
matplotlib.pyplot.show()

# Create for loop to work out the distances between the agent's locations
# agent0 refers to each seperate agent, and agent1 refers to each agent's coords
# so the distance given will be between agent0 and agent1, agent1 and agent2 etc.
for agent0 in agents:
    for agent1 in agents:
        distance = distance_between(agent0, agent1)
    print("Distance between agents is", " ", distance)

