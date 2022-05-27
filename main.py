from matplotlib.pyplot import table
import pandas as pd
import random
class game_game():
    def __init__(self):
        self.table = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
        self.random_adding()
        self.random_adding()
        self.display()

    def random_adding(self):
        musaitler = []
        for i in range(0,4):
            for b in range(0,4):
                if self.table[i][b] == 0:
                    musaitler.append([i,b])
                if self.table[i][b] == 2048:
                    print("Kazandınız")
        if len(musaitler) == 0:
            print("Kaybettiniz")
        random_block = random.choice(musaitler)
        line = random_block[0]
        col = random_block[1]
        self.table[line][col] = 2

    def play_r(self):
        self.right_çek()
        for line in self.table:
            for i in range(0,3):
                if line[i] == line[i+1]:
                    line[i] = line[i+1] + line[i]
                    line[i+1] = 0
        self.right_çek()
        self.random_adding()
        self.display()            

    def play_l(self):
        self.left_çek()
        for line in self.table:
            for i in range(2,-1,-1):
                if line[i] == line[i+1]:
                    line[i+1] = line[i+1] + line[i]
                    line[i] = 0
        self.left_çek()
        self.random_adding()
        self.display()  

    def play_u(self):
        r_table = pd.DataFrame(self.table).transpose().values.tolist()
        reversed_table=self.right_çek(r_table)
        for line in reversed_table:
            for i in range(0,3):
                if line[i] == line[i+1]:
                    line[i] = line[i+1] + line[i]
                    line[i+1] = 0
        reversed_table = self.right_çek(r_table)
        self.table = pd.DataFrame(reversed_table).transpose().values.tolist()
        self.random_adding()
        self.display()
    
    def play_d(self):
        r_table = pd.DataFrame(self.table).transpose().values.tolist()
        reversed_table=self.left_çek(r_table)
        for line in reversed_table:
            for i in range(2,-1,-1):
                if line[i] == line[i+1]:
                    line[i+1] = line[i+1] + line[i]
                    line[i] = 0
        reversed_table = self.left_çek(r_table)
        self.table = pd.DataFrame(reversed_table).transpose().values.tolist()
        self.random_adding()
        self.display()          

    def right_çek(self,table=None):
        if table == None:
            for line in self.table:
                for i in range(1,4):
                    for b in range(0,i):
                        if line[b] == 0:
                            line[b] = line[i]
                            line[i] = 0 
        else:
            for line in table:
                for i in range(1,4):
                    for b in range(0,i):
                        if line[b] == 0:
                            line[b] = line[i]
                            line[i] = 0 
            return table

    def left_çek(self,table=None):
        if table == None:
            for line in self.table:
                for i in range(3,-1,-1):
                    for b in range(3,i,-1):
                        if line[b] == 0:
                            line[b] = line[i]
                            line[i] = 0
        else:
            for line in table:
                for i in range(2,-1,-1):
                    for b in range(3,i,-1):
                        if line[b] == 0:
                            line[b] = line[i]
                            line[i] = 0
            return table

    def display(self):
        print("\n")
        for line in self.table:
            print(line)
        print("\n")

game = game_game()

while True:
    rep = input("Hamleniz: ")
    if rep == "quit":
        break
    if rep == "w":
        game.play_u()
    if rep == "s":
        game.play_d()
    if rep == "a":
        game.play_r()
    if rep == "d":
        game.play_l()
