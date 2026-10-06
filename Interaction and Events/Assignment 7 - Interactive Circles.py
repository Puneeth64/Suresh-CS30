#Puneeth Suresh
#2107296@gscs,ca
#Asignment 7 - Interactive Circles

def setup(): #This runs first, and only once. The code contained here creates the canvas with a size of 900x600px
    size(900, 600) # creates the windows that is 900x600px
    

def draw(): #Loops everything in this block at 60Hz, this draws the actual circle following the mouse
    background(0)#clears the background with every new frame by setting it to black
    fill(155, 0, 255) # Makes the larger circle purple
    circle(mouse_x, mouse_y, 100) #Circle is created where the mouse is, with a diameter of 100
    fill(0, 255, 255) #Makes the smaller circle a teal
    circle(mouse_x, mouse_y, 50) #Smaller circle pasted on top of the larger at a diameter of 0