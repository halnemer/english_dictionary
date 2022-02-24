import json
from difflib import get_close_matches

def dictionary(word):
    word = word.lower()
    if word in data:
        result = data[word]
        out(result)
    elif len(get_close_matches(word, data.keys())) > 0:
        Q = input("did you mean \"%s\"? Enter Y if yes, enter N if no: " % get_close_matches(word, data.keys())[0])
        if Q == "Y":
            result = data[get_close_matches(word, data.keys())[0]]
            out(result)
        elif Q == "N":
            print("This word is not exist in this dictionary. ")
        else:
            print("Sorry ... We didnt understand your comannd")
    else:
        print("this word is not exist in this dictionary. ")

def out(result):
    for item in result:
        print(item)
    print()

data = json.load(open("data.json"))

while True:
    word = input("Enter word you wanna search about it ... (Enter Q to exit from the program): ")
    if word.lower() == "q":
        break
    dictionary(word)