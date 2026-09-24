#Puneeth Suresh
#2107296@gscs.ca
#Assignment 11 - Model View Controller

circle_col = 200
bg_col = 200
x = 0
y = 0

def setup():
    size(300, 300)
    background(200, 0, 0)
    
    
def summon_circle():
    global circle_col, x, y
    fill(0, 0, circle_col)
    circle(x, y, 50)
    
def change_bg():
    global bg_col
    background(bg_col, 0, 0)
    
def keyPressed():
    global circle_col, bg_col
    if key == 'b':
        circle_col = circle_col+1
        summon_circle()
    elif key == 'n':
        circle_col = circle_col-1
        summon_circle()