from datetime import date,time,datetime
#date calculator
# def DOB():
#     date=int(input("Enter your date: "))
#     month=int(input("Enter your month: "))
#     year=int(input("Enter your year: "))
#     today=datetime.today()
#     currentage = today.year-year
#     print("current age:", currentage)
# DOB()

# #days calculator
# def age():
#     date=int(input("Enter your date: "))
#     month=int(input("Enter your month: "))
#     years=int(input("Enter your year: "))
#     day_s=datetime(years,month,date)
#     today=datetime.today()
#     total=(today-day_s).days
#     print(total)
# age()

#1. Countdown timer
#Create a program that takes a future date and calculates:
# Days remaining
# Hours remaining
# Minutes remaining

# def count():
#     days=int(input("enter the days:"))
#     hours=int(input("enter the hours:"))
#     mins=int(input("enter the mins:"))
#     future_Date=datetime(mins,hours,days)
#     Today=datetime.today()
#     total_Days= (future_Date-Today).days
#     total_hours=(future_Date-Today).seconds//3600
#     total_mins=((future_Date-Today).seconds%3600)//60
#     print(total_Days)
#     print(total_hours)
#     print(total_mins)
# count()

#2. Calculate someone's next birthday
# Input:
# Enter birth date: 2005-09-15

# def count():
#     date=int(input("enter the date:"))
#     month=int(input("enter the month:"))
#     year=int(input("enter the year:"))
#     birthday=datetime(year, month, date)
#     today=datetime.today()
#     next_Bday=datetime(today.year,month,date)
#     Total_Days=(next_Bday-today).days
#     print("Your next birthday is in",Total_Days,"days")
# count()

#3. Working hours calculator
# Given:
# Start time: 09:30
# End time: 17:45
# Calculate:
# Total working hours: 8 hours 15 minutes

def count():
    start_Time=(input("enter the time:"))
    end_time=(input("enter the time:"))

    start=datetime.strptime(start_Time, "%H:%M")
    end = datetime.strptime(end_time, "%H:%M")

    difference = end - start

    hours = difference.seconds // 3600
    minutes = (difference.seconds % 3600) // 60

    print("Total working hours:",hours,minutes)
count()