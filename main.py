password = input("Enter Password:")

for pswd in range(1):
    if((password[0].isupper()) == True):
        continue
    else:
        print("First Letter should be capital\nTry again")
        quit()

for pswd in range(len(password)):
    password = str(password)
    if(password.isalpha()==False):
        continue
    else:
        print("Password should contain atleast one number\nTry again")
        quit()

for pswd in range(1):
    if (password.isalnum()==True):
        print("Atleast one special character needed\nTry again")
        quit()
    else:
        continue

for pswd in range(1):
    if(len(password)>=6):
        continue
    else:
        print("Password length should be greater than six character\nTry again")
        quit() 

for a in range(3):
    pwsd = input("Renter Password :")
    b = 2
    if(pwsd == password):
        print("Password Matched\nLogin Success")
        break
    elif((b-a)==2):
        print("Password did not matched\nSecond last attempt")
        continue
    elif((b-a)==1):
        print("Final Attempt\nTry again")
        continue
    else:
        print("No password matched\nTry new password")
        break
