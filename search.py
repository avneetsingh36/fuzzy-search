# IMPORTANT VARIABLES
from posixpath import split
from tkinter import Y
from lib import ending
from colorama import Fore
from colorama import Style



preSplitpreLower = ''
instanceCounter = 0
misSpelled = 0
posAdd = -1
posSub = -1

linenumber = 0

userSearch = input("\nType the phrase/word you looking for: ")
print()
userInputLower = userSearch



with open("/Users/rest/of/path", mode = 'r', encoding="utf-8") as myText:
    storing = myText.readlines()
for i in storing:
    preSplitpreLower = preSplitpreLower + i
preSplit = preSplitpreLower
splitText = preSplit.split()


print("If found, the phrase that is or contains the word inside it will be highlighted.")
userConfirm = input("Type okay to continue: ")


for i in range(len(splitText)):
    pos = splitText[i].find(userInputLower)
    pos2 = splitText[i].find(userSearch.capitalize())
    if len(userInputLower) > 5 and pos == -1 and pos2 == -1:
        posAdd = splitText[i].find(userInputLower[1:(len(userInputLower))])
        posSub = splitText[i].find(userInputLower[0:((len(userInputLower)-1))])
    if pos >= 0 or pos2 >= 0 or posAdd >= 0 or posSub >= 0:
        if posAdd >= 0 or posSub >= 0:
            misSpelled += 1
        instanceCounter += 1
        if i > 0 and i < len(splitText)-1:
            print(f'Time it was referenced: {instanceCounter}{ending(instanceCounter)} | Was found in the phrase: "{splitText[i - 1]} {Fore.BLUE}{splitText[i]}{Style.RESET_ALL} {splitText[i + 1]}"')
        elif i == len(splitText)-1:
            print(f'Time it was referenced: {instanceCounter}{ending(instanceCounter)} | Was found in the phrase: "{splitText[i - 2]} {splitText[i - 1]} {Fore.BLUE}{splitText[i]}{Style.RESET_ALL}"')
        else:
            print(f'Time it was referenced: {instanceCounter}{ending(instanceCounter)} | Was found in the phrase: "{Fore.BLUE}{splitText[i]}{Style.RESET_ALL} {splitText[i + 1]} {splitText[i + 2]}"')

if misSpelled > 0:
    print(f"\nYOU MAY HAVE A TYPO IN YOUR SEARCH!")

print(f'\nTotal times that the phrase "{userSearch}" was mentioned: {instanceCounter}\n')



choiceToSeeAll = input("Would you like to see it in a whole body of text: ")
print()
if choiceToSeeAll.lower() == 'y' or choiceToSeeAll.lower() == 'yes':
    splitPreLower = preSplitpreLower.split()
    for i in range(len(splitPreLower)):
        pos = splitPreLower[i].find(userInputLower)
        pos2 = splitPreLower[i].find(userInputLower.capitalize())
        if pos >= 0 or pos2 >= 0:
            print(f'{Fore.BLUE}{splitPreLower[i]}{Style.RESET_ALL} ', end='')
        else:
            print(f'{splitPreLower[i]} ', end='')
else:
    print("Have a good day.")
