import random
import string

def generate_password(length, use_uppercase, use_digits, use_special):
    # Base character set: lowercase letters
    characters = string.ascii_lowercase
    
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_digits:
        characters += string.digits
    if use_special:
        characters += string.punctuation
    
    if not characters:
        print("No character sets selected! Please choose at least one.")
        return ""
    
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Welcome to the Password Generator!")
    
    try:
        length = int(input("Enter the desired password length: "))
        use_uppercase = input("Include uppercase letters? (yes/no): ").strip().lower() == 'yes'
        use_digits = input("Include digits? (yes/no): ").strip().lower() == 'yes'
        use_special = input("Include special characters? (yes/no): ").strip().lower() == 'yes'
        
        password = generate_password(length, use_uppercase, use_digits, use_special)
        if password:
            print(f"Generated Password: {password}")
    except ValueError:
        print("Invalid input. Please enter a valid number for the password length.")

if __name__ == "__main__":
    main()