#Puneeth Suresh
#2107296@gscs.ca
#Assignment 21 - The Robot!'s Repair Shop

#global lists, auto global don't need to mention that it's a global in each function.

menu = ["Hand", "Foot", "Ear", "Button"] #The orderable items, and the prices for the item
prices = [20, 15, 10, 5]

order = [] #Blank list for the user's order

def setup(): #Runs once on startup, creates the actual 500x500px canvas
    size(500, 500)

def draw(): #This handles the actual view, so drawing bascially drawing text
    background(255) #Wipes the BG on every loop of draw, so there isn't ghost text.
    
    line(240, 0, 240, 420) #Creates the center divide line
      
    #The left menu side's menu text
    fill(0)
    text_size(32) #Makes the text larger
    text("Menu", 30, 50) #Displays "Menu" at 30,50
    
    text_size(20)
    menu_y = 90 #Defines the y coord for the top of the menu (so I can change this easily if something is off)
    for i in range(len(menu)): #This allows menu[] to be added to later. For the range of the lenght of menu[], this loops.
        text(menu[i] + ": $" + str(prices[i]), 30, menu_y) #The current iteration's menu item is showed in a text, along with the price[] of the same iteration.
        menu_y += 30 #This adds 3 to menu_y, so that text doesn't overlap
        
    #The right order side
    text_size(32)
    text("Your Order", 270, 50) #Just says "Your Order" at 270,50
    
    #Displays each ordered item line by line
    text_size(20)
    order_y = 90
    for item in order: #For the things in the order list, it loops this function.
        text(item, 270, order_y) #The text displays the current iteration's order value, fixed at x 270, and order_y y coord, which increases on each iteration.
        order_y += 25 #Fixes overlap
    
    total_cost = calc_cost() #Receives the total cost from the calc_cost() function
      
    #Displays the total cost on the bottom
    text_size(20)
    text("Cost: $" + str(total_cost), 310, 430) #Turns the total_cost var into a string, and displays it to the user.

def key_pressed(): #This handles adding or removing items from the order with the right key press
    if key == 'h' or key == 'H': #Adds a Hand to the list
        add_to_order("Hand")#Sends a call to the function add_to_order with the parameter "Hand" to append to the order list. Same things happen below, but with different items sent to the function.
    elif key == 'f' or key == 'F':
        add_to_order("Foot")
    elif key == 'e' or key == 'E':
        add_to_order("Ear")
    elif key == 'b' or key == 'B':
        add_to_order("Button")
    elif key == 'u' or key == 'U': #When U is pressed, the last item is deleted from the order.
        del_order() #undo_order() sends a pop() command to the order list, to remove the last item (as long as the lenght of the order is over 0)
        
def calc_cost(): #Calculates total cost of order
    total_cost = 0 #Defines total_cost var
    
    for item in order: #Runs this loop for the things in the order
        item_index = menu.index(item) #the index() function gets the index number value of the current item
        total_cost += prices[item_index] #It finds the price value for the current index #, and returns that value to total cost.
    
    return total_cost #total_cost is returned to the vaiable in draw()

def add_to_order(item): #This adds an item to the order, the item parameter is what is actually added to the order list.
    order.append(item) #Appends the parameter to the order list.

def del_order(): #Removes the last item from the ordr
    if len(order) > 0: #Fixes the code crashing when poping an empty list
        order.pop() #If it passes the check, pops the last item from the order list.