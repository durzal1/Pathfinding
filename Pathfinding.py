import pygame
import sys
import math
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import os
import time
run = False
pygame.init()
pygame.display.set_caption("Pathfinding")
screen = pygame.display.set_mode((800, 800))
#creates colors that can be used
WHITE = (255, 255, 255)

BLACK = (0, 0, 0)

RED = (255, 0, 0)

GREEN = (0, 255, 0)

yg = (156, 188, 53)
orange = (255,165,0)

BLUE = (0, 0, 255)
screen.fill(BLACK)
w =20
hit_start = False
hit_end = False
walls = []
alg = []

def edit():
    global run

    global x_cords
    global y_cords
    global x_cords2
    global y_cords2
    y_cords = int(y_cord.get())
    x_cords = int(x_cord.get())
    y_cords2 = int(y_cord2.get())
    x_cords2 = int(x_cord2.get())

    global start
    global end
    start = spot(x_cords, y_cords)  # change to a variable
    end = spot(x_cords2, y_cords2)  # change to a variable
    run = True
    root.destroy()

prev_val = 0

root = Tk()
root.geometry("330x200")

go = Button(root, text="Begin", command=edit)
go.grid(row=4, column=0, columnspan=2, pady=10, padx=10, ipadx=140)
#set up window that lets you change start and finish cords
x_cord = Entry(root, width=30)
x_cord.grid(row=0, column=1, padx=20, pady=(10, 0))

y_cord = Entry(root, width=30)
y_cord.grid(row=1, column=1)

x_cord2 = Entry(root, width=30)
x_cord2.grid(row=2, column=1, padx=20, pady=(10, 0))

y_cord2 = Entry(root, width=30)
y_cord2.grid(row=3, column=1)

f_name_label = Label(root, text="x cord for start")
f_name_label.grid(row=0, column=0, pady=(10, 0))
l_name_label = Label(root, text="y cord for start")
l_name_label.grid(row=1, column=0)
f_name_label2 = Label(root, text="x cord for end")
f_name_label2.grid(row=2, column=0, pady=(10, 0))
l_name_label2 = Label(root, text="y cord for end")
l_name_label2.grid(row=3, column=0)
grid = [[n]*35 for n in range(35)]
real_score = [1, 0, 0]
#print (grid)
#creates spot
real_score_ = [0, 0, -20]

