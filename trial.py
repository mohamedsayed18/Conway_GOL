import tkinter as tk
from conway import ConWay, GolGui


def make_iteration():
    gou.draw(play.pg)   # draw the playground
    play.new_screen()   # calculate the new playground
    root.after(500, make_iteration) # call the function again after 500 ms


play = ConWay()  # create a game instance
root = tk.Tk()  # create the master window
gou = GolGui(root)  # instance of my GUI
play.shapes('Beehive')  # choose the shape to start with
play.shapes('Toad')


make_iteration()
root.mainloop()
