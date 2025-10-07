def character_counter(message, dictionary):
    for character in message:
        dictionary.setdefault(character, 0) #Si la letra está dos veces, la ignora y solo pone 1 en lugar de 0 y 2 en lugar de 1. 
        dictionary[character] += 1

    print(dictionary)
    print(sum(dictionary.values()))
    
#Alternative 1
    # values_list = list(dictionary.values())
    # # print(values_list)
    # largest_number_index = values_list.index(max(values_list)) #// we put .index to know in what number is the letra.// to return index
    # repeated_character = list(dictionary.keys())[largest_number_index]
    # print(f"The most repeated character is {repeated_character}, repeating {dictionary[repeated_character]} times.")

#Alternative 2
    largest_number2 = max(dictionary, key=dictionary.get)
    print(f"The most repeated character is {largest_number2}, repeating {dictionary[largest_number2]} times.")
        
message = input("Write a message: ")
dictionary = {}
character_counter(message, dictionary)

# character_counter(message, dictionary)

# print(f"The most repeated number is:{len(message)}")

#greater
