"""the conway game"""
class ConwayGame:
    def __init__(self):
        import tkinter as tk

        from conway import ConWay
        from GOLGUI import GolGui

        play = ConWay()  # create a game instance
        root = tk.Tk()  # create the master window
        gou = GolGui(root)  # instance of my GUI

    def make_iteration(self):
        gou.draw(play.pg)
        play.new_screen()
        print("hello")
        root.after(500, make_iteration)
    def shapes(self,shape,row,col):
        if shape == 'toad':
            pass
        elif shape == 'glider':
            pass
        else:
            pass


if __name__ == '__main__':
    p = ConwayGame()