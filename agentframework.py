# -*- coding: utf-8 -*-
"""
Created on Sat Oct 21 14:34:27 2017

@author: JennieG
"""

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
# Create random integers for x and y coordinates of agents within the full extent 
# of the environment (300x300 grid)
        self.x = random.randint(0,300)
        self.y = random.randint(0,300)
# Set the store (the sheep's(agents') stomach), as zero (empty stomach)
        self.store = 0
# Set agents as agents list
        self.agents = agents
    
        
# Define 'move' for the random movement of agents within the 300x300 neighbourhood        
    def move(self):
# Create if statement for movement using random agent's locations
# change value of x coordinate within the extent of the environment (300x300grid)          
        if random.random() < 0.5:
            self.x = (self.x + 1) % 300
        else:
            self.x = (self.x - 1) % 300
# Create if statement for movement using random agent's locations
# change value of y coordinate within the extent of the environment (300x300grid)      
        if random.random() < 0.5:
            self.y = (self.y + 1) % 300
        else:
            self.y = (self.y - 1) % 300
            
            
# Define 'eat' for the sheep to graze on the environment            
    def eat(self):
# Create if statement to decide whether the sheep eats or not    
        if self.environment[self.y][self.x] > 10:
            self.environment[self.y][self.x] -= 10
# When sheep eats, increase store by value of 10            
            self.store += 30
# Else, keep store as store            
        else:
            self.store = self.store
# Create if statement to make the sheep sick (empty their stomach(store))
# if they have eaten more than 100 of the environment        
        if self.store <= 100:
            self.store = 0
            
            
# Define 'distance_between' to calculate the distance between each agent    
    def distance_between(self, agent1):
        return (((self.x - agent1.x)**2) + ((self.y - agent1.y)**2))**0.5
        
        
# Define 'share_with_neighbours' for deciding whether the sheep share the 
# environment for grazing within the neighbourhood       
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
                agent.store = average 
                
                agent.getstore()
                agent.setstore(average)
                # Print (agent) is sharing distanace 
                print("Agent is sharing "+ str(distance) + " " + str(average))
            
        

        
            
