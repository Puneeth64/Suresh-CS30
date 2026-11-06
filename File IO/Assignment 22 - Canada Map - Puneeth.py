#Puneeth Suresh
#2107296@gscs.ca
#Assignment 22 - Canada Map


city_names = []  # Stores city names as strings
city_pops = []   # Stores city populations as integers
city_x = []     # Stores x-coordinates as integers
city_y = []     # Stores y-coordinates as integers

map_img = ""


def load_city_data(filename): #reads the pop txt file, parses it and puts the data into indiviudal lists.
    
    file = open(filename, "r")
    all_lines = file.readlines()  #Reads all the lines, and puts it as a continuours string (all_lines would end up aving 18 lines)


    for i in range(len(all_lines)):
        clean_line = all_lines[i].strip()  #Removes the newline characters, using .strip, which remves leading/trailing whitespace.
        
        row_values = clean_line.split(",")  #Splits string by the comma
           
        name = row_values[0].strip() #Pulls each value out of the string using the string's equivalent of an index, and puts that into the appropraite var.
        city_pop = int(row_values[1].strip())
        x = int(row_values[2].strip())
        y = int(row_values[3].strip())
        
        city_names.append(name) #All the lists have the current line's appropriate vars appended to the list.
        city_pops.append(city_pop) #ex. if i=2, this would be 758515 for winnepeg (the 2nd thing in the txt file)
        city_x.append(x)
        city_y.append(y)
        
    file.close()  #Safely closes the file once it has read it




def draw_cities(): #Draws the pop and names of every city
    
    for i in range(len(city_names)): #for the current iterations city data, it creates the pop circles, and the names
        name = city_names[i]
        city_pop = city_pops[i]
        x = city_x[i]
        y = city_y[i]

        diameter = (city_pop ** 0.5) * 0.05 #Calculutes the appropriate circle size for the population (these values where found with trail and error)
        diameter = max(diameter, 2)  #Minimum size so small pops are still somewhat visible

        no_stroke()
        fill(255, 0, 0, 180)  #Red coloud for circle
        circle(x, y, diameter) #Draws the pop circle at the appropriate x,y, with the above calculated diameter.

        fill(0, 0, 255) #Fills the text blue

        if name == "St. John's": #If it is st.johns, flips it to the right so it doesn't go out of the screen
            text_align(RIGHT, CENTER)
            text(name, x - 10, y)
        else:
            text_align(LEFT, CENTER) #Text is rendered with the name var @x,y (with a slight offset so that it's somewhat beside the circle)
            text(name, x + 5, y)


def setup(): #Creates the canvas, loads the txt file, and loads the map data
    global map_img
    size(800, 800)
    
    load_city_data("popdata.txt")
    
    map_img = load_image("Canada_provinces_blank.png")
    
def draw(): #Renders the city pop circles, the text, and the map img.
    global map_img
    
    draw_cities() #Calls the function that draws the pop circles and the text.
    
    image(map_img, 0, 0, 800, 800) #Renders the map image; top left corner @ (0,0) with the height/width fixed at 800x800px
    
    no_loop()  #Prevents it from looping, since it only needs a single iteration to draw all the data.