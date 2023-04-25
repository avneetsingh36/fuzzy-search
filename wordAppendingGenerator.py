# this file just appends words to your text file in case you want to generate some random words to play with

from random_word import RandomWords
import time

r = RandomWords()

while (True):
    with open("/Users/avneetsingh/Desktop/stuff/School Pitt/CODING/PYTHON/Saihaj Projects/22.08.31_searchfzzsort/md.txt", mode = 'a', encoding="utf-8") as myText:
        checkIfString = str(r.get_random_word())
        if type(checkIfString) == str:
            myText.write(checkIfString)
            myText.write(' ')
        time.sleep(5)
        
   
