import os
import time
import random
import string

# Constants
UPPER = string.ascii_uppercase
LOWER = string.ascii_lowercase
NUMBERS = '1234567890'
SYMBOLS = '~!@$%^&*()[]?/><'

def generate_password():
    """Generate a random password."""
    total =  UPPER + LOWER + NUMBERS + SYMBOLS
    password = "".join(random.sample(total, 16))
    return password

# Main loop
while True:
    print("\n[ WELCOME TO MY RANDOM PASSWORD GENERATOR TOOL ]")
    user_input = input("Random Password Generate (1.yes/2.no): ").lower()

    if user_input in ['yes', 'y', '1']:
        # Get file name and create file
        file_name = input("Give the Name of File: ") + ".txt"
        file_path = os.path.join('D:/', 'Passwords', file_name)

        # Generate password
        password = generate_password()
        print('_' * 50)
        print(f"Your password is >>> {password}")
        os.system(f'echo {password} | clip')
        print("Successfully copied to clipboard!")
        print('_' * 50)

        # Save password to file
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(f'Your passwd of {file_name.upper()} is >>> {password}')
            print(f"Your Passwd File of {file_name.upper()} is successfully saved!")

    else:
        # Exit the program
        print("Thanks for using it!")
        time.sleep(1)
        os.system('cls')
        break

    # Ask the user if they want to generate another password
    again = input("Do you want to generate another password? (y/n): ").lower()
    if again != 'y':
        print("Bye!")
        time.sleep(1)
        os.system('cls')
        break