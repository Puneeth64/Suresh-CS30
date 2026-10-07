#Puneeth Suresh
#2107296@gscs.ca
#Assignment 15 - How many Hamburgers?

#Defines the global variables for both the patty and bun paks. It is global so that the draw, and key_pressed function can both access them without needing parameters between them.
patty_pak = 0
bun_pak = 0
    
def setup(): #This function runs once when the script is started. The canvas is created with a size of 400x250px.
    size(400,250) #Canvas is 400x250px
    
def draw(): #This draws the text on screen, the code here is rerun 60 times/second.
    global patty_pak, bun_pak #The function is told that these are global variables, and to modify those global vars instead of creating new local vars.
    background(255) #The BG is reset to a blank white upon each pass.
    
    hamburgler = make_hamburgers(patty_pak, bun_pak) #This calculates how many burgers are made. The hamburgler var uses the calc_patty function (defined later) and gives it the patty_pak and bun_pak data as parms. The calc_patty function returns the final value of the amount of burgers made, which is then displayed in the text() function.
    
    fill(0) #The text colour is black, so that it is actually visible.
    text("Patty Packages: " + str(patty_pak), 20, 50) #The patty pak amount is displayed as a string using the str() function and patty_pak var. The text() function can only display strings.
    text("Bun Packages: " + str(bun_pak), 20, 90) #The bun pak amount is displayed using the text() function with the bun_pak var.
    text("Hamburgers Made: " + str(hamburgler), 20, 150) #The amount of hamburgers are displayed using the hamburgler var that was created above.
    text("Press p for more patty; o for less. Press b for more bun, n for less", 20, 200) #Simply displays the controls using the text() function.

    
def key_pressed(): #This runs whenever a key is presseed. This handles the logic to add or remove patty/bun paks.
    global patty_pak, bun_pak #The patty_pak and bun_pak are defined as globals, so that the function doesn't try and create a new local var.
 
    if key == 'p': #If the key pressed is p
        patty_pak += 1 #Adds the value on the right side to the var on the left, so basically adds one to the patty_pak var.
    elif key == 'o': #Else if the key is 0, this runs.
        if patty_pak > 0: # Prevent negative packages by only running the code below if patty_pak is already greater than 0.
            patty_pak -= 1 #Substracts the value on the right side to the var on the left. This time, removes a patty_pak.
    
    elif key == 'b': #Else if the key is b, this will run.
        bun_pak += 1 #bun_pak gets a one added to it's value
    elif key == 'n': #Else if the key is n, this will run
        if bun_pak > 0: # Prevent negative packages, same explanation as with patty_pak's code
            bun_pak -= 1 #bun_pak loses a one from it's value (if it's not a negative)

def make_hamburgers(p_pak, b_pak): #This runs the calculation for how many burgers can be made
    total_patty = p_pak * 8 #Each pak has 8 pattys, so the total amount of patties/pak is 8, so the total_patty pak is patty_pak times 8
    total_bun = b_pak * 12 #The amount of buns/pak is 12. total_bun is b_pak times 12
    
    total_burgers = min(total_patty, total_bun) #min() finds the max complete burgers possible. The min function gives you the lowest value, so if you have 20 patties, and 5 buns, it'll return a 5 since you cna only make 5 burgers.
    
    return total_burgers #Returns the value of total_burgers, so the hamburgler var in draw() gets this value.
    