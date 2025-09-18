# names = []

# for i in range(3): //crea una lista, por ejemplo si qiuero crear una lista del 0 al 100 (para no escribir del 0 al 100).
#     name = input("What's your name?: ")
#     print(f"{i}.Hello {name}")

# for i in range(3): 
#      names.append(input("What's your name?: "))
     
# for name in sorted(names):
#       print(f"Hello {name}")

name = input("What's your name?: ") #Aparece otra file:000 xd 
file = open("names.txt", "a") #"w" is to write in that other file // "a" to append.
file.write(f"{name}")
file.close()
