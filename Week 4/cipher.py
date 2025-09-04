def main():
    message = input("Write something: ").lower() #define the variable and ask to input a message.
    encode_message(message) #define the function.

def encode_message(message): #define the variable and put the limit that is the input.
    alphabet = "abcdefghijklmnopqrstuvwxyz" #defining the variable.
    cipher = "zyxwvutsrqponmlkjihgfedcba" #defining the variable but backwards to enocode.
    new_message = "" #empthy to store the input.
    i = 0 #define in which number will start. 

    while i < len(message): #made a loop and meassure the length of the input.
        char = message [i] #to count the characters.

        if char in alphabet: #telling the program that if the character is in the alphabet do:
            cipher_index = alphabet.find(char) #
            new_message += cipher[cipher_index]
        else:
            new_message += char
        i += 1
    print("Encoded message: " + new_message)
              
main()
