import random
import string

alphabet = {"a": 1,"b": 3,"c": 3,"d": 2,"e": 1,"f": 4,"g": 2,"h": 4,"i": 1,"j": 8,"k": 5,"l": 1,"m": 3,"n": 1,"o": 1,"p": 3,"q":10,"r": 1,"s": 1,"t": 1,"u":1,"v": 4,"w": 4,"x": 8,"y": 4,"z": 10}

print("Welcome to Scrabble")
print("Your letters are:")

user_letters = []
i = 0
while i < 13:
    user_letters.append(list(alphabet.keys())[random.randint(0,25)])
    i += 1
print(user_letters)

word = input("Enter a word with these letters: ")
o = 0
while o < 1:
    if word.upper()[o] in user_letters:
        print(word[o])
        o += 1

    else:
        print("wrong")
        o += 1

with open("dictionary.txt", "r") as file:
    lines = file.readlines()
dictwords = []
for line in lines:
    dictwords.append(line.replace("\n", ""))
if alphabet in dictwords:
    print("It's ok")
else:print("Not ok")
