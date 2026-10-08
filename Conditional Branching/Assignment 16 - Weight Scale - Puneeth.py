#Puneeth Suresh
#2107296@gscs.ca
#Assignment 16 - Weight Scale

#Global variables for the x and y position of the coins. The initial value is where they start off.
coin1_x = 100
coin1_y = 300

coin2_x = 150
coin2_y = 300

coin3_x = 210
coin3_y = 300

img = None #This variable is created, so that setup can tell the draw function what image to load, without querying the hard drive 60 times/second.


def setup(): #This code runs only once when the script is started. This defines where the image is on the computer, creates the canvas at 550x400px, and it defines that the text should be centered, and at the top
    global img
    size(550, 400) #The canvas is created with a dimension of 550x400px
    
    img = load_image("scale.jpg") #The computer is told that the img that should be loaded is called scale.jpg. This file should be in the same directory.
    
    text_align(CENTER, TOP) #This makes it so that all text is alligned to the center, and top.
      
def draw(): #The code here runs 60 times/second. This is what handles the actual logic of where the coins are, and what side is heavier
    global img, coin1_x, coin1_y, coin2_x, coin2_y, coin3_x, coin3_y #This defines the global variables.
    background(255) #The BG is cleared upon every pass so that there are no ghost circles.
    
    image(img, 0, 0) #The image that was loaded in setup is placed at (0,0). This is the scale.
    
    
     # Draw Coin 1
    fill(255, 215, 0) #gold colour
    circle(coin1_x, coin1_y, 30) #The first circle uses the global vars for coin1_x and y, and has a diameter of 30
    
    # Draw Coin 2
    fill(192, 192, 192) #silver
    circle(coin2_x, coin2_y, 45) #The 2nd circle uses the global vars to place the circle, has a diameter of 45
    
    # Draw Coin 3
    fill(205, 127, 50) #bronze
    circle(coin3_x, coin3_y, 60) #The 3rd circle uses the global vars to place it, has a diameter of 60px.
    
        # Calculate total weight on each side
    left_weight = 0 #Will be set to the total amount of weight on the left side
    right_weight = 0 #The total weight on the right side
    midpoint = width / 2 #The midpoint is for the text, so that it is placed in the center of the canvas.
    
    if (coin1_x > 40 and coin1_x < 180) and (coin1_y > 180 and coin1_y < 240): #If the first coin fits within the bounds of the left balance, left_weight gets 1 added to it.
        left_weight = left_weight + 1
    elif (coin1_x > 360 and coin1_x < 500) and (coin1_y > 180 and coin1_y < 240):#If the first coin fits within the bounds of the right balance, right_weight gets 1 added to it.
        right_weight = right_weight + 1
        
    # Check Coin 2 (Weight = 2)
    if (coin2_x > 40 and coin2_x < 180) and (coin2_y > 180 and coin2_y < 240):#If the second coin fits within the bounds of the left balance, left_weight gets 2 added to it.
        left_weight = left_weight + 2
    elif (coin2_x > 360 and coin2_x < 500) and (coin2_y > 180 and coin2_y < 240): #If the second coin fits within the bounds of the right balance, right_weight gets 2 added to it.
        right_weight = right_weight + 2
        
    # Check Coin 3 (Weight = 3)
    if (coin3_x > 40 and coin3_x < 180) and (coin3_y > 180 and coin3_y < 240): #If the third coin fits within the bounds of the left balance, left_weight gets 3 added to it.
        left_weight = left_weight + 3
    elif (coin3_x > 360 and coin3_x < 500) and (coin3_y > 180 and coin3_y < 240):#If the third coin fits within the bounds of the right balance, right_weight gets 3 added to it.
        right_weight = right_weight + 3

    #Displays the results at the top
    fill(0) 
    if left_weight > right_weight: #If the final result for the variable left_weight is greater than right_weight, the user-facing text says that the left side is heavier.
        text("Scale is unbalanced, the left side is heavier", midpoint, 20)
    elif right_weight > left_weight: #On the other hand, if the right_weight variable is greater, the user-facing text says that the right side is heavier.
        text("Scale is unbalanced, the right side is heavier", midpoint, 20)
    else: #If none if the above statements are true, it's most likely equal, so the user-facing text says that the scale is balanced.
        text("Scale is blanced", midpoint, 20)
        
    text("Press 1 to move the gold coin, 2 for the silver and 3 for the bronze coin", midpoint, 350) #Simple tutorial text, says what key-bind moves what.

def key_pressed(): #This code runs whenever a key is pressed. The code changes what the variable of the x and y for the circles are, and sets it to the mouse poisition if the right key is pressed.
    global coin1_x, coin1_y, coin2_x, coin2_y, coin3_x, coin3_y #These are all global vars.
    
    if key == '1': #If the key pressed is 1, coin 1's x and y are set to mouse_x and y
        coin1_x = mouse_x
        coin1_y = mouse_y
    elif key == '2': #If the key pressed is 2, coin 2's x and y are set to mouse_x and y
        coin2_x = mouse_x
        coin2_y = mouse_y
    elif key == '3': #If the key pressed is 3, coin 3's x and y are set to mouse_x and y
        coin3_x = mouse_x
        coin3_y = mouse_y