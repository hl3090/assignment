
word = input("Enter a word: ")
length = len(word)

if length < 3:
     print ("more than 3 letters")
elif word.endswith ("ing"):
    word += "ly"
else:
    word += "ing"        
    
print (word)    