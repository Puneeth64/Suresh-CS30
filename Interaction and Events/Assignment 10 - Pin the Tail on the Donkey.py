#Puneeth Suresh
#2107296@gscs.ca
#Assignment 10 - Pin the Tail on the Donkey
def setup(): #Runs once when the script is started
    size(400, 400) # makes the canvas size 400px x 400px, make the donkey mostly centered, and gives enough room
    background(100)
    summon_donkey() #Calls this function on startup to place the donkey on the background
    frame_rate(10) #Sets the FPS to 10 to be more efficient. This script does not require a high frame rate
    
def summon_donkey():
        fill(210, 105, 30) #Donkey code copy pasted from the assignment dropbox; makes the orange "donkey"
        rect(130, 160, 40, 40)
        rect(145, 220, 20, 55)
        rect(155, 220, 20, 55)
        rect(220, 220, 20, 55)
        rect(230, 220, 20, 55)
        ellipse(200, 200, 140, 60)
        ellipse(150, 125, 15, 55)
        ellipse(160, 125, 15, 55)
        ellipse(130, 155, 80, 40)
    
def summon_tail(): #This function is called to create the tail
    fill(255, 163, 98) #This makes the main rectangle a lighter orange
    rect(mouse_x, mouse_y, 7, 25) #Hard coded to set the top left corner the mouse's x and y axis. Has a width of 7px, and a height of 25px
    fill(255, 0, 0) #Makes the circle a bright red
    circle(mouse_x, mouse_y, 10) #Circle is hard coded to be centered at the mouse's x and y value, and circle has a diameter of 10px
    
def mouse_clicked(): #This function is executed when the left mouse button is clicked
    summon_tail() #Calls the summon tail function to create the tail
    
def key_pressed(): #This function activates when any key is pressed
    background(100) #Resets the background to a blank grey; clearing the tails and donkey
    summon_donkey() #Places the donkey again on the background