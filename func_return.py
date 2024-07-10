def validate_user(username, password):
    if username.lower() == "emc" and password.lower() == "123":
        return True
    else:
        return False

username = input("enter username ")
password = input("enter password ")
print(validate_user(username, password))