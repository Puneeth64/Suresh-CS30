#Puneeth Suresh
#2107296@gscs.ca
#Assignment 12 - Cube of a Number

#crashes if you click with no numbers, so don't do that :). Ignore that, has been fixed now!

string_num = "" #Creates the string_num var which is where the number types by the user will be stored
calcd = 0 #This is the variable which tells the computer whether or not the script has calculated the number or not (This will make sense in the key_pressed function)

def setup(): #This part runs when the script is first started. It creates the actual canvas, and sets the background to black. #View
    size(1000,100) #The canvas is 1000x100 px, since you need more horizontal space than vertical
    background(0) #Black BG

def key_pressed(): #This runs when any key is pressed. This handles adding the numbers to the string_num variable. #controller
    global string_num, calcd # These vars are global, so that the other functions can access the data here.
    
    if calcd == 1: #If the mouse_clicked function has already calculated the cube, the background gets wiped, and calcd gets reset to 0.
        wipe_bg()
        calcd = 0
        
    if key.isdigit(): #Only lets a key get added to the string if it is a digit
        string_num = string_num + key #The number is added to the string_num string
        wipe_bg()#prevents text overlap
        display_value("") #This displays the strng_num to the display. The blank "" are there as a placeholder value for the cube parameter, which is not needed at the moment.

def wipe_bg():
    background(0)
    
def display_value(cube): #This function handles drawing the test to the canvas. The cube parameter gives the cubed value to the text function inside of calcd == 1 #View
    global string_num, calcd
    if calcd == 1: #This text is only displayed if the number has veen calculated
        text(f"The cube of {string_num} is {cube}", 20, 50) #The final results are displayed (f = f string, allows me to insert vars using {}
    else:
        text(string_num, 20, 50) #The string is displayed upon every key stroke
    
def mouse_clicked(): #This function runs when the mouse is clicked. This handles actually displaying the cube to the user after the mouse has been clicked #controller
    global string_num, calcd # string_num is global, so that this function can use the data from the key_pressed function, and calcd so that the other function knows if the data has been calcd.
    
    
    if string_num != "": #Makes it so that the calculations only occur when the string_num variable has data in it
        wipe_bg() #BG is wiped
        cube = int(string_num) #Var cube is created to hold the integer of the string_num var
        cube = pow(cube, 3) #cube var is cubed using the pow function, set to output the integer to the power of 3.
        
        calcd = 1 #key_pressed function is told that the mouse_clicked function has calculated, and to wipe the window on the next key stroke.
        
        display_value(cube) #Displays the text on screen, gives the function the final cubed value
    
        string_num = "" #string_numars are wiped