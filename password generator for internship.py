import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("your safe Password Generator")
    print("-------------------")

    try:
        length = int(input("Enter the length of the password you want: "))
        if length <= 0:
            raise ValueError("Password length should be greater than zero.")
    except ValueError as e:
        print(f"Error: {e}")
        return

    # Generate and display the password
    password = generate_password(length)
    print("\nGenerated Password is:")
    print(password)

if __name__ == "__main__":
    main()
