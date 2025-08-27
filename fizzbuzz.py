def main():
    b = input("Write an integrer number: ")
    if b % 3 == 0:
        print("Fizz ")
    if b % 5 == 0:
        print("Buzz ")
    elif b % 5 == 0 and b % 3 == 0:
        print("FizzBuzz! ")
    else: 
        print(b)

main()
