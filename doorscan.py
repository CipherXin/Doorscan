# Automatic Door
# using facial recognition

import time

def open_door():
    print("Opening door...")
    time.sleep(4)
    print("Door opened, Enter")

def face_scan():
    print("Scanning...")
    time.sleep(3)
    print("Scan Complete")

def close_door():
    print("Door Closing...")
    time.sleep(3)
    print("Door Closed")

def main():
    while True:
        print("To Open Door; press 'o' "
              "To Close Door; press 'c' "
              "To Quit; press 'q' ")

        action = input("Enter 'o' to open door.")

        if action == 'o':
            open_door()
            face_scan()
        elif action == 'c':
            close_door()
        elif action == 'q':
            print("Exiting")

        else:
            print("Invalid Input. Please try again.")

if __name__ == "__main__":
    main()


