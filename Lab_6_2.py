import re

def is_strong_password(password):    
    password_pattern = r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@#$%^&+=!])(.{8,})$'
    if re.match(password_pattern, password):
        return True
    else:
        return False


password = "anurAag787"

if is_strong_password(password):
    print("Password is strong.")
else:
    print("Password is not strong.")
