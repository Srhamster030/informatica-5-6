def main():
    b = input("Write an integrer number: ")
    if b % 3:
        print("Fizz ")
    if b % 5:
        print("Buzz ")
    elif b % 5 % 3:
        print("FizzBuzz! ")
    else: 
        print(b)
 
main()
