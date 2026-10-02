#Puneeth Suresh
#2107296@gscs.ca
#Assignment 13 - House Placement

def setup(): #This runs when the script is first started.
    size(400, 400) #The canvas is 400x 400px.


def draw(): #The code in this function is looped 60 times per second
    background(0, 101, 0)#The background is wiped to green upon each pass, so that the house doesn't have trails.
    
    draw_tree(50, 20)#All these function calls draw a tree at different coords using the parameters (x,y)
    draw_tree(70, 150)
    draw_tree(90, 170)
    draw_tree(50, 350)
    draw_tree(375, 50)
    draw_tree(375, 300)
    
    lake(200, 300)#This function calls the lake fuunction with the parameters (x,y) to draw a lake at coords (x,y)
    
    draw_house(mouse_x, mouse_y) #Sends the draw_house function the mouse_x and mouse_y coords as the (x,y) parameters 60 times per second, to make it seem like the house is moving with the mouse.

def draw_tree(x, y): #This function draws a tree. the x and y params define where the rectangles and circles below are placed.
    fill(140, 69, 6) #Fills the rectangle brown
    rect(x - 5, y, 10, 35) #Creates the recangle at the coords defined with the parameters, but x is lowered by 5 to not overlap with the circle. has a height of 35, and a width of 10.
    
    fill(0, 255, 0) #Fills the circle green
    circle(x, y, 25) #Circle is centered right on x,y with a diameter of 25
    
def lake(x, y): #This is the lake function. It draws a lake. The function has the parameters x,y which are given to the ellipse, and the x and y coords are where the ellipse is centered.
    fill(0, 255, 255) #Fills the lake cyan.
    ellipse(x, y, 200, 100) #Ellipse is centered at x,y parameters, with a wisth of 200px, and a height of 100 px.
    
def draw_house(x,y): #The draw_house function draws a house with the x and y parameters. This function is fed mouse_x and mouse_y for the x and y parameters 60 times per seconds from the function being called in the draw() fucntion.
    fill(255) #the colour is white for the main house part.
    rect(x - 35, y - 25, 70, 50) #The rectangle is created at x - 35 and y -25, since that is exactly half of the size of the total house, and it has to be placed on the center of the mouse. It has a width of 70px and a heght of 50px.
    
    fill(0, 0, 255) #The roof is filled with a bright blue
    triangle(x - 35, y - 25, x + 35, y - 25, x, y - 55) #The roof is made with the trangle function, and the 3 x and y repeats are the 3 corners of the trangle.
    
    fill(255, 0, 0) #The door isfilled with a red.
    rect(x - 10, y - 5, 20, 30) #The door has a size of 20x30px, and is placed 10px to the left of the x variable (the left side of the house), and 5 down from the y (The top of the house)