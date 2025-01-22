# Program Name: Lab1_Muntadher_Hezekiah.py
# Program Author: Muntadher Al-Bawi, Hezekiah Cua
# Date: 21-01-25
#
# Description: Develop a Python program that generates secure passwords based on user-defined
# criteria, such as length, number of letters, digits, and special characters.
from typing import LiteralString

import random
import string

# Function to get user input (skeleton)
def get_user_input(prompt, min_value, max_value):
    # Implement logic to get valid user input within a range
    pass

# Function to generate a password (skeleton)
def generate_password(length, num_letters, num_digits, num_specials):
    # Ensure total requested characters do not exceed length
    # Generate required characters (letters, digits, specials)

    # Generate a random letter
    random_letter = random.choice(string.ascii_letters)
    print(f"Random letter: {random_letter}")

    # Generate a random digit
    random_digit = random.choice(string.digits)
    print(f"Random digit: {random_digit}")

    # Generate a random special character
    random_special = random.choice(string.punctuation)
    print(f"Random special character: {random_special}")

    # Fill remaining characters
    # Shuffle and return password
    pass

# Main function (skeleton)
def main():
    print("\n--- Secure Password Generator ---\n")

    # Step 1: Get user inputs for password length and character distribution

    # Step 2: Validate user inputs

    # Step 3: Generate the password

    # Step 4: Display the generated password

    # Step 5: Save password to file

# Entry point of the script
if __name__ == "__main__":
    main()
