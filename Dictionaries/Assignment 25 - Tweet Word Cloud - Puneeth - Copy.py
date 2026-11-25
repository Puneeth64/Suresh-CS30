#Puneeth Suresh
#2107296@gscs.ca
#Assignment 25 - Tweet Word Cloud

#============ "setup" ============

size(500, 500)


#================================== Data reading/manipulating vars and dictionaries ===================================

word_counts = {}

ignore_words = ["the", "a", "an", "i", "me", "you", "with", "this", "that", "what", "to", "too", "in", "it", "is", "if", "are", "am", "and", "for", "so", "but"] #List of words to ignore (all lowercase for now)

with open("tweets.txt", "r") as file:  #Opens tweets.txt in read-only mode
    for l in file:  #Loops through each line in the file
        words = l.strip().split()  #Removes trailing/leading whitespace and splits the sentence into a list of words
        
        for w in words:  #Loops through each individual word in the tweet
            word = w.lower()  #Lowercases the word, so capitalization doesn't create duplicates
            
            if word != "" and word not in ignore_words: #Checks that the word is not blank and also not in ignore list
                if word in word_counts:  #If the word already exists, add 1 to its count
                    word_counts[word] += 1
                else:  #Otherwise, add the word to the dictionary with a count of 1
                    word_counts[word] = 1


#====================================== Drawing the text ==========================

background(0) #Makes BG black
fill(255)  #Makes the text white

for word, count in word_counts.items(): #Runs this loop for the number of key-pairs in word_counts dictionary
    if count >= 5:  #Only draws words that appear 5 or more times
        text_size(count * 3)  #Text size is 3 times the amount of times it appears
        
        x = random(0, width - 20) #Randomely chooses an x and y coord that fits within the canvas. 20 minused from the x, so it doesn't go too off screen
        y = random(0, height)
        
        text(word, x, y) #Places the current iteration's word at the randomely generated x,y coords