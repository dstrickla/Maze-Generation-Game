"""
This class represents the maze generation algorithms used to randomly construct 
a maze to be rendered as a playable game level. This class was constructed to 
allow for easy integration in other projects requiring maze generation. 
"""

import numpy as np
from random import shuffle

class Direction():
    """Enum direction values"""
    UP = 0
    RIGHT = 1
    DOWN = 2
    LEFT = 3

class MazeChar():
    """Maze character legend"""
    WALL = '#'
    PATH = '_'

class MazeGenerator():

    def __init__(self, dim, left_limit=1):
        """Maze Generator constructor"""
        self.dim = dim 
        self.left_limit = left_limit
        self.maze = np.empty(shape=(dim, dim), dtype=str)

    #==========================================================================#

    def rec_depth_first(self, start_row=1, start_col=1):
        """ 
        Returns a randomly generated maze using a recursive backtpropagation 
        implementation of Randomized depth-first search. Default starting path 
        is in the top left corner of the maze. 
        """
        self.maze.fill(MazeChar.WALL)
        self.df_recurse(start_row, start_col)
    
    def df_recurse(self, row, col):
        """Recursive step of Recursive Randomized Depth-first search"""
        self.maze[row][col] = MazeChar.PATH # Mark cell as visited
        directions = [Direction.UP, Direction.RIGHT, Direction.DOWN, Direction.LEFT]
        shuffle(directions)

        while directions: 
            curr_direction = directions.pop()

            match curr_direction:
                case Direction.UP:
                    if self.is_valid_up(row, col): self.df_recurse(row-1, col)
                case Direction.RIGHT:
                    if self.is_valid_right(row, col): self.df_recurse(row, col+1)
                case Direction.DOWN:
                    if self.is_valid_down(row, col): self.df_recurse(row+1, col)
                case Direction.LEFT:
                    if self.is_valid_left(row, col): self.df_recurse(row, col-1)                                            
    
    def is_valid_up(self, row, col):
        """Determines if up can be explored in depth first search"""
        if self.left_limit < row: 
            risk_points = [self.maze[row-1][col], self.maze[row-2][col],
                            self.maze[row-1][col-1], self.maze[row-1][col+1]]
            if all(r_point != MazeChar.PATH for r_point in risk_points):
                return True 
        return False

    def is_valid_right(self, row, col):
        """Determines if right can be explored in depth first search"""
        if col < self.dim-2: 
            risk_points = [self.maze[row][col+1], self.maze[row][col+2],
                            self.maze[row-1][col+1], self.maze[row+1][col+1]]
            if all(r_point != MazeChar.PATH for r_point in risk_points):
                return True 
        return False

    def is_valid_down(self, row, col):
        """Determines if down can be explored in depth first search"""
        if row < self.dim-2: 
            risk_points = [self.maze[row+1][col], self.maze[row+2][col],
                            self.maze[row+1][col-1], self.maze[row+1][col+1]]
            if all(r_point != MazeChar.PATH for r_point in risk_points):
                return True 
        return False
    
    def is_valid_left(self, row, col):
        """Determines if left can be explored in depth first search"""
        if self.left_limit < col: 
            risk_points = [self.maze[row][col-1], self.maze[row][col-2],
                            self.maze[row-1][col-1], self.maze[row+1][col-1]]
            if all(r_point != MazeChar.PATH for r_point in risk_points):
                return True 
        return False
    
    #==========================================================================#


    
