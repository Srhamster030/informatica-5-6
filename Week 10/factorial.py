# def divide(a,b):
#     if b == 0:
#         raise ValueError("Hey! You cannot divide by zero.")
#     return a / b

# print(divide(1,2))
# print(divide(2,0))
#////////////////////////////////////////////////////////////////////
# def main():
#     x = (int(input("Type a positive integer: ")))
#     print(f"{x}! = {factorial(x)}")

# def factorial():

def main():
    while True:
        x = int(input("Type a positive integer: "))

        if x > 1:
            print(f"{x}! = {(x)}")            
        else:
            print("Type a positive number.")
            return(x)
main()