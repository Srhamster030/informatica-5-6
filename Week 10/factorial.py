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


# x = int(input("Type a positive integer: "))
# fact = 1
# for d in range(1,x +1 ):
#     fact *= d
#     while True:
#         print(f"The factoral of {x} is: ", fact)
#     if x < 0:
#         print("Type a POSITVE number!")
#     else:
#         retrun 

print("Type a positive integer:")
x = int(input())
fact = 1
if x > 0:
    for i in range(1, x + 1):
        fact *= i
    print("The factorial of", x ,"is: ", fact)
else:
    print("ERROR")
