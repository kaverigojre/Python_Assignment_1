
special_characters = "!@#$%^&*()-+?_=,<>/"
def check_password_strength(password):
    if password.isupper() or password.lower == False:
        print("Password should contains both uppercase and lowercase letters")
    passwordlenghth = len(password)
    if passwordlenghth<8:
        print("The password should be at least 8 characters long")
    if any(i.isdigit() for i in password) == False:
        print("The password should contains at least one digit (0-9)")
    if any(s in special_characters for s in password)== False:
        print("The password should contains at least one special character (e.g., !, @, #, $, %) ")
    else:
        print ("Password Updated Successfully!!")  


check_password_strength("Testingpassword")
     



 



 