"""Game of life, GUI"""
import tkinter as tk
import numpy as np

class GolGui:
    def __init__(self, master):
        self.master = master  # create the master window
        master.title("simple GUI")

        # canvas
        self.c = tk.Canvas(master, height=1000, width=1000, bg='white')  # create a canvas object
        self.c.pack(fill=tk.BOTH, expand=True)  # chose some options related to canvas (widget)
        self.c.bind('<Configure>', self.create_grid)

    def create_grid(self,event=None):
        """draw the grid 9*9"""
        w = self.c.winfo_width()  # Get current width of canvas
        h = self.c.winfo_height()  # Get current height of canvas
        #self.c.delete('grid_line')  # Will only remove the grid_line

        for i in range(9):
            self.c.create_line([(i * 30, 0), (i * 30, h)], tag='grid_line')

        for i in range(9):
            self.c.create_line([(0, i * 30), (w, i * 30)], tag='grid_line')

    def color_rec(self, col, row ):
        start = (row * 30, col * 30)
        end = (row * 30 + 30, col * 30 + 30)
        self.c.create_rectangle([start, end], fill="black", outline="red")

    def draw(self, a):
        self.c.delete("all")
        self.create_grid()
        for ix, iy in np.ndindex(a.shape):
            if a[ix,iy] == 1:
                self.color_rec(ix,iy)
                print("found @")

if __name__ == "__main__":
    pg = np.zeros((9, 9))
    pg[0,0] = 1
    pg[1,1] = 1
    pg[3,5] = 1
    root = tk.Tk()
    gou = GolGui(root)
    root.mainloop()
