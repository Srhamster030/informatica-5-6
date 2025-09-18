# names = []

# for i in range(3): //crea una lista, por ejemplo si qiuero crear una lista del 0 al 100 (para no escribir del 0 al 100).
#     name = input("What's your name?: ")
#     print(f"{i}.Hello {name}")

# for i in range(3): 
#      names.append(input("What's your name?: "))
     
# for name in sorted(names):
#       print(f"Hello {name}")

# name = input("What's your name?: ") #Aparece otra file:000 xd 
# file = open("names.txt", "a") #"w" is to write in that other file // "a" to append.
# file.write(f"{name}")
# file.close()

# with open("names.txt", "a") as file: //the same but with two lines less xd.
#     file.write(f"{input("What's your name?")}")

with open("names.txt", "r") as file: #allows you to see the text in the file.
    lines = file.readlines()

# for line in lines:
#     print(f"Hello {line.rstrip()}")

for line in sorted(lines):
    print(f"Hello {line.strip()}")



