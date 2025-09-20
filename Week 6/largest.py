def main():        
    length = int(input("Enter the length of a list: "))
    number_list = []
    for i in range(2):
        length = int(input("Enter the length of a list: "))
        number_list.append(length)
    print(number_list)

    length = int(input("Enter the length of a list: "))
    file = open("largest.txt", "w") 
    file.write(f"{length}")
    file.close()
            
main()