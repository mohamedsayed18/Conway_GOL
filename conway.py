import numpy as np

class ConWay :
    def __init__(self):
        self.pg = np.zeros((20, 20))  # size of the playground
        self.new_pg = np.zeros((20, 20))

    def count_neighbours(self,row,col):
        lives = 0
        for i in range(row-1,row+2):
            for j in range(col-1,col+2):
                if i in range(self.pg.shape[0]) and j in range(self.pg.shape[1]) and (i != row or j != col):
                    lives += self.pg[i][j]
                    #print("alive",i,j)
        return lives

    def new_screen(self):
        for i in range(self.pg.shape[0]): # loop through rows
            for j in range(self.pg.shape[1]):   # loop through cols
                population = self.count_neighbours(i, j)  # population of neighbours
                # check if cell is alive or dead
                if self.pg[i][j]:    # alive
                    if population == 2 or population == 3:
                        self.new_pg[i][j] = 1
                else:   #dead
                    if population == 3:
                        self.new_pg[i][j] = 1

        self.pg = self.new_pg
        self.new_pg = np.zeros((20, 20))

if __name__ == "__main__":
    play = ConWay()
    #play.pg[0][0]=1
    play.pg[0][1]=1
    play.pg[1][0]=1
    play.pg[1][1]=1
    print(play.pg)
    play.new_screen()
    print(play.pg)
    #print(lives)