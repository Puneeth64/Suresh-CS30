#Puneeth Suresh
#2107296@gscs.ca
#Assignment 12 - Cube of a Number

#crashes if you click with no numbers, so don't do that :)

string_num = "" #Creates the string_num var which is where the number types by the user will be stored
calcd = 0 #This is the variable which tells the computer whether or not the script has calculated the number or not (This will make sense in the key_pressed function)

def setup(): #This part runs when the script is first started
    size(1000,100) #The canvas is 1000x100 px, since you need more horizontal space than vertical
    background(0) #Black BG

def key_pressed(): #This runs when any key is pressed
    global string_num, calcd # These vars are global, so that the other functions can access the data here.
    
    if calcd == 1: #If the mouse_clicked function has already calculated the cube, the background gets wiped.
        background(0)
        
    if key.isdigit(): #Only lets a key get added to the string if it is a digit
        string_num = string_num + key #The number is added to the string_num string
        text(string_num, 20, 50) #The string is displayed upon every key stroke
    
def mouse_clicked(): #This function runs when the mouse is clicked
    global string_num, calcd # string_num is global, so that this function can use the data from the key_pressed function, and calcd so that the other function knows if the data has been calcd.
    
    background(0) #BG is wiped
    
    cube = int(string_num) #Var cube is created to hold the integer of the string_num var
    cube = pow(cube, 3) #cube var is cubed using the pow function, set to output the integer to the power of 3.
    
    text(f"The cube of {string_num} is {cube}", 20, 50) #The final results are displayed (f = f string, allows me to insert vars using {}
    
    string_num = "" #string_num and int_num vars are wiped
    int_num = 0

    calcd = 1 #key_pressed function is told that the mouse_clicked function has calculated, and to wipe the window on the next key stroke.