# Conway_GOL
[Conway’s Game of Life](https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life)<br/>
![](https://github.com/mohamedsayed18/Conway_GOL/blob/master/GOL.gif)<br/>
Project using python tkinter and numpy
the main module conway contain two classes<br/>
ConWay: which handles calculations<br/>
GolGui: which handles GUI
#### How to use it 
import the module and the tkinter
```python
import tkinter as tk
from conway import ConWay, GolGui
```
make instances
```python
play = ConWay()  # create a game instance
root = tk.Tk()  # create the master window
gou = GolGui(root)  # instance of my GUI
```
choose initial shapes to display
```python
play.shapes('Beehive')  # choose the shape to start with
play.shapes('Toad')
```
then run the main_iteration function in (trial.py)
```python
make_iteration()
root.mainloop()
```
in trial.py you can find example how to use this module <br/>
#### Important methods:
* ConWay.shape(shape) <br/>take the shape you want to display Blinker, Toad, Glider or Beehive

* ConWay.new_screen() <br/>Update the playground
* GolGui.draw(playground)<br/>Draw the given numpy array

#### Contribution & future work
any one is welcomed to work on this code you work on any new feature or improve existing ones.<br/>
Some ideas:
* Make the user choose the initial positions by mouse
