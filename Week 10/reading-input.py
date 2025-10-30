def main():
  number = read_input("Please type in a number: ", 5, 10)  #Define the funcions with 3 parameters
  print("You typed in:", number)

def read_input(prompt, small, large): # Insert missing parameters
  while True:   
    try:
      x = int(input(prompt))
      if 5 < x < 10:
        return x
      else:
        print("Please type a number BETWEEN" , small, "and", large)
    except ValueError:
      print("Please type a number between", small, "and", large)

main()