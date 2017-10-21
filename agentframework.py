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
    def __init__(self):
# Create random integers for x and y coordinates of agents within the extent 
# of the environment (100x100 grid)
        self.x = random.randint(0,100)
        self.y = random.randint(0,100)
    
# Define 'move' for the random movement of agents within the 100x100 neighbourhood        
    def move(self):
        if random.random() < 0.5:
            self.x = (self.x + 1) % 100
        else:
            self.x = (self.x - 1) % 100
    
        if random.random() < 0.5:
            self.y = (self.y + 1) % 100
        else:
            self.y = (self.y - 1) % 100
            
