import getpass

def main():
    password = getpass.getpass("Set a password: ")
    input("Press enter to log in.")
    check_password(password)


def check_password(p):
    guess = input("Enter password: ")
    if p == guess:
        print("Correct password!")
    print("The program has ended.")

main()