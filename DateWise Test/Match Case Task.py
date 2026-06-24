#Even or Odd using match-case
num = int(input("Enter a number: "))
match num % 2:
    case True:
        print("Even Number")
    case False:
        print("Odd Number")

#number is *positive, negative, or zero*
num = int(input("Enter a number: "))
match num:
    case 0:
        print("Zero")
    case _ if num > 0:
        print("Positive Number")
    case _ if num < 0:
        print("Negative Number")

#simple calculator
n1=int(input("Enter first number: "))
n2=int(input("Enter second number: "))
op=input("Enter operator (+, -, *, /): ")
match op:
    case '+':
        print((n1+n2))
    case '-':
        print((n1-n2))
    case '*':
        print((n1*n2))
    case '/':
        print((n1/n2))

#weekday or weekend
day=(input("enter the day:"))
match day:
    case ("tuesday" | "saturday"):
        print("Weekend")
    case ("monday" | "wednesday" | "thursday" | "friday"):
        print("Weekday")

#grading system
grade=input("Enter grade (A, B, C, D, F): ")
match grade:
    case 'A':
        print("Excellent")
    case 'B':
        print("Good")
    case 'C':
        print("Average")
    case 'D':
        print("Pass")
    case 'F':
        print("Fail")

#month name
month=int(input("Enter month number (1-12): "))
match month:
    case 1:
        print("January")
    case 2:
        print("February")
    case 3:
        print("March")
    case 4:
        print("April")
    case 5:
        print("May")
    case 6:
        print("June")
    case 7:
        print("July")
    case 8:
        print("August")
    case 9:
        print("September")
    case 10:
        print("October")
    case 11:
        print("November")
    case 12:
        print("December")

#*traffic signal color
colour=input("Enter traffic signal color (red, yellow, green): ")
match colour:
    case "red":
        print("Stop")
    case "yellow":
        print("Ready")
    case "green":
        print("Go")

#age group
age=int(input("Enter age: "))
match age:
    case _ if age < 13:
        print("Child")
    case _ if 13 <= age < 20:
        print("Teen")
    case _ if 20 <= age < 60:
        print("Adult")
    case _ if age >= 60:
        print("Senior")

#between 1 and 10
num=int(input("Enter a number between 1 and 10: "))
match num:
    case _ if 1 <= num <= 10:
        print("Number is between 1 and 10")
    case _:
        print("Number is not between 1 and 10")

#username and password
username=input("Enter username: ")
password=input("Enter password: ")
match username:
    case _ if username == "admin" and password == "admin123":
        print("Login successful")
    case _:
        print("Invalid username or password")

#leap year
year=int(input("Enter a year: "))
match year:
    case _ if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print("Leap Year")
    case _:
        print("Not a Leap Year")

#vowel or consonant
letter=input("Enter a letter: ")
match letter:
    case 'a' | 'e' | 'i' | 'o' | 'u':
        print("Vowel")
    case _:
        print("Consonant")

#shape name
sides=int(input("Enter number of sides: "))
match sides:
    case 3:
        print("Triangle")
    case 4:
        print("Quadrilateral")
    case 5:
        print("Pentagon")
    case 6:
        print("Hexagon")
    case _:
        print("Shape not recognized")

#divisible by 3 and 5
num=int(input("Enter a number: "))
match num:
    case _ if num % 3 == 0 and num % 5 == 0:
        print("Divisible" \
        " by both 3 and 5")
    case _:
        print("Not divisible by both 3 and 5")

#