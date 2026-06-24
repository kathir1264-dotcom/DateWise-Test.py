balance=int(input("Enter your balance: "))
amount=int(input("Enter the amount you want to withdraw: "))
pin=int(input("Enter your pin: "))
dbpin=1234
if (pin==dbpin):
    if (amount<=balance):
        if(amount%100==0):
            print("Collect your cash: ",amount)
            print("Your current balance is: ",balance-amount)
        else:
            print("Please enter the amount in multiples of 100")
    else:
        print("Insufficient balance")
else:
    print('invalid pin try again')

 