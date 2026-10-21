#Puneeth Suresh
#2107296@gscs.ca
#Assignment 20 - Coloured Squares

x_list = []          #square x coords
y_list = []          #square y coords
r_list = []          #R colour vars
g_list = []          #G colour vars
b_list = []          #B colour vars
SQUARE_SIZE = 10     #Fixed square size in px


def setup():
    size(500, 500)
    background(200) 


def draw():
    background(200)
    
    for i in range(len(x_list)): #loops for the range of the lenght of the square list, and draws the square.
        fill(r_list[i], g_list[i], b_list[i]) #Fills the square with the "random" rgb value for that specific iteration

        rect(x_list[i] - SQUARE_SIZE / 2, y_list[i] - SQUARE_SIZE / 2, SQUARE_SIZE, SQUARE_SIZE) #Centers the square at the defined coords, by minusing half of the square's size 


def mouse_pressed():
    x_list.append(mouse_x)
    y_list.append(mouse_y)
    
    r_list.append(0) #The new square is created as black
    g_list.append(0)
    b_list.append(0)


def key_pressed():
    if key == 'c' or key == 'C': #If c or C is pressed, for the range of the lenght of the coords list, it will set a random colour between 0 and 255 for the R, G and B
        for i in range(len(x_list)):
            r_list[i] = random(0, 255)
            g_list[i] = random(0, 255)
            b_list[i] = random(0, 255)