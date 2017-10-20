# -*- coding: utf-8 -*-
"""
Created on Fri Oct 20 14:47:14 2017

@author: JennieG
"""
# Import modules required for the ABM
import random
import operator
import matplotlib.pyplot

# Create a list for agents
agents =[]

# Use the agents list to create random starting locations of agent using random integers
# in order to remove x and y variables for cleaner code
agents.append([random.randint(0,100), random.randint(0,100)])

# The first dimenstion within the list refers to each agent
# The second dimension within the list; 0 is the x coord, 1 is the y coord

# Print the starting coordinates of the first(and currently the only) agent
print("Agent 0's starting coordinates are", " ", agents[0])

# Step 1 of agent 0's movement
# Change x coordinate based on random numbers using if else statement
if random.random() < 0.5:
    agents[0][0] += 1
else:
    agents[0][0] -= 1

# Change y coordinate based on random numbers using if else statement
if random.random() < 0.5:
    agents[0][1] += 1
else:
    agents[0][1] -= 1

# Print to check code for agent's movement is working
print("Agent 0's location after step 1 is", " ", agents[0])    

# Step 2 of agent 0's movement
if random.random() < 0.5:
    agents[0][0] += 1
else:
    agents[0][0] -= 1
    
if random.random() < 0.5:
    agents[0][1] += 1
# else:
    agents[0][1] -= 1    
    
# Print to check code for agent's movement is working
print("Agent 0's location after step 2 is", " ", agents[0])


# Create a second agent by appending random integers to agents list
agents.append([random.randint(0,100), random.randint(0,100)])

# Print the starting coordinates of the second agent, agent 1
print("Agent 1's starting coordinates are", " ", agents[1])

# Move the second agent randomly using if else statement
if random.random() < 0.5:
    agents[1][0] += 1
else:
    agents[1][0] -= 1

if random.random() < 0.5:
    agents[1][1] += 1
else:
    agents[1][1] -= 1
    
print("Agent 1's location after step 1 is", " ", agents[1])

if random.random() < 0.5:
    agents[1][0] += 1
else:
    agents[1][0] -= 1

if random.random() < 0.5:
    agents[1][1] += 1
else:
    agents[1][1] -= 1
    
print("Agent 1's location after step 2 is", " ", agents[1])

# Work out the pythagorous distance between the two sets of x's and y's
answer = ((agents[0][0] - agents[1][0])**2) + ((agents[0][1] - agents[1][1])**2)** 0.5
print("The distance between the two agents is", " ", answer)


# Conduct some analysis on the agent's coordinates 
print(max(agents))
# This will only take into consideration the y coordinate if all of the x
# coordinates are the same. So this will thereforeprint the set of coords 
# with the maximum number in it

# However, the .itemgettier variable from the operator package will take into
# account the y variable due to grabbbing it [1] from the agents list
# so this will give the coords with both the maximum x [0] and y[1] number

print(max(agents, key=operator.itemgetter(1)))

# Use matplotlib.pyplot to plot the current locations of agent 0 and agent 1
matplotlib.pyplot.ylim(0, 100)
matplotlib.pyplot.xlim(0, 100)
matplotlib.pyplot.scatter(agents[0][1],agents[0][0], color='pink')
matplotlib.pyplot.scatter(agents[1][1],agents[1][0], color='purple')
matplotlib.pyplot.show()

