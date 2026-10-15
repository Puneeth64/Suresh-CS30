#Puneeth Suresh
#2107296@gscs.ca
#Assignment 11 - Model View Controller

#Defines the global variables, so I don't have to call stuff a million times as parameters. Change the var in one place; changes everywhere
circle_col = 200 #Circle colour starts off with a blue value of 200, but this value will change as the b or n key is pressed
bg_col = 200 #Background's red value, also starts at 200, but changes as r or d is pressed.
x = 150 #Inital x value for the circle, but will change when the mouse is clicked
y = 150 #Initial y value, will also change as mouse is clicked

def setup(): #Starts right when the script is initiated This part of the view, it only handles the canvas
    size(300, 300) #Sets the canvas to 300x300px
    change_bg() #Generates the inital BG with the bg_col values defined above
    summon_circle() #Generates the inital circle with the global variables (This will make sense in the actual function)
   
def summon_circle(): #Called when the circle should be created. This is a part of view, it handles the circle which is graphical.
    global circle_col, x, y #says that these variables are global, not confined to this function
    fill(0, 0, circle_col) #R and G are 0, while the blue value it the circle_col variable
    circle(x, y, 50) #The circle is placed at the x and y global variable, diameter is 50.
    
def change_bg(): #Called when the bg should be updated/changed. This is view, controlles the background, with no logic.
    global bg_col #bg_col is a global variable
    background(bg_col, 0, 0) #Background's red value is set to the bg_col variable, G and B are hard-coded to be 0.
    summon_circle() #Calls the summon_circle funtion, to prevent it from being hidden when the BG is redrawn

def fix_out_of_range(): #This makes sure the circle_col and bg_col stay within 0 and 255. This is a part of model, it handles variables, and logic.
    global circle_col, bg_col
    if circle_col < 0: #Prevents the circle_col variable from going into the negatives. WIthout this code, it goes into the negatives, so it'll jump from pitch black to bright red super easily if you hold down the key.
        circle_col = 0 
    elif circle_col > 255: #Same reason as above, but prevents it from going over 255, which is the limit for RGB vals.
        circle_col = 255

    if bg_col < 0: #Created for the same reason as in above. Prevents the bg_col from going into the negatives, or the over 255.
        bg_col = 0
    elif bg_col > 255:
        bg_col = 255
    
        
def draw(): #This draws the actual circles, and redraws the BG for when the variables are changed. This is a part of view, it only handles drawing.
    summon_circle() #Summons the circle, and redrawn for when the x,y and colours are changed.
    change_bg() #Redraws for when the bg is changed

def key_pressed(): #This runs when any key is pressed. This is a part of controller, it handles key press logic, and adds a value to the variable if the correct key is pressed.
    global circle_col, bg_col #These 2 are global variables
    if key == 'b': #If else statements, if the value of the key pressed is b, this code is executed
        circle_col = circle_col+15 #The value of circle_col is set to circle_col + 25, so if it was 00, its now 225.
    elif key == 'n': #If the value of the key pressed is n, the code here is executed
        circle_col = circle_col-15 #global var circle_col is set to circle_col - 25.
    elif key == 'r': #If the key is r, the code here runs.
        bg_col = bg_col+15 #bg_col is set to bg_col +25
    elif key == 'd': #If the d key is pressed, this code runs
        bg_col = bg_col-15 #bg_col is set to bg_col - 25.
    
    fix_out_of_range() #Runs after the code, so it can correct the variables if it is over 255, or below 0.

def mouse_clicked(): #Runs this code when the mouse is clicked (Left,right or middle click). This is also controller, it runs when the mouse is clicked to update the x,y var to the mouse_x and y.
    global x, y #x and y are global variables
    
    x = mouse_x #The x var is set to the current value of mouse_x
    y = mouse_y #The y var is set to the value of mouse_y
    
