#funtion that gets key as input and returns value
#load json file and print output

import json

data = json.load(open("data.json"))

def translate(word):
    return data[word]

word = input("Enter word: ")

print(translate(word))