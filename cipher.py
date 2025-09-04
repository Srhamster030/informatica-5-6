def main():
    b = input("Write something: ").lower
    encode_message(b)

def encode_message(text):
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        sipher = "zyxwvutsrqponmlkjihgfedcba"
        new_message = ""
        i = 0

        while i < len(text):
            char = text [i]
              
main()
