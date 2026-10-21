#Puneeth Suresh
#2107296@gscs.ca
#Assignment 19 - Loop Chessboard


num_tiles = 6  #Global var for number of tiles. Initially a 6x6 square.


def setup(): #This creates the initial 300x300px canvas
    size(300, 300)

            
def draw(): #This handles actually drawing the 
    global num_tiles
    
    tile_size = 20 #Each square is 20px. I got this val by dividing 300px by the amount of squares I should fit, so 15. This got me a value of 20px.
    
    background(160)  #Wipes the BG to gray on every refresh (aka. when the loop is done)
    no_stroke() #Removes the outlines without needing to stroke() each square.
    
    for row in range(num_tiles): #Runs both of these loops for the range of num_tiles
        for col in range(num_tiles): #This loop runs num_tiles amount of times before the row loop runs the next num_tiles iteration.
            if (row + col) % 2 == 0: #If the current coordinates are even (ex. (0, 0) (2,0)), it'll be divided by 2, and thus leave a modulo of 0, confirming that it is even. So that square would be black. If it is (0,1) it'll leave a module, so that would be odd, thus white.
                fill(0)  #Fills square black
            else:
                fill(255)  #Fills square white

            rect(col * tile_size, row * tile_size, tile_size, tile_size) #x and y are multiplied by the tile size, so is the coords are 0,0, the top right is 0,0. But in the next iteration of the loop when it is 1,0, the top left corner will be at 20,0px. It is also tile_size in width and height, so 20px.

def key_pressed(): #This handles increasing and decreasing the num_tiles variable if the correct key is pressed.
    global num_tiles

    if key == '+' or key == '=': 
        num_tiles = min(num_tiles + 1, 15)  #Increases the num_tiles var by 1, but caps at 15 if the user hits + (or = since its on he same key) by using the min function (so if num_value+1 goes over 15, the min is still 15, so that's what the var will be)
    elif key == '-':
        num_tiles = max(num_tiles - 1, 2)  #Same thing as above, but decreases the size if - is hit. Minimum is 2. Uses max() this time.