first_try = True
global times_repeat
times_repeat = 0
times_repeat1 = 0
class spot:
    x = 0
    y = 0
    global nn
    nn = 0

    #initializes spot
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.neighbors = []
        self.neighbors1 = []
        self.neighbors2 = []
        self.neighbors3 = []
        self.check = []
        self.value = 1
        self.beg = []
        self.end = []
        self.rectangle =(self.x *(w+3) , self.y* (w+3)  , w, w)
        #makes it appear on screen
    def show(self, color):
        pygame.draw.rect(screen, color, self.rectangle)
        pygame.display.update()
    def addNeighbors(self):
        x_ = (self.x * 20) + (self.x * 3)
        y_ = (self.y * 20) + (self.y * 3)
        global added_value
        global nn
        nn += 1
        if nn == 1:
            self.neighbors.append(str(nn) + " : " + str(x_ + 23) + ": " + str(y_))
            #print(self.neighbors)
            nn += 1
        if nn == 2:
            self.neighbors.append(str(nn) + " : " + str(x_ - 23) + ": " + str(y_))
            #print(self.neighbors)
            nn += 1
        if nn == 3:
            self.neighbors.append(str(nn) + " : " + str(x_) + ": " + str(y_ +23))
            #print(self.neighbors)
            nn += 1
        if nn == 4:
            self.neighbors.append(str(nn) + " : " + str(x_) + ": " + str(y_ - 23))
            #print(self.neighbors)
        if not(added_value):
            start.value += 1
            added_value = True
        nn = 0
    def addNeighbors2(self):
        x_ = self.x
        y_ = self.y
        global nn
        global added_value
        nn += 1
        global x_cords
        global y_cords
        global x_cords2
        global y_cords2
        global hit_start
        global hit_end
        #if cord1f == x_cords and cord2f == y_cords:
            #hit_start = True
       #if cord1f == x_cords2 and cord2f == y_cords2:
           # hit_end == True

        if nn == 1:
            self.neighbors.append(str(nn) + " : " + str(x_ + 23) + ": " + str(y_))
            #print(self.neighbors)
            pygame.draw.rect(screen, orange, (x_ + 23, y_, w, w))

            nn += 1
        if nn == 2:
            self.neighbors.append(str(nn) + " : " + str(x_ - 23) + ": " + str(y_))
            #print(self.neighbors)
            pygame.draw.rect(screen, orange, (x_ -23, y_ , w, w))

            nn += 1
        if nn == 3:
            self.neighbors.append(str(nn) + " : " + str(x_) + ": " + str(y_ +23))
            #print(self.neighbors)
            pygame.draw.rect(screen, orange, (x_, y_ + 23, w, w))

            nn += 1
        if nn == 4:
            self.neighbors.append(str(nn) + " : " + str(x_) + ": " + str(y_ - 23))
            #print(self.neighbors)
            pygame.draw.rect(screen, orange, (x_, y_ - 23, w, w))
        if not(added_value):
            start.value += 1
        nn = 0
        pygame.display.update()
    def addNeighbors3(self):
        global times_repeat
        global first_try
        global x_1
        global y_1
        global times_repeat1
        x_ = x_1
        y_ = y_1
        global nn
        global added_value
        nn += 1
        global x_cords
        global y_cords
        global x_cords2
        global y_cords2
        global hit_start
        global hit_end
        global done
        global y_cords

        times_repeat += 1

        x_cor = (x_cords * 20) + (x_cords * 3)
        y_cor = (y_cords * 20) + (y_cords * 3)
        x_cor2 = (x_cords2 * 20) + (x_cords2 * 3)
        y_cor2 = (y_cords2 * 20) + (y_cords2 * 3)
        self.beg.append(str(x_cor) + ":" + str(y_cor))
        self.end.append(str(x_cor2) + ":" + str(y_cor2))

        if x_1 <= 0:
            x_1 *= -1
        if y_1 <= 0:
            y_1 *= -1
        if x_1 > 782:
            x_1 -= 23
        if y_1 > 782:
            y_1 -= 23


        if x_1 + 23 != x_cor or y_1 != y_cor:
            if str(x_1 + 23) + ":" + str(y_1) not in walls:
                if str(x_1 + 23) + ":" + str(y_1) not in self.end:
                    pygame.draw.rect(screen, orange, (x_1 + 23, y_1, w, w))
                    self.neighbors.append(str(nn) + " : " + str(x_1 + 23) + ": " + str(y_1))
                    self.check.append(str(x_1 + 23) + ":" + str(y_))

            elif str(x_1 + 23) + ":" + str(y_1) in walls:
                #print("wall_hit")
                pass
        elif x_1 + 23 == x_cor and y_1  == y_cor:
            print("hit")


        if x_1 - 23 != x_cor or y_1 != y_cor:
            if str(x_1 - 23) + ":" + str(y_1) not in walls:
                if str(x_1 - 23) + ":" + str(y_1) not in self.end:

                    pygame.draw.rect(screen, orange, (x_1 - 23, y_1, w, w))
                    self.neighbors.append(str(nn) + " : " + str(x_1 - 23) + ": " + str(y_1))
                    self.check.append(str(x_1 - 23) + ":" + str(y_1))
            elif str(x_1 - 23) + ":" + str(y_1) in walls:
                print("hit_wall")

        elif x_1 - 23 == x_cor and y_1 == y_cor:
            print("hit")



        if x_1 != x_cor or y_1 + 23 != y_cor:
            if str(x_1) + ":" + str(y_1 + 23) not in walls:
                if str(x_1) + ":" + str(y_1 + 23 ) not in self.end:

                    pygame.draw.rect(screen, orange, (x_1, y_1 + 23, w, w))
                    self.neighbors.append(str(nn) + " : " + str(x_1) + ": " + str(y_1 + 23))
                    self.check.append(str(x_1) + ":" + str(y_1 + 23))
            elif str(x_1) + ":" + str(y_1 + 23) in walls:
                #print("wall_hit")
                pass

        elif x_1 == x_cor and y_1 + 23 == y_cor:
            print("hit")

        if x_1 != x_cor or y_1 - 23 != y_cor:
            if str(x_1) + ":" + str(y_1 - 23) not in walls:
                if str(x_1) + ":" + str(y_1 - 23 ) not in self.end:

                    pygame.draw.rect(screen, orange, (x_1, y_1 - 23, w, w))
                    self.neighbors.append(str(nn) + " : " + str(x_1) + ": " + str(y_1 - 23))
                    self.check.append(str(x_1) + ":" + str(y_1 - 23))
            elif str(x_1) + ":" + str(y_1 - 23) in walls:

                #print("wall_hit")
                pass

        elif x_1 == x_cor and y_1 - 23 == y_cor:
            print("hit")

        if x_1 != x_cor or y_1 != y_cor:
            pygame.draw.rect(screen, orange, (x_, y_, w, w))
        elif x_1 == x_cor and y_1 == y_cor:
            print("hit")
        nn = 1

        self.value += 1
        #print(self.check)
        for i in range(len(self.neighbors)):
            neighbor = self.neighbors[i]
            neighbor_split = neighbor.split(": ")
            x_1 = int(neighbor_split[1])
            y_1 = int(neighbor_split[2])
            # make start.value t then multiply it by x and y values to see if they reach the end
            neighbor_split_value = self.value
            #print(neighbor_split_value)
            if x_1 <= 0:
                x_1 *= -1
            if y_1 <= 0:
                y_1 *= -1
            if x_1 > 782:
                x_1 -= 23
            if y_1 > 782:
                y_1 -= 23
            #print(str(x_1 + 23) + " " + str(y_1))
            if str(x_1 + 23) + ":" + str(y_1) not in self.check:
                if str(x_1 + 23) + ":" + str(y_1) not in walls:
                    if str(x_1 + 23) + ":" + str(y_1) not in self.beg:
                        if str(x_1 + 23) + ":" + str(y_1) not in self.end:

                            pygame.draw.rect(screen, orange, (x_1 + 23, y_1, w, w))
                            self.neighbors.append(str(nn) + " : " + str(x_1 + 23) + ": " + str(y_1))
                            self.check.append(str(x_1 + 23) + ":" + str(y_1))
                            #print("1: good")
                            nn += 1
                        elif str(x_1 + 23) + ":" + str(y_1) in self.end:
                            done = True
                            #pygame.draw.rect(screen, yg, (x_1, y_1, w, w))


                    elif x_ + 23 == x_cords and y_ == y_cords:
                        print("hit")
                elif str(x_1 + 23) + ":" + str(y_1) not in walls:
                    #print("wall_hit")
                    pass



            else:
                pass
                #print("1: not good")
            if str(x_1 - 23) + ":" + str(y_1) not in self.check:
                if x_1 <= 0:
                    x_1 *= -1
                if y_1 <= 0:
                    y_1 *= -1
                if str(x_1 - 23) + ":" + str(y_1) not in self.beg:
                    if str(x_1 - 23) + ":" + str(y_1) not in walls:
                        if str(x_1 - 23) + ":" + str(y_1) not in self.end:

                            pygame.draw.rect(screen, orange, (x_1 - 23, y_1, w, w))
                            self.neighbors.append(str(nn) + " : " + str(x_1 - 23) + ": " + str(y_1))
                            self.check.append(str(x_1 - 23) + ":" + str(y_1))
                            #print("2: good")


                            nn += 1
                        elif str(x_1 - 23) + ":" + str(y_1) not in self.end:
                            done = True
                            #pygame.draw.rect(screen, yg, (x_1, y_1, w, w))

                    elif str(x_1 - 23) + ":" + str(y_1)  in walls:
                        #print("wall_hit")
                        pass

                elif x_ - 23 == x_cords and y_ == y_cords:
                    print("hit")
            else:
                pass
                #print("2: not good")
            if str(x_1) + ":" + str(y_1 + 23) not in self.check:
                if x_1 <= 0:
                    x_1 *= -1
                if y_1 <= 0:
                    y_1 *= -1
                if str(x_1) + ":" + str(y_1 + 23) not in self.beg:
                    if str(x_1) + ":" + str(y_1 + 23) not in walls:
                        if str(x_1) + ":" + str(y_1 + 23) not in self.end:

                            pygame.draw.rect(screen, orange, (x_1, y_1 + 23, w, w))
                            self.neighbors.append(str(nn) + " : " + str(x_1) + ": " + str(y_1 + 23))
                            self.check.append(str(x_1) + ":" + str(y_1 + 23))
                            #print("3: good")
                            nn += 1
                        if str(x_1) + ":" + str(y_1 + 23) in self.end:
                            done = True
                            #pygame.draw.rect(screen, yg, (x_1, y_1, w, w))


                    elif str(x_1) + ":" + str(y_1 + 23) in walls:
                        #print("wall_hit")
                        pass

                elif x_ == x_cords and y_ + 23 == y_cords:
                    print("hit")
            else:
                pass
                #print("3: not good")
            if str(x_1) + ":" + str(y_1 - 23) not in self.check:
                if x_1 <= 0:
                    x_1 *= -1
                if y_1 <= 0:
                    y_1 *= -1
                if str(x_1) + ":" + str(y_1 - 23) not in self.beg:
                    if str(x_1) + ":" + str(y_1 - 23) not in walls:
                        if str(x_1) + ":" + str(y_1 - 23) not in self.end:

                            pygame.draw.rect(screen, orange, (x_1, y_1 - 23, w, w))
                            self.neighbors.append(str(nn) + " : " + str(x_1) + ": " + str(y_1 - 23))
                            self.check.append(str(x_1) + ":" + str(y_1 - 23))
                            #print("4: good")
                            nn += 1
                        if str(x_1) + ":" + str(y_1 - 23) in self.end:
                            done = True
                            #pygame.draw.rect(screen, yg, (x_1, y_1, w, w))


                    elif str(x_1) + ":" + str(y_1 - 23) in walls:
                        #print("wall_hit")

                        pass

                elif x_1 == x_cords and y_1 - 23 == y_cords:
                    print("hit")
            else:
                pass


                # make start.value t then multiply it by x and y values to see if they reach the end
                #def heuritic and make call it after done. Use distance formula to determine it and also use the in i range
                #print("4: not good")
            #print(len(self.neighbors))
            #now make it check if it hits start/finish then walls


        pygame.display.update()
        #print(self.neighbors)
        #print(self.x, self.y)
    def heur(self):
        global heur
        global prev_val
        global real_score_

        x_ = int(self.x * 20) + (self.x * 3)
        y_ = int(self.y * 20) + (self.y * 3)
        x_cor = (x_cords * 20) + (x_cords * 3)
        y_cor = (y_cords * 20) + (y_cords * 3)
        x_cor2 = (x_cords2 * 20) + (x_cords2 * 3)
        y_cor2 = (y_cords2 * 20) + (y_cords2 * 3)
        tentative_gScore = math.sqrt((x_ - x_cor2) ** 2 + (y_ - y_cor2) ** 2)
        #print(tentative_gScore)
        g_score1 = math.sqrt(((x_ + 23) - x_cor2) ** 2 + (y_ - y_cor2) ** 2)
        g_score2 = math.sqrt(((x_ - 23) - x_cor2) ** 2 + (y_ - y_cor2) ** 2)
        g_score3 = math.sqrt(((x_) - x_cor2) ** 2 + ((y_ + 23) - y_cor2) ** 2)
        g_score4 = math.sqrt(((x_) - x_cor2) ** 2 + ((y_ - 23) - y_cor2) ** 2)
        work = [tentative_gScore, x_, y_]

        tentative_gScore = 10000

        if g_score1 <= tentative_gScore:
            if str(x_ + 23) + ":" + str(y_) not in walls:
                tentative_gScore = g_score1
                work = [tentative_gScore, x_ + 23, y_]
            elif str(x_ + 23) + ":" + str(y_) in walls:
                print("worked")
        if g_score2 <= tentative_gScore:
            if str(x_ - 23) + ":" + str(y_) not in walls:
                tentative_gScore = g_score2
                work = [tentative_gScore, x_ - 23, y_]
            elif str(x_ - 23) + ":" + str(y_) in walls:
                print("worked")
        if g_score3 <= tentative_gScore:
            if str(x_ ) + ":" + str(y_ + 23) not in walls:
                tentative_gScore = g_score3
                work = [tentative_gScore, x_, y_ + 23]

        if g_score4 <= tentative_gScore:
            if str(x_) + ":" + str(y_ - 23) not in walls:
                tentative_gScore = g_score4
                work = [tentative_gScore, x_, y_ - 23]



        pygame.draw.rect(screen, yg, (work[1], work[2], w, w))
        val = self.value - 1
        #todo figure out how to automate this
        if prev_val < val:
            alg.append(str(real_score_[1]) + ":" + str(real_score_[2]))
            pygame.draw.rect(screen, yg, (real_score_[1], real_score_[2], w, w))

            for i in range(len(self.neighbors)):
                neighbor = self.neighbors[i]
                neighbor_split = neighbor.split(": ")
                x_1 = int(neighbor_split[1])
                y_1 = int(neighbor_split[2])
                if str(x_1) + ":" + str(y_1 - 23) not in walls:
                    g_score1 = math.sqrt((x_1 - x_cor2) ** 2 + (y_1 - y_cor2) ** 2)

                if str(x_1) + ":" + str(y_1 + 23) not in walls:
                    g_score1 = math.sqrt((x_1 - x_cor2) ** 2 + (y_1 - y_cor2) ** 2)


                if str(x_1 + 23) + ":" + str(y_1 ) not in walls:
                    g_score1 = math.sqrt((x_1 - x_cor2) ** 2 + (y_1 - y_cor2) ** 2)

                if str(x_1 - 23) + ":" + str(y_1 - 23) not in walls:
                    g_score1 = math.sqrt((x_1 - x_cor2) ** 2 + (y_1 - y_cor2) ** 2)



                if g_score1 < tentative_gScore:
                    tentative_gScore = g_score1
                    real_score_ = [tentative_gScore, x_1, y_1]

                if g_score1 == tentative_gScore:
                    pass
                prev_val = val




            #make this only work if walls arent placed


            pygame.display.update()










        heur = False
    def check1(self):
        x_ = int(self.x * 20) + (self.x * 3)
        y_ = int(self.y * 20) + (self.y * 3)
        x_cor = (x_cords * 20) + (x_cords * 3)
        y_cor = (y_cords * 20) + (y_cords * 3)
        x_cor2 = (x_cords2 * 20) + (x_cords2 * 3)
        y_cor2 = (y_cords2 * 20) + (y_cords2 * 3)
        tentative_gScore = math.sqrt((x_ - x_cor2) ** 2 + (y_ - y_cor2) ** 2)

        for i in range(len(self.neighbors)):
            neighbor = self.neighbors[i]
            neighbor_split = neighbor.split(": ")
            x_1 = int(neighbor_split[1])
            y_1 = int(neighbor_split[2])

            x_2 = x_1
            y_2 = y_1
            x_3 = x_1
            y_3 = y_1

            if i < len(self.neighbors) - 1:
                # print(i)
                neighbor1 = self.neighbors[i + 1]
                neighbor_split2 = neighbor1.split(": ")

                x_2 = int(neighbor_split2[1])
                y_2 = int(neighbor_split2[2])
                # print(x_2 ,  y_2)
            if i > 1:
                print("work")

                neighbor2 = self.neighbors[i - 1]
                neighbor_split3 = neighbor2.split(": ")
                x_3 = int(neighbor_split3[1])
                y_3 = int(neighbor_split3[2])
                #print(x_3 , y_3)

            g_score = math.sqrt((x_1 - x_cor2) ** 2 + (y_1 - y_cor2) ** 2)
            g_score1 = math.sqrt((x_2 - x_cor2) ** 2 + (y_2 - y_cor2) ** 2)
            g_score2 = math.sqrt((x_3 - x_cor2) ** 2 + (y_3 - y_cor2) ** 2)


            if g_score1 < g_score:
                pygame.draw.rect(screen, orange, (x_1, y_1, w, w))
            if g_score2 < g_score:
                pygame.draw.rect(screen, orange, (x_1, y_1, w, w))



