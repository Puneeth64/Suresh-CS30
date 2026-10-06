#Puneeth Suresh
#2107296@gscs.ca
#Assignment 14 - Circle in a Box

#Global vars
d = 50 #Diameter of the circle following mouse
border = 20 #Size of the borders in px, change this to change all the border sizes

def setup(): #This function runs once upon the script's startup
    size(400,300) #The canvas is 400x300px as specified in the assignment
    no_stroke() #Disables outlines and borders for shapes, lines or anything else.
    
def draw(): #The code here is rerun 60 times/second
    background(0) #The background is cleared upon each rerun
    
    #Blue borders
    global border #The border variable is global, it uses the one defined above.
    fill(0, 0, 255) #The borders are filled
    
    #The borders are created using rectangle functions. The width and height are the size of the canvas (built-in p5 vars), while the border is the global variable. With these 3 variables, the borders can be made to work with any canvas size, and any border size.
    rect(0, 0, border, height)          # Left border
    rect(width - border, 0, border, height) # Right border
    rect(0, 0, width, border)          # Top border
    rect(0, height - border, width, border) # Bottom border
    
    #draw the dircle
    global d #The d (diameter) variable is global
    fill(255,255,0) #The circle is set to a bright yellow

    r = d / 2 #This tells the code below that radius = diameter/2
    circle_x = constrain(mouse_x, border + r, width - border - r) #This keeps the circle's X dimension in check, by using the built-in constrain function. It also uses the width and border variables to calculate the max distance the circle can move, so it works with any canvas and border size and combination. It also uses the mouse_x variable, so it follows the mouse.
    circle_y = constrain(mouse_y, border + r, height - border - r) #This keeps the circle's Y axis in check.
    
    circle(circle_x, circle_y, d) #The circle is drawn using the coords defined in the function defined above, and uses the diameter defined in the global variable.