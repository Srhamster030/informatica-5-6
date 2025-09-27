birthdays = {
    "José": "19/05/2008",
    "Rodrigo": "10/09/2007",
    "Alexis": "13/12/2007"
}

name = input("Write a name: ")
if name in birthdays:
    print(birthdays[name])
  

else:
  print("I do not have information for",name,"...")
  new_name = input("Enter the new name: ")
  new_birthday = input("Enter the new birthday: ")
  birthdays[new_name] = new_birthday
  print("Okay!")
  print("setting infromation from", new_name)
  print(birthdays)


            

  


    

