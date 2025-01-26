# Program Name: Lab1_Muntadher_Hezekiah.py
# Program Author: Muntadher Al-Bawi, Hezekiah Cua
# Date: 21-01-25

# Description: Develop a Python program that generates secure passwords based on user-defined
# criteria, such as length, number of letters, digits, and special characters.

# Import the necessary modules to generate random values
import random
# Import string to get the characters for the program
import string

# Defining the Functions to make the flow of the program work

# This get_user_input function prompts the user input and validates it
def get_user_input(prompt, min_value, max_value):
    # We use the try except to validate if the inputs are integers
    try:
        value = int(input(prompt))
        # If the value the user entered is between the minimum value and the max value
        # It will return the value
        if min_value <= value <= max_value:
            return value
        # But if the user enters a value that is less than or more than the min and max
        # It delivers an error message and tells the user to enter a valid input
        else:
            print(f"Please enter a value between {min_value} and {max_value}.")
    except ValueError:
        print("Invalid input; please enter a valid number.")
        # If the user enters an invalid input
        # The function then delivers an error message and asks the user to input a number
    return get_user_input(prompt, min_value, max_value)  # Recursive call if validation fails

# The generate_password function generates a password containing the three types of characters
def generate_password(length, num_letters, num_digits, num_specials):
    if num_letters + num_digits + num_specials > length:
        print("Error: The sum of specified characters exceeds the total password length.")
        return None  # Ensure total requested characters do not exceed length

    # Generate the required letters, digits and special characters
    # if the total sum is less than the total length, fill in the gaps with letters
    letters = random.choices(string.ascii_letters, k=num_letters)
    digits = random.choices(string.digits, k=num_digits)
    specials = random.choices(string.punctuation, k=num_specials)
    remaining = length - (num_letters + num_digits + num_specials)
    others = random.choices(string.ascii_letters, k=remaining)  # Fill remaining with letters

    # Create password list and put all the generated characters
    password_list = letters + digits + specials + others
    # Shuffle the llist to have a stronger password
    random.shuffle(password_list)

    # Join the password list into a string to form the final password
    return ''.join(password_list)

# The main function is where the program starts to run
def main():
    # Display a welcome message that indicates
    # that the password generator has started
    print("\n--- Secure Password Generator ---\n")
    # The program now prompts the user to input
    # This includes the password's length, number of letters, digits, and special characters
    total_length = get_user_input("Enter the total length of the password: ", 8, 20)
    num_letters = get_user_input("Enter the number of letters in the password: ", 0, total_length)
    num_digits = get_user_input("Enter the number of digits in the password: ", 0, total_length - num_letters)
    num_specials = get_user_input("Enter the number of special characters: ", 0, total_length - num_letters - num_digits)

    # After the program prompts the user for the password length and other details
    # The program now calls the generate_password function to generate the password
    # based on the user's inputs
    password = generate_password(total_length, num_letters, num_digits, num_specials)
    # If the total number of characters exceeds the total
    # length of the password, it will not proceed and will deliver an error message
    if password is None:
        # The program will exit if it can't generate the password
        return

    # If the password is generated, the program will display the password
    print(f"\nGenerated Password: {password}")

    # Then it gets saved to a file
    with open("password.txt", "w") as file:
        file.write(password)
    print("Password saved to 'password.txt'.")

if __name__ == "__main__":
    main()