heur = True

class Walls:
    x = 0
    y = 0
    #initalize wall
    def __init__(self, x ,y):

        self.x = x
        self.y = y
        self.walls = []

        self.rectangle =(self.x *(w+3) , self.y* (w+3)  , w, w)
    def show(self, grid):
        pygame.draw.rect(screen, RED, self.rectangle)
        pygame.display.update()

#created the 35x35 grid
def drawGrid():
    x=0
    y=0



    for row in grid:
        for col in row:
            box = pygame.Rect(x, y, w, w)
            pygame.draw.rect(screen, WHITE, box)
            x = x + w + 3
        y = y + w + 3
        x=0
#start = grid[12][5]
#end = grid[3][6]
#creates the start and end function

root.mainloop()

wall_create = False
#runs grid and allows placement of walls
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    drawGrid()
    start.show(BLUE)
    end.show(GREEN)
    pygame.display.update()

    run = False
    wall_create = True
    break


wallnum = int(0)
def mouse_pressed(x):
    global wallnum
    wallnum += 1
    global cord1f
    global cord2f
    global hit_start
    global hit_end
    posx = x[0]
    posy = x[1]
    cord1f = posx // (800 // 35)
    cord2f = posy // (800 // 35)
    x_cor = (x_cords * 20) + (x_cords * 3)
    y_cor = (y_cords * 20) + (y_cords * 3)
    x_cor2 = (x_cords2 * 20) + (x_cords2 * 3)
    y_cor2 = (y_cords2 * 20) + (y_cords2 * 3)


    if not(hit_start) and not(hit_end):
        if cord1f ==0 and cord2f == 0:
            #print("0")
            cord1 = (posx // (800 // 35) * 20 ) + (posx // (800 // 35) * 3)
            cord2 = (posy // (800 // 35) * 20 ) + (posy // (800 // 35) * 3 )



        elif cord1f >= 18 and cord2f <= 18:
            #print("x>=18 and y<=18")
            cord1 = (posx // (800 // 35) * 20- 20) + (posx // (800 // 35) * 3- 3)
            cord2 = (posy // (800 // 35) * 20 ) + (posy // (800 // 35) * 3 )
        elif cord2f >= 18 and cord1f >=18:
           #print("x >= 18 and y >=18")
            cord1 = (posx // (800 // 35) * 20 - 20) + (posx // (800 // 35) * 3 - 3)
            cord2 = (posy // (800 // 35) * 20- 20 ) + (posy // (800 // 35) * 3 -3 )
        elif cord1f >= 1 and cord2f >= 18 and cord1f <= 15:
            #print("x>=1 and x<=15 and y>=18")
            cord1 = (posx // (800 // 35) * 20 ) + (posx // (800 // 35) * 3 )
            cord2 = (posy // (800 // 35) * 20 - 20) + (posy // (800 // 35) * 3 - 3)
        elif cord1f == 0 and cord2f <= 17:
            #print("x == 0 and y <= 14")
            cord1 = (posx // (800 // 35) * 20) + (posx // (800 // 35) * 3)
            cord2 = (posy // (800 // 35) * 20) + (posy // (800 // 35) * 3)
        elif cord1f == 0 and cord2f >=14:
            #print(x ==0 and y>=14)
            cord1 = (posx // (800 // 35) * 20) + (posx // (800 // 35) * 3)
            cord2 = (posy // (800 // 35) * 20 - 20) + (posy // (800 // 35) * 3 - 3)


        elif cord1f != 0 and cord2f == 0:
            #print("x")
            cord1 = (posx // (800 // 35) * 20) + (posx // (800 // 35) * 3)
            cord2 = (posy // (800 // 35) * 20) + (posy // (800 // 35) * 3)
        else:

            #print("else")
            cord1 = (posx // (800 // 35) * 20) + (posx // (800 // 35) * 3)
            cord2 = (posy // (800 // 35) * 20) + (posy // (800 // 35) * 3)
        if cord1 == x_cor and cord2 == y_cor:
            print("wall has been hit start")
        elif cord1 == x_cor2 and cord2 == y_cor2:
            print("wall has been hit end")
        elif cord1 != x_cor or cord2 != y_cor:
            rectangle = (cord1, cord2, w, w)
            pygame.draw.rect(screen, RED, rectangle)
            # print("pixel", posx ,posy)
            print("output", cord1, cord2)
            # print("cord",cord1f , cord2f)
            # walls.append(Walls(posx, posy))
            walls.append(str(cord1) + ":" + str(cord2))
            print(walls)
            #print("no wall has been hit start")


        elif cord1 != x_cor2 or cord2 != y_cor2:

            rectangle = (cord1, cord2, w, w)
            pygame.draw.rect(screen, RED, rectangle)
            # print("pixel", posx ,posy)
            print("output", cord1, cord2)
            # print("cord",cord1f , cord2f)
            # walls.append(Walls(posx, posy))
            walls.append(str(cord1) + ":" + str(cord2))
            print(walls)
            #print("no wall has been hit end")
        # wall = walls.index(walls[])
        #print(walls)
    else:
        print("wtf")

    hit_end = False
    hit_start = False





mainseq = False

while wall_create:
    ev = pygame.event.get()

    for event in ev:
        if event.type == pygame.QUIT:
            pygame.quit()
        if pygame.mouse.get_pressed()[0]:
            pos = pygame.mouse.get_pos()
            mouse_pressed(pos)
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                wall_create = False

                mainseq = True
                break

    pygame.display.update()
first_neighbor = False
added_value = False

done = False


def main():
    global first_neighbor
    global added_value
    global done
    global times_repeat
    if not(first_neighbor):
        global x_1
        global y_1
        x_1 = (start.x * 20) + (start.x*3)
        y_1 = (start.y * 20) + (start.y*3)

        while not(done):
            start.addNeighbors3()
            start.heur()
        for i in range(len(alg)):
            algs = alg[i]
            alg_split = algs.split(":")
            x1 = int(alg_split[0])
            y1 = int(alg_split[1])
            if not walls:
                pygame.draw.rect(screen, yg, (x1, y1, w, w))
            if walls:
                for a in range(len(start.neighbors)):
                    neighbor = start.neighbors[a]
                    neighbor_split = neighbor.split(": ")
                    x2 = int(neighbor_split[1])
                    y2 = int(neighbor_split[2])






while mainseq:
    pygame.display.update()
    main()

