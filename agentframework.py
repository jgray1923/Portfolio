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
    def __init__(self, environment):
# Set the environment as environment, the file opened in portfoliomodel.py
        self.environment = environment
# Create random integers for x and y coordinates of agents within the full extent 
# of the environment (300x300 grid)
        self.x = random.randint(0,300)
        self.y = random.randint(0,300)
# Set the store (the sheep's(agents') stomach), as zero (empty stomach)
        self.store = 0
    
# Define 'move' for the random movement of agents within the 300x300 neighbourhood        
    def move(self):
        if random.random() < 0.5:
            self.x = (self.x + 1) % 300
        else:
            self.x = (self.x - 1) % 300
    
        if random.random() < 0.5:
            self.y = (self.y + 1) % 300
        else:
            self.y = (self.y - 1) % 300
# Define 'eat' for the sheep to graze on the environment            
    def eat(self):
        if self.environment[self.y][self.x] > 10:
            self.environment[self.y][self.x] -= 10
            self.store += 30
        else:
            self.store = self.store
# Create if statement to make the sheep sick (empty their stomach(store)), if they
# have eaten more than 100 of the environment        
        if self.store <= 100:
            self.store = 0

        
            
