# -*- coding: utf-8 -*-
"""
Created on Fri Oct 20 14:47:14 2017

@author: JennieG
"""
# copyright 2017 Jennie Gray
# This file is part of portfoliomodel.py.

#    portfoliomodel.py is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    portfoliomodel.py is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with portfoliomodel.py.  If not, see <http://www.gnu.org/licenses/>.

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
num_of_agents = 20
num_of_iterations = 150
neighbourhood = 30

# Create a list for agents
agents =[]


# Create for loop for creating random starting coordinates for agents, within 
# the given environment
for i in range(num_of_agents):
    agents.append(agentframework.Agent(environment,agents))
    

# Due to the for loop and agent framework, we can now refer to each agent as agents[i]
# Due to the Agent class, we can refer to the x coordinate as agents[i].x
# and we can refer to the y coordinate as agents[i].y


# Write so that any .csv environment could be added and the code will still run
# The length of the environment's first index (x coordinates)
matplotlib.pyplot.xlim(0, len(environment[0]))
# The length of the environment (y coordinates)
matplotlib.pyplot.ylim(0, len(environment))
matplotlib.pyplot.imshow(environment)
matplotlib.pyplot.show()

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
        #agents[i].consumption()
                


# Create a graph to show the current location of the sheep within the environment
# displaying where the sheep have been grazing 

# Write so that any .csv environment could be added and the code will still run
# The length of the environment's first index (x coordinates)
matplotlib.pyplot.xlim(0, len(environment[0]))
# The length of the environment (y coordinates)
matplotlib.pyplot.ylim(0, len(environment))
matplotlib.pyplot.imshow(environment)
matplotlib.pyplot.show()

# Write so that any .csv environment could be added and the code will still run
# The length of the environment's first index (x coordinates)
matplotlib.pyplot.xlim(0, len(environment[0]))
# The length of the environment (y coordinates)
matplotlib.pyplot.ylim(0, len(environment))
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

