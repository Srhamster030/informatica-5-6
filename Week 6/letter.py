def main():
    receiver = ["Mario", "Luigi", "Daisy", "Yoshi", "Toad", "Princess Peach", "Bowser"]
    receiver.remove("Princess Peach")
    for sender in receiver:
        invitation(sender)

def invitation(b):
    print(f"""
    +~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~+
       Dear {b}
    
       You are cordially invited to a ball at
       Peach's Castle this evening, 7:00 PM.

       Sincerely,
        Princess Peach
    +~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~+ 
    """)
main()