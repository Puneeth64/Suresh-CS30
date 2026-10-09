#Puneeth Suresh
#2107296@gscs.ca
#Assignment 17 - Asteroid

import ctypes #This library is used to send calls to the Windows Media controller

ast_x = 0
ast_y = 0
ast_size = 0
score = 0
game_over = False

def setup(): #Creates the initial canvas and asteroid
    size(700, 700)
    
    # Creates initial asteroid
    reset_asteroid()
    play_mp3("彼女なのか.mp3") #Plays the music
    
def play_mp3(file_path): #This is the function to actually play music. Only works on Windows
    # Sends a direct command to Windows Media Control Interface to play the MP3
    stop_mp3()
    ctypes.windll.winmm.mciSendStringW(f"open {file_path} type mpegvideo alias mp3audio", None, 0, 0)
    ctypes.windll.winmm.mciSendStringW("play mp3audio", None, 0, 0)
    
def stop_mp3(): #This function stops the audio
    ctypes.windll.winmm.mciSendStringW("stop mp3audio", None, 0, 0)
    ctypes.windll.winmm.mciSendStringW("close mp3audio", None, 0, 0)

def draw(): #This handles the actual drawing of asteroids, and text (ex. score, game over)
    global ast_size, game_over
    background(0) 
    
    if not game_over:
        #Makes asteroid bigger slowly
        ast_size += 0.5 
        fill(150, 150, 150) # Grey asteroid
        
        # Makes sure that the asteroid is not bigger than a diameter of 100
        if ast_size >= 100:
            ast_size = 100
            game_over = True #If the diameter is over 100, game is over
            stop_mp3() #Stop music on game over
    else:
        fill(255, 0, 0) # Text is red at game over
        
        # Displays the game over text
        text_align(CENTER, CENTER) #The text is centered horizontally, and vertically
        text_size(24) #Make the text size larger
        fill(255, 0, 0) #the text is red
        text("Game over!", width / 2, height / 2) #The game over text is placed right in the center of the canvas
        text("Press 'r' to restart", width / 2, height / 2 + 50) #The press r to restart key is centered, and placed 50 px below the game over text

    # Draw the asteroid circle
    no_stroke() #No borders for the asteroid
    circle(ast_x, ast_y, ast_size) #The actual asteroid is placed at ast_x, ast_y with a diameter of ast_size.
    
    # Display the score
    text_align(LEFT, TOP) #the score is at the top left
    text_size(24) #makes the text not absurdly small 
    fill(255) #Makes the score text colour white.
    text("Score: " + str(score), 20, 20) #Displys the actual score, by converting the score var into a string.

def mouse_pressed(): #This lets the program know if, and where your mouse was clicked, and whether or not you clicked the asteroid. It also handles the scoring.
    global score, game_over

    if not game_over: #only lets you hit the asteroid if the game is still running
        if inside_asteroid(mouse_x, mouse_y, ast_x, ast_y, ast_size): #Checks the function whether the mouse is within the asteroid.
            score += 1 #The score variable gets a 1 added to it
            reset_asteroid() #A new asteroid spawns in at a random spot.

def key_pressed(): #resets the game if r or R is pressed
    global score, game_over

    if key == 'r' or key == 'R': #if the key pressed is r, or R ,the code below runs to reset the score, make the game not over, restart the music and reset the asteroid
        score = 0
        game_over = False
        reset_asteroid()
        play_mp3("彼女なのか.mp3")

def reset_asteroid(): #This spawns a new asteroid at a random coord
    global ast_x, ast_y, ast_size
    #Generates new random position between 50 and 700
    ast_x = random(50, 700)
    ast_y = random(50, 700)
    ast_size = 0 # Starts at diameter 0

def inside_asteroid(x, y, ast_x, ast_y, ast_size): #Function determines if the mouse click is within the asteroid's diameter
    # Calculate distance between clicked point and asteroid center
    distance = dist(x, y, ast_x, ast_y) #The distance var is the distance between the mouse's x and y coords, and the asteroid's x and y coords.
    radius = ast_size / 2.0 #The radius is ast_size divided by 2 (used to see if the click is within the radius)
    
    #returns a True if the distance is less than or equal to the radius.
    if distance <= radius:
        return True
    else:
        return False

