#Puneeth Suresh
#2107296@gscs.ca
#Assignment 20 - Coloured Squares

square_x = [] #The global lists to gold the x,y coords and the rgb values
square_y = []
square_r = []
square_g = []
square_b = []

def setup(): #This creates the initial canvas, and has a peice of code to tell the script that the square's coords are defining the center.
    size(500, 500) #500px by 500px canvas
    rect_mode(CENTER) #This is a built in function, and changes how the squares are placed. Now the x,y are the center instead of the top left.

def draw(): #This runs the loop to actually draw the squares
    global square_x, square_x, square_r, square_g, square_b
    background(200) #This runs to prevent smearing
    
    for i in range(len(square_x)): #For the lenght of the square_x, it'll get the correct iteration of the r,g,b values and fill it to that, then, places the rectangle's x, y vars according to the current iteration.
        fill(square_r[i], square_g[i], square_b[i]) #Fills rgb value according to currecnt iteration
        square(square_x[i], square_y[i], 10) #Current x,y vars, size fixed at 10


def mouse_pressed(): #Runs when the mouse is clicked to add the current mouse_x and y to the list.
    global square_x, square_x, square_r, square_g, square_b
    square_x.append(mouse_x) #Appends the mouse_x and y coords to the end of the square_x and square_y lists.
    square_y.append(mouse_y)
    
    square_r.append(0) #Appends r,g,b as 0 (aka black) at the end of square_r, g and b
    square_g.append(0)
    square_b.append(0)

def key_pressed(): #This runs the code to randomize r,g and b if c or C is pressed.
    global square_r, square_g, square_b
    if key == 'c' or key == 'C': #If the key is c or C, it runs the loop below
        for i in range(len(square_x)): #Sets a random value between 0 and 255; square_r, g and b value using a loop that runs for the lenght of square_x.
            square_r[i] = random(0, 255)
            square_g[i] = random(0, 255)
            square_b[i] = random(0, 255)

