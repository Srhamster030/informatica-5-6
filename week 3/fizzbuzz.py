def main():
    b = int(input("Write an integrer number: "))
    if b % 5 == 0 and b % 3 == 0:
        print("FizzBuzz! ")
    
    elif b % 3 == 0:
        print("Fizz ")
        
    elif b % 5 == 0:
        print("Buzz ")
    
    else: 
        print(b, ">:c")

main()
