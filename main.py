import re
from database import *
def password_check(password):
    """
    validate regex format from given password
    """
    # Regex pattern to match the criteria
    pattern = re.compile(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&=+_#^()])[A-Za-z\d@$!%*?&=+_#^()]{8,}$")
    # Check if the password matches the pattern
    if re.match(pattern, password):
        return True
    else:
        return False


while True:
    if check_key():
        print("Your key has been successfully imported \n\n")
    else:

        new_master_key(input("Enter master key password: "))

    ask = str(input("Enter (signup or login) to continue: "))
    username = str(input("Enter the username: "))
    password = str(input("Enter the password: "))

    if ask == "login":
        if password_check(password):
            print("Password is valid format")
            validate_password(username,password)

        else:
            print("password or username isn't match or password given isn't in password policy")

    elif ask == "signup":
        if password_check(password):
            print("Password is valid format")
            add_user("users",username,password)
            print(f"user: {username} with password: {password}. has been added")
        else:
            print("password given isn't in password policy or something went wrong")
