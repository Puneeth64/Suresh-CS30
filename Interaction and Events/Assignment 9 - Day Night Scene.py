#Puneeth Suresh
#2107296@gscs.ca
#Assignment 9 - Day/Night Scene

def setup(): #Runs only once when the script starts
    size(400, 400) #Win size is set to 400x400px
    background(0, 160, 255) #BG is set to light blue
    frame_rate(1) #FPS is 1 to save power, don't need 60 FPS for this
    son(0) #Draws the sun, makes it yellow
    carpet(181, 101, 29) #Carpet is a light brown
    box1(255, 193, 0) #Orange
    box2(255, 0, 255) #Magenta
    box3(0, 255, 120)#Neon Green
    
def son(son3): #Defines the son function which draws the sun. son3 defines the blue value, since that is the only thing that changes between yellow and white.
    stroke(255, 255, son3) #Strokes the borders with definied colours
    fill(255, 255, son3)#Fills the circle
    circle(200, 30, 50) #Draws a circle at these coords, with a diam of 50px
    
def carpet(car1, car2, car3): #Function to create carpet, takes 3 params, related to R, G and B
    stroke(car1, car2, car3)
    fill(car1, car2, car3)
    rect(0, 350, 400, 50) #Creates a rectangle witht he top left corner at 0, 250px, with a width of 500px, and a height of 50px
    
def box1(bxo1, bxo2, bxo3): #First box function
    stroke(bxo1, bxo2, bxo3)
    fill(bxo1, bxo2, bxo3)
    rect(20, 275, 75, 75) # Rectangle creates at the defined coords, with a size of 75x75px
    
def box2(bxt1, bxt2, bxt3):
    stroke(bxt1, bxt2, bxt3)
    fill(bxt1, bxt2, bxt3)
    rect(160, 275, 75, 75)

def box3(bxtr1, bxtr2, bxtr3):
    stroke(bxtr1, bxtr2, bxtr3)
    fill(bxtr1, bxtr2, bxtr3)
    rect(300, 275, 75, 75)

def key_pressed(): #This activates when any key is pressed
    background(0, 0, 75) #BG is changed to a dark blue
    son(255) #Sun is set to a white (Blue value is now 255 vs. 0)
    carpet(101, 67, 33)#Carpet is now a dark brown
    box1(255, 143, 0) #Switches to a dark orange box
    box2(155, 0, 155) #Dark purple
    box3(0, 150, 70) #Dark green 