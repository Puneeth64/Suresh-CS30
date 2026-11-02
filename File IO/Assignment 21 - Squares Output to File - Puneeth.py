#Puneeth Suresh
#2107296@gscs.ca
#Assignment 21 - Squares Output to File

square_x = [] #The global lists to hold the x,y coords and the rgb values/ size values
square_y = []
square_r = []
square_g = []
square_b = []
square_s = []

def setup(): #This creates the initial canvas, and has a peice of code to tell the script that the square's coords are defining the center.
    size(500, 500) #500px by 500px canvas
    
def draw(): #This runs the loop to actually draw the squares
    background(0) #This runs to prevent smearing
    rect_mode(CENTER) #This is a built in function, and changes how the squares are placed. Now the x,y are the center instead of the top left.
    
    for i in range(len(square_x)): #For the lenght of the square_x, it'll get the correct iteration of the r,g,b values and fill it to that, then, places the rectangle's x, y vars according to the current iteration.
        fill(square_r[i], square_g[i], square_b[i]) #Fills rgb value according to currecnt iteration
        square(square_x[i], square_y[i], square_s[i]) #Current x,y vars, size fixed at 10


def mouse_pressed(): #Runs when the mouse is clicked to add the current mouse_x and y to the list.
    square_x.append(mouse_x) #Appends the mouse_x and y coords to the end of the square_x and square_y lists.
    square_y.append(mouse_y)
    
    square_r.append(random(0, 255)) #Appends a random colour to the end of square_r, g and b
    square_g.append(random(0, 255))
    square_b.append(random(0, 255))

    square_s.append(random(5,30)) #Appends a random size at the end of square_s between a size of 5 and 30.

def key_pressed(): #This runs the code to export the data to a txt file
    data = open("square_data_pts.txt", "w")
    
    for i in range(len(square_x)): #Puts all the values of each list into a single list
        row_values = [square_x[i], square_y[i], square_r[i], square_g[i], square_b[i], square_s[i]] 
        
        row_strings = [] #Creates a black row_strings list, will be used below.
        
        for things in row_values: #For the amount of things in row_values, it'll add that data into row_strings as a string.
            row_strings.append(str(things))
            
        lin = "\t".join(row_strings) + "\n" #Sets the lin var to a blank space attached to the row_strings var, and creates a new line at the very end for the next iteration of the loop.
        
        data.write(lin) #Write the lin var to the txt file at the end of every iteration
        
    data.close() #Safely closes the file at the end
    
    exit_sketch() #Terminates the program safely. Using exit() forcefully terminated the sketch before the script finished writing data. exit_sketch() stops the sketch safely.


