import tkinter as tk
import time

from conway import ConWay
from GOLGUI import GolGui

play = ConWay() #create a game instance
root = tk.Tk()  #create the master window
gou = GolGui(root)  #instance of my GUI

#Blinker
"""
play.pg[1,1]=1
play.pg[1,2]=1
play.pg[1,3]=1
"""

#Toad
"""
play.pg[1,2]=1
play.pg[1,3]=1
play.pg[1,4]=1

play.pg[2,1]=1
play.pg[2,2]=1
play.pg[2,3]=1
"""
#glider
play.pg[1,1]=1
play.pg[2,2]=1
play.pg[2,3]=1
play.pg[3,1]=1
play.pg[3,2]=1

def make_iteration():
    gou.draw(play.pg)
    play.new_screen()
    print("hello")
    root.after(500, make_iteration)

make_iteration()
root.mainloop()
