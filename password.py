import random
alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$&"
pwsd_len = 9
pwsd = ""

choice = int(input("Generate Password By\n1.Manual Method\n2.Random Method\nEnter Your Choice:"))

if (choice == 1):
    print("\nEnter Password that Contains:")
    print("1.Capital First Letter")
    print("2.Size Greater than 6")
    print("3.Atleast 1 special character and 1 Number")

    password = input("\n\tEnter Password:")

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
            quit()
        elif((b-a)==2):
            print("Password did not matched\nSecond last attempt")
            continue
        elif((b-a)==1):
            print("Final Attempt\nTry again")
            continue
        else:
            print("No password matched\nTry new password")
            break

else:
    for i in range(pwsd_len):
        next_index = random.randrange(len(alphabets))
        pwsd = pwsd + alphabets[next_index]
	

print(pwsd)
pswd = (input("Renter Password Given Above"))
if (pwsd == pswd):
    print("Login Success")
else:
    print("Password Incorrect\nTry Generating New Password")
