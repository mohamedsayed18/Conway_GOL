"""Conway game of life there are two classes ConWay, GolGui"""
import numpy as np
import tkinter as tk


class ConWay:
    """"""
    def __init__(self):
        """Create the play ground"""
        self.pg = np.zeros((20, 20))  # size of the playground
        self.new_pg = np.zeros((20, 20))

    def count_neighbours(self, row, col):
        """Returns number of living neighbours for a given cell"""
        lives = 0
        for i in range(row-1, row+2):
            for j in range(col-1, col+2):
                if i in range(self.pg.shape[0]) and j in range(self.pg.shape[1]) and (i != row or j != col):
                    lives += self.pg[i][j]
        return lives

    def new_screen(self):
        """Update the playground"""
        for i in range(self.pg.shape[0]):   # loop through rows
            for j in range(self.pg.shape[1]):   # loop through cols
                population = self.count_neighbours(i, j)  # population of neighbours
                # check if cell is alive or dead
                if self.pg[i][j]:    # alive
                    if population == 2 or population == 3:
                        self.new_pg[i][j] = 1
                else:   # dead
                    if population == 3:
                        self.new_pg[i][j] = 1

        self.pg = self.new_pg   # Assign the new playground to old one
        self.new_pg = np.zeros((20, 20))    # clear the playground

    def shapes(self, shape):
        """Generate the given shape Blinker,Toad,Glider or Beehive"""
        if shape == 'Blinker':
            # Blinker
            self.pg[1, 1] = 1
            self.pg[1, 2] = 1
            self.pg[1, 3] = 1
        elif shape == 'Toad':
            # Toad
            self.pg[1, 2] = 1
            self.pg[1, 3] = 1
            self.pg[1, 4] = 1

            self.pg[2, 1] = 1
            self.pg[2, 2] = 1
            self.pg[2, 3] = 1
        elif shape == 'Glider':
            # Glider
            self.pg[1, 1] = 1
            self.pg[2, 2] = 1
            self.pg[2, 3] = 1
            self.pg[3, 1] = 1
            self.pg[3, 2] = 1
        elif shape == 'Beehive':
            self.pg[13, 5] = 1
            self.pg[13, 6] = 1
            self.pg[14, 4] = 1
            self.pg[14, 7] = 1
            self.pg[15, 5] = 1
            self.pg[15, 6] = 1


class GolGui:
    """GUI of game draw the grid and the shapes"""
    def __init__(self, master):
        self.master = master  # create the master window
        master.title("Game of life")

        # canvas
        self.c = tk.Canvas(master, height=1000, width=1000, bg='white')  # create a canvas object
        self.c.pack(fill=tk.BOTH, expand=True)  # chose some options related to canvas (widget)
        self.c.bind('<Configure>', self.create_grid)

    def create_grid(self, event=None):
        """Draw the grid"""
        w = self.c.winfo_width()  # Get current width of canvas
        h = self.c.winfo_height()  # Get current height of canvas

        for i in range(h):
            self.c.create_line([(i * 30, 0), (i * 30, h)], tag='grid_line')

        for i in range(w):
            self.c.create_line([(0, i * 30), (w, i * 30)], tag='grid_line')

    def color_rec(self, col, row):
        """Draw one rectangle at row, col"""
        start = (row * 30, col * 30)
        end = (row * 30 + 30, col * 30 + 30)
        self.c.create_rectangle([start, end], fill="black", outline="red", tag='rec')

    def draw(self, a):
        """Draw the new playground"""
        self.c.delete("rec")
        # loop through the play ground and draw the rectangles
        for ix, iy in np.ndindex(a.shape):
            if a[ix, iy] == 1:
                self.color_rec(ix, iy)
