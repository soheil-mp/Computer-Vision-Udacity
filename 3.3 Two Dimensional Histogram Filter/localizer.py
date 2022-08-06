import pdb
from helpers import normalize, blur
import numpy as np

def initialize_beliefs(grid):
    height = len(grid)
    width = len(grid[0])
    area = height * width
    belief_per_cell = 1.0 / area
    beliefs = []
    for i in range(height):
        row = []
        for j in range(width):
            row.append(belief_per_cell)
        beliefs.append(row)
    return beliefs

# Sense function
def sense(color, grid, beliefs, p_hit, p_miss):
    height = len(beliefs)
    width = len(beliefs[0])
    new_beliefs = [[0.0 for i in range(width)] for j in range(height)] 
    for i in range(len(beliefs)): # 0, 1, 2, 3, 4, 5, 6
        for j in range(len(beliefs[0])): # 0, 1, 2, 3
            #pdb.set_trace()
            hit = (grid[i][j] == color)
            new_beliefs[i][j] = (beliefs[i][j] * (hit * p_hit + (1-hit) * p_miss))
            
    s = np.sum(np.array(new_beliefs).flatten())

    for i in range(len(new_beliefs)):
        for j in range(len(new_beliefs[0])):
            new_beliefs[i][j] = new_beliefs[i][j] / s
            
    return new_beliefs

def move(dy, dx, beliefs, blurring):
    height = len(beliefs)
    width = len(beliefs[0])
    new_G = [[0.0 for i in range(width)] for j in range(height)]
    for i, row in enumerate(beliefs):
        for j, cell in enumerate(row):
            new_i = (i + dy ) % width
            new_j = (j + dx ) % height
            # pdb.set_trace()
            new_G[int(new_j)][int(new_i)] = cell
    return blur(new_G, blurring)