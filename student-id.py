def main():
	print('')
	print('Please enter the following information to create your ID Card.')
	input('Press enter to continue.')
	ask_student_info()
	display_student_info()

def ask_student_info():
    fname = input("First name: ").title()
    input("Last name: ").capitalize()
    input("Email adress: ").upper()
    input("Phone number: ").replace("*")
	
def display_student_info():
	print(fname)
	print("Your ID card is: ")
	line = "-" * 45
	print(line)
	print()
	
main()