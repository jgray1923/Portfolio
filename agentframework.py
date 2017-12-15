# -*- coding: utf-8 -*-
"""
Created on Sat Oct 21 14:34:27 2017

@author: JennieG
"""
# Copyright 2017 Jennie Gray
# This file is part of portfoliomodel.py.
#
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


# Import random module for the creation of the random movement of agents
import random

# Create a class for the agents
class Agent():
    
# Use __init__ to construct a self parameter for Agent, to enable us to refer to the
# instance of the class, eg the agent's x and y coordinates

# Define 'self'
    def __init__(self, environment, agents):
# Set the environment as environment, the file opened in portfoliomodel.py
        self.environment = environment
# Create random integers for x and y coordinates of agents within the extent 
# of the environment 
        self.x = random.randint(0,len(environment[0]))
        self.y = random.randint(0,len(environment))
# Set the store (the sheep's(agents') stomach), as zero (empty stomach)
        self.store = 0
# Set agents as agents list
        self.agents = agents
    
        
# Define 'move' for the random movement of agents within the environment        
    def move(self):
# Create if statement for movement using random agent's locations
# change value of x coordinate within the extent of the environment          
        if random.random() < 0.5:
            self.x = (self.x + 1) % len(self.environment[0])
        else:
            self.x = (self.x - 1) % len(self.environment[0])
# Create if statement for movement using random agent's locations
# change value of y coordinate within the extent of the environment      
        if random.random() < 0.5:
            self.y = (self.y + 1) % len(self.environment)
        else:
            self.y = (self.y - 1) % len(self.environment)
            
            
# Define 'eat' for the sheep to graze on the environment            
    def eat(self):
# Create if statement to decide whether the sheep eats or not    
        if self.environment[self.y][self.x] > 10:
            self.environment[self.y][self.x] -= 10
# When sheep eats, increase store by value of 10            
            self.store += 30
# Elif statement; if the environment is greater than 0 (and lower than 10):
        elif self.environment[self.y][self.x] >0:
# Make the sheep eat the remainder of the environment (but not any more!)
            self.store += self.environment[self.y][self.x]
# Then set the environment as zero, all the grass for grazing has now gone.
            self.environment[self.y][self.x] = 0            
# Else, keep store as store            
        else:
            self.store = self.store
            
            
# Make the sheep sick if they eat too much            
    def sick(self):
# If the store is more than 500 (greedy sheep!)
        if self.store > 500:
# Make the sheep sick up some of their food
            self.store -= 50
# Therefore increase the environment by the amount of sick up
            self.environment[self.y][self.x] += 50           
            
            
            
# Define 'distance_between' to calculate the distance between each agent    
    def distance_between(self, agent1):
        return (((self.x - agent1.x)**2) + ((self.y - agent1.y)**2))**0.5
        
        
# Define 'share_with_neighbours' for deciding whether the sheep share their store(food)        
    def share_with_neighbours(self, neighbourhood):
# Set neighbourhood as neighbourhood labelled in portfoliomodel.py       
        self.neighbourhood = neighbourhood
# Create for loop        
        for agent in self.agents:
            distance = self.distance_between(agent)
 # Create if loop: if distance is less than or equal to neighbourhood           
            if distance <= self.neighbourhood:
 # then set average as the store plus agent.store/2
                average = (self.store + agent.store)/2 
 # set self.store as average
                self.store = average
 # set agent.store as average
                agent.store = average# If distance is greater than 0
                if distance > 0:
 # Print found within distance, and the average store of agents
                    print("Found agent within " + str(distance) + ". " + "Average store = " + str(average))
 # Else pass (if the distance is the same (ie agent passing against itself, it will not print out)
                else:
                    pass
                    
                
# Define _str_ so that when 'agents' is printed, the x and y coordinates, and
# store are displayed
    def __str__(self):
        for agent in self.agents:
 # Return the values of the coordinates and stores. {} refers to the arguments, which are passed in .format()              
            return("X coordinate= {0}, Y coordinate= {1}, Store= {2}".format(self.x, self.y, self.store))
        
        
# Define consumption as a method as opposed to a variable within the ABM.            
    def consumption(self):
 # Set consumption as zero       
        consumption = 0
        
        for agent in self.agents:           
            distance = self.distance_between(agent)
# If distance is less than or equal to neighbourhood            
            if distance <= self.neighbourhood:
# Consumption = 0 plus the store of the agents                
                consumption = (0 + (self.store + agent.store))
 # If consumption is greater than 0               
                if consumption > 0:
# Print consumption                    
                    print(" Consumption is currently: " + str(consumption))
# Else pass - do not print consumption                    
                else:
                    pass
# Else consumption = zero                 
            else: 
                consumption = 0
                
        
            
