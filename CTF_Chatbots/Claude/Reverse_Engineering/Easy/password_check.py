def check_password(password):
    correct_password = "secret123"
    if password == correct_password:
        return True
    return False

def main():
    password = input("Enter password: ")
    if check_password(password):
        print("Correct! Here's your flag: FLAG{reverse_engineering_basics}")
    else:
        print("Wrong password!")

if __name__ == "__main__":
    main()