#Empty
userEmail='userEmail@gmail.com'
PassWord='123456'
Email=input("Enter your email: ")
Password=input("Enter your Password: ")
if Email!="empty" and Password!="empty":
    if Email==userEmail:
        if Password==PassWord:
            print("login successful")
        else:
            print("invaild password")
    else:
        print("invaild email")
else: 
    print("login failed")
