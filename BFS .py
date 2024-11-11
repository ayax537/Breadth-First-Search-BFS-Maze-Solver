# -*- coding: utf-8 -*-
"""
Created on Sun Dec 24 17:05:30 2023

@author: HP
"""

import turtle
import time
from collections import deque

wn = turtle.Screen()
wn.bgcolor("black")
wn.title("A Maze Solving Program")
wn.setup(1300, 700)

class Maze(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("white")
        self.penup()
        self.speed(0)

class Green(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("green")
        self.penup()
        self.speed(0)

class Blue(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("blue")
        self.penup()
        self.speed(0)

class Red(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("red")
        self.setheading(270)
        self.penup()
        self.speed(0)

class Yellow(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("circle")
        self.color("yellow")
        self.penup()
        self.speed(0)


grid4 = [
    "+++++++++++++++",
    "              e",
    "               ",
    "               ",
    "               ",
    "               ",
    "               ",
    "               ",
    "s              ",
    "+++++++++++++++",
]

grid2 = [
"+++++++++++++++",
"+s+       + +e+",
"+ +++++ +++ + +",
"+ + +       + +",
"+ +   +++ + + +",
"+ + + +   + + +",
"+   + + + + + +",
"+++++ + + + + +",
"+     + + +   +",
"+++++++++++++++",
 ]

grid3 = [
"+++++++++",
"+ ++ ++++",
"+ ++ ++++",
"+ ++ ++++",
"+s   ++++",
"++++ ++++",
"++++ ++++",
"+      e+",
"+++++++++",
 ]

grid1 = [
"++++++++++++++++++++++++++++++++++++++++++++++",
"+ s             +                            +",
"+ +++++++++++ +++++++++++++++ ++++++++ +++++ +",
"+           +                 +        +     +",
"++ +++++++ ++++++++++++++ ++++++++++++++++++++",
"++ ++    + ++           + ++                 +",
"++ ++ ++ + ++ ++ +++++ ++ ++ +++++++++++++++ +",
"++ ++ ++ + ++ ++ +     ++ ++ ++ ++        ++ +",
"++ ++ ++++ ++ +++++++++++ ++ ++ +++++ +++ ++ +",
"++ ++   ++ ++             ++          +++ ++ +",
"++ ++++ ++ +++++++++++++++++ +++++++++++++++ +",
"++    + ++                   ++              +",
"+++++ + +++++++++++++++++++++++ ++++++++++++ +",
"++ ++ +                   ++          +++ ++ +",
"++ ++ ++++ ++++++++++++++ ++ +++++ ++ +++ ++ +",
"++ ++ ++   ++     +    ++ ++ ++    ++     ++ +",
"++ ++ ++ +++++++ +++++ ++ ++ +++++++++++++++ +",
"++                     ++ ++ ++              +",
"+++++ ++ + +++++++++++ ++ ++ ++ ++++++++++++e+",
"++++++++++++++++++++++++++++++++++++++++++++++",
 ]

start_x = 0
start_y = 0
end_x = 0
end_y = 0

def setup_maze(grid):
    global start_x, start_y, end_x, end_y
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            character = grid[y][x]
            screen_x = -588 + (x * 24)
            screen_y = 288 - (y * 24)

            if character == "+":
                maze.goto(screen_x, screen_y)
                maze.stamp()
            if character == " ":
                path.append((screen_x, screen_y))
            if character == "e":
                yellow.goto(screen_x, screen_y)
                yellow.stamp()
                end_x, end_y = screen_x, screen_y
                path.append((screen_x, screen_y))
            if character == "s":
                start_x, start_y = screen_x, screen_y
                red.goto(screen_x, screen_y)

def search(x, y):
    queue = deque([(x, y)])
    solution[x, y] = x, y
    while queue:
        time.sleep(0)
        current = queue.popleft()

        x, y = current
        if (x - 24, y) in path and (x - 24, y) not in visited:
            cellleft = (x - 24, y)
            solution[cellleft] = x, y
            blue.goto(cellleft)
            blue.stamp()
            queue.append(cellleft)

        if (x, y - 24) in path and (x, y - 24) not in visited:
            celldown = (x, y - 24)
            solution[celldown] = x, y
            blue.goto(celldown)
            blue.stamp()
            queue.append(celldown)

        if (x + 24, y) in path and (x + 24, y) not in visited:
            cellright = (x + 24, y)
            solution[cellright] = x, y
            blue.goto(cellright)
            blue.stamp()
            queue.append(cellright)

        if (x, y + 24) in path and (x, y + 24) not in visited:
            cellup = (x, y + 24)
            solution[cellup] = x, y
            blue.goto(cellup)
            blue.stamp()
            queue.append(cellup)

        visited.append(current)
        green.goto(x, y)
        green.stamp()
        if (x, y) == (end_x, end_y):
            yellow.stamp()
        if (x, y) == (start_x, start_y):
            red.stamp()

def backRoute(x, y):
    yellow.goto(x, y)
    yellow.stamp()
    while (x, y) != (start_x, start_y):
        yellow.goto(solution[x, y])
        yellow.stamp()
        x, y = solution[x, y]

maze = Maze()
red = Red()
blue = Blue()
green = Green()
yellow = Yellow()
walls = []
path = []
visited = []
solution = {}

setup_maze(grid1)
search(start_x, start_y)
backRoute(end_x, end_y)

wn.exitonclick()
