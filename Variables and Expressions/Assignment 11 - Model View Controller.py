#Puneeth Suresh
#2107296@gscs.ca
#Assignment 11 - Model View Controller

#Defines the global variables, so I don't have to call stuff a million times as parameters. Change the var in one place; changes everywhere
circle_col = 200 #Circle colour starts off with a blue value of 200, but this value will change as the b or n key is pressed
bg_col = 200 #Background's red value, also starts at 200, but changes as r or d is pressed.
x = 150 #Inital x value for the circle, but will change when the mouse is clicked
y = 150 #Initial y value, will also change as mouse is clicked

def setup(): #Starts right when the script is initiated
    size(300, 300) #Sets the canvas to 300x300px
    change_bg() #Generates the inital BG with the bg_col values defined above
    summon_circle() #Generates the inital circle with the global variables (This will make sense in the actual function)
   
def summon_circle(): #Called when the circle should be created
    global circle_col, x, y #says that these variables are global, not confined to this function
    fill(0, 0, circle_col) #R and G are 0, while the blue value it the circle_col variable
    circle(x, y, 50) #The circle is placed at the x and y global variable, diameter is 50.
    if circle_col < 0: #Prevents the circle_col variable from going into the negatives. WIthout this code, it goes into the negatives, so it'll jump from pitch black to bright red super easily if you hold down the key.
        circle_col = 0 
    elif circle_col > 255: #Same reason as above, but prevents it from going over 255, which is the limit for RGB vals.
        circle_col = 255 
    
def change_bg(): #Called when the bg should be updated/changed
    global bg_col #bg_col is a global variable
    background(bg_col, 0, 0) #Background's red value is set to the bg_col variable, G and B are hard-coded to be 0.
    summon_circle() #Calls the summon_circle funtion, to prevent it from being hidden when the BG is redrawn
    if bg_col < 0: #Created for the same reason as in summon_circle. Prevents the bg_col from going into the negatives, or the over 255.
        bg_col = 0
    elif bg_col > 255:
        bg_col = 255

def key_pressed(): #This runs when any key is pressed
    global circle_col, bg_col #These 2 are global variables
    if key == 'b': #If else statements, if the value of the key pressed is b, this code is executed
        circle_col = circle_col+15 #The value of circle_col is set to circle_col + 25, so if it was 00, its now 225.
        summon_circle() #summon_circle is called to redraw the circle
    elif key == 'n': #If the value of the key pressed is n, the code here is executed
        circle_col = circle_col-15 #global var circle_col is set to circle_col - 25.
        summon_circle() #Circle is redrawn by calling the function
    elif key == 'r': #If the key is r, the code here runs.
        bg_col = bg_col+15 #bg_col is set to bg_col +25
        change_bg() #change_bg is called to redraw the background
    elif key == 'd': #If the d key is pressed, this code runs
        bg_col = bg_col-15 #bg_col is set to bg_col - 25.
        change_bg() #change_bg is called to redraw the background

def mouse_clicked(): #Runs this code when the mouse is clicked (Left,right or middle click)
    global x, y #x and y are global variables
    
    x = mouse_x #The x var is set to the current value of mouse_x
    y = mouse_y #The y var is set to the value of mouse_y
    
    change_bg() #Calls the change_bg function so that the BG is redrawn so that we don't have a multiple circles, and the change_bg function also calls the summon_circle function in it, so the circle is redrawn with the updated x and y variables