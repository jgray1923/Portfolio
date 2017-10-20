# -*- coding: utf-8 -*-
"""
Created on Fri Oct 20 14:47:14 2017

@author: JennieG
"""
# Import modules required for the ABM
import random

# Create variables for agent's location
# Create an x coordinate
x0 = 50
# Create a y coordinate
y0 = 50

print("Agent 0's starting coordinates are", " ", x0, y0)

# Step 1 of agent 0's movement
# Change x coordinate based on random numbers
if random.random() < 0.5:
    x0 += 1
else:
    x0 -= 1

# Change y coordinate based on random numbers
if random.random() < 0.5:
    y0 += 1
else:
    y0 -= 1

# Print to check code for agent's movement is working
print("Agent 0's location after step 1 is", " ", x0,y0)    

# Step 2 of agent's movement
if random.random() < 0.5:
    x0 += 1
else:
    x0 -= 1
    
if random.random() < 0.5:
    y0 += 1
else:
    y0 -= 1    
    
# Print to check code for agent's movement is working
print("Agent 0's location after step 2 is", " ", x0, y0)

# Create a second random agent with random movement over two steps
x1 = random.randint(0,100)
y1 = random.randint(0,100)

print("Agent 1's starting coordinates are", " ", x1, y1)

if random.random() < 0.5:
    x1 += 1
else:
    x1 -= 1

if random.random() < 0.5:
    y1 += 1
else:
    y1 -= 1
    
print("Agent 1's location after step 1 is", " ", x1,y1)

if random.random() < 0.5:
    x1 += 1
else:
    x1 -= 1

if random.random() < 0.5:
    y1 += 1
else:
    y1 -= 1
    
print("Agent 1's location after step 2 is", " ", x1,y1)
    

# Work out the pythagorous distance between the two sets of x's and y's
answer = ((x0 - x1)**2) + ((y0 - y1)**2)** 0.5
print("The distance between the two agents is", " ", answer)

