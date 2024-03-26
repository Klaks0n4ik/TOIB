import string
import random

def generate_password(length=8):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

if __name__ == "__main__":
    length = int(input("Enter desired password length (default is 8): "))
    length = length if length > 0 else 8
    password = generate_password(length)
    print("Generated password:", password)