#Puneeth Suresh
#2107296@gscs.ca
#Assignment 24 - Word Cloud

#============ "setup" ============

size(500,500)


#================================== Data reading/manipulating vars and dictionaries ===================================

word_counts = {}

with open("words.txt", "r") as file: #Opens word.txt in read only mode (with basically opens a temporary session that handles cleaning up automatically)
    for l in file:  #Runs this loop for the amount of lines in "file"
        word = l.strip() #removes trailing and leading whitespace/newline, and adds the current line to the word var
        
        if word != "": #If the current line is blank, ignores it.
            if word in word_counts: #If the word already exists, adds a 1 to it's key-pair value
                word_counts[word] += 1
            else: #Otherwise, adds the word as a key to the dictionay, with a value of 1.
                word_counts[word] = 1
                

#====================================== Drawing the text ==========================

background(0)

fill(255) #makes the text white (since the default black wouln't work)

for word, count in word_counts.items(): #For loop for the amount of key-pair values (key var= word, pair var=count) in the word_count dictionary.
    if count >= 5: #If the pair for that word is over, it keeps going to place the word.
        text_size(count * 3) #Sets the text size to 3 times the count.
        
        x = random(0, width-10) #Sets x and y to a random value within the boundaries 
        y = random(0, height)

        text(word, x, y) #Places the text with the word, at the generated x and y values