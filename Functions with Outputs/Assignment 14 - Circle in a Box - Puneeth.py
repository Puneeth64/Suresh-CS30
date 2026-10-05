#Puneeth Suresh
#2107296@gscs.ca
#Assignment 14 - Circle in a Box

d = 50 #Diameter of the circle following mouse
border = 20 #Size of the borders in px

def setup():
    size(300,300)
    no_stroke()
    
def draw():
    background(0)
    
    #Blue borders
    global border
    fill(0, 0, 255)
    
    rect(0, 0, border, height)          # Left
    rect(width - border, 0, border, height) # Right
    rect(0, 0, width, border)          # Top
    rect(0, height - border, width, border) # Bottom
    
    #draw the dircle
    global d
    fill(255,255,0)

    r = d / 2
    circle_x = constrain(mouse_x, border + r, width - border - r)
    circle_y = constrain(mouse_y, border + r, height - border - r)
    
    ellipse(circle_x, circle_y, d, d)