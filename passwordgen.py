import random
import string
#Task2: Password generator
def generate_password(length, include_uppercase=True, include_lowercase=True,
                      include_numbers=True, include_symbols=True):


  # Define character sets based on user options
  characters = ""
  if include_uppercase:
    characters += string.ascii_uppercase
  if include_lowercase:
    characters += string.ascii_lowercase
  if include_numbers:
    characters += string.digits
  if include_symbols:
    characters += string.punctuation

  # Validate character selection
  if not characters:
    raise ValueError("Please choose at least one character type (uppercase, lowercase, numbers, or symbols).")

  # Generate a random password
  password = ''.join(random.choice(characters) for _ in range(length))
  return password

while True:
  try:
    # Get user input for password length
    length = int(input("Enter the desired password length (minimum 8): "))
    if length < 8:
      raise ValueError("Password length must be at least 8 characters.")

    # Get user input for complexity options
    include_uppercase = input("Include uppercase letters (y/n)? ").lower() == "y"
    include_lowercase = input("Include lowercase letters (y/n)? ").lower() == "y"
    include_numbers = input("Include numbers (y/n)? ").lower() == "y"
    include_symbols = input("Include symbols (y/n)? ").lower() == "y"

    # Generate password
    password = generate_password(length, include_uppercase, include_lowercase, include_numbers, include_symbols)

    # Display password
    print(f"Your generated password is: {password}")

    # Ask user if they want to generate another password
    choice = input("Do you want to generate another password? (y/n): ")
    if choice.lower() != "y":
      break

  except ValueError as e:
    print(f"Error: {e}")

print("Thank you for using the password generator!")
