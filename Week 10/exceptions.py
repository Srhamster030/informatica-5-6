#error cometido por el programador:

#Syntax error: xd 
#print("Hello, world)



#VALUE ERROR:

# try:
#     x = int(input("What's x?: "))
#     print(f"x is equal to {x}")
# except ValueError:
#     print("x is not a number...")


def spam(divide_by):
    #way 1: try:
        return 42 / divide_by
    #way 1: except ZeroDivisionError:
        #way 1: print("Error: Invalid argument")
#way 2:try: 
    # print(spam(2))
    # print(spam(12))
    # print(spam(0))
    # print(spam(1))    
#way 2: except ZeroDivisionError:
    #way 2: print("Error: Invalid argument")



# while True:
#     try:
#         x = int(input("What's x?: ")) #//para "descomentar" xd, se usa "ctrl k+u".
#     except ValueError:
#         print("x is not a number...")
#     else:
#         break
# print(f"x is equal to {x}")



def read_small_integeer():
        while True:
            try:
                input_str = input("Please type an integeer: ")
                number = int(input_str)
                if number < 100 and number >= 0:
                    return number
            except ValueError:
                  pass
            print("This input is invlaid...")

number = read_small_integeer()
print(number, "to the power of three is: ", number**3 )
