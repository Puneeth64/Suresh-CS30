#Puneeth Suresh
#2107296@gscs.ca
#Assignment 6 - The Robot!

sc1 = 255 # defines global variables; starts off as yellow
sc2 = 255
sc3 = 0

def setup(): #Runs this only once, when the script starts
    size(400, 600) #sets the canvas size to 400x600px, matches the robot size
    background(0, 0, 160) #Background is all blue
    frame_rate(5) #Sets FPS to 5, since it saves power, and this script doesn't need a high frame rate
    draw_the_robot(250, sc1, sc2, sc3) #Uses the global variables to draw a robot with yellow accents

def draw_head(pc):
    fill(pc) #fills the head with the colour of the pc variable passed to the function (don't need to stroke it, since the default outline is black)
    x = 200 #defines the main x value (makes it easy to move later)
    y = 200 #defines the main heads y value, for the same reason as above
    circle(x - 50, y - 50, 60) #left ear, y value is exactly 50 up, and 50 px to the left
    circle(x + 50, y - 50, 60) #right ear same y value as before, but 50 to the right in relation to the circle's y value
    circle(x, y, 100) #creates the main circle for the bot's head at 200,200 with a diameter of 100

    fill(0) #sets fill to black for the eye balls
    circle(x - 20, y, 10) #creates the left eye, -20 px from the middle of the head, same y value
    circle(x + 20, y, 10) #creates right eye, 20px to the right.
  
def draw_body(pc): 
    x = 200 #sets the main x value for where the body is
    y = 350 #and main y value
    fill(pc) #sets the colour of the body, as defined in pc
    ellipse(x, y, 100, 200) #places the variable in (x,y) with a width of 100 and a height of 200
    
    fill(255, 0, 255) #creates the first circle with a colour of magenta
    circle(x -20, y, 10) #circle has a diameter of 10, x value of 20 minus the center of the torso, same y value
    
    fill(0, 255, 255) #teal colour for 2nd circle
    circle(x, y, 10) #diameter of 10, circle is centered on the center of the torso
    
    fill(255, 255, 0) #colour of yellow
    circle(x + 20, y, 10) #d of 10, x is 20 to the right in relation to the torso
  
def draw_arms(pc, sc1, sc2, sc3):
    x = 200 #defines where the arms will be centered
    y = 300
    fill(pc) #fills the arms using the var pc
    rect(x - 10, y, - 90 , 15) #ceates the rectangle at 10px to the left, y 300, 90px wide reflected so that it goes to the left rather than the right, and is 15 tall.
    rect(x + 10, y, 90, 15) #10px to the right, 90 px wide, goes to the right, 15 tall.
    fill(sc1, sc2, sc3) #sets circle to the colour defined using sc when the function was called
    circle(x - 100, y + 5, 30) #left circle created 100px to the left of the center of the body. 5 px added to y in order to center the arms.
    circle(x + 100, y + 5, 30) #left circle is 100 pc to the right.

  
def draw_legs(pc, sc1, sc2, sc3): 
    x = 200
    y = 400
    
    fill(pc) #fills legs to same colour as pc var defined
    rect(x - 15, y, -15, 100) # is the x value, but 10 px to the left, and width is reflected along the y axis. additionally, it is 90px tall.
    rect(x + 15, y, 15, 100)# 10 px to the right of the x value, 15 wide, and 90 tall.
    
    fill(sc1, sc2, sc3) #sets feet to same colour as defined in function
    circle(x - 25, y + 110, 30) #creates right foot
    circle(x + 25, y + 110, 30) #creates left foot
  
def draw_the_robot(pc, sc1, sc2, sc3):  #defines the variavles that are passed through
    draw_head(pc) #passes the variables to all the existing functions.
    draw_arms(pc, sc1, sc2, sc3)
    draw_legs(pc, sc1 ,sc2, sc3)
    draw_body(pc)
    
def mouse_clicked(): #Runs this function when the mouse is clicked
    global sc1, sc2 #Modifies the globalv variables sc1 and sc2
    sc1 = mouse_y #Sets the red value to mouse's y value
    sc2 = mouse_x #Sets the green value to mouse's x value
    draw_the_robot(250, sc1, sc2, sc3) #draws the robot with the new values.
