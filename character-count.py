def character_counter(message, dictionary):
    for character in message:
        dictionary.setdefault(character, 0) #Si la letra está dos veces, la ignora y solo pone 1 en lugar de 0 y 2 en lugar de 1. 
        dictionary[character] += 1

    print(dictionary)
    
message = input("Write a message: ")
dictionary = {}
character_counter(message, dictionary)

print(f"The most repeated number is:{len(message)}")
        