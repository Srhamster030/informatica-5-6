def main():
    is_armed = False
    motion_detected = False
    door_open = False
    is_afternoon = False
    display_alarm(is_armed, motion_detected, door_open, is_afternoon)

def display_alarm(iar, ms, dop, an):
    if iar:
        if ms:
            print("WAWAWAWA, UN NEGRO D:!!!!!")
        if dop:
            print("door is open")
    else:
        if an:
            print("Welcome home! Turning lights on.")

            
main()