#1. Write a program to divide two numbers using try and except.
try:
    a=float(input("enter a number:"))
    b=float(input("enter a number:"))

    solution=a/b
    print(solution)

except ZeroDivisionError:
    print("error cannot divisible by Zero")

except ValueError:
    print("error ValueError")

finally:
    print("execute the value")

#2. Write a program that divides two numbers. Print "Division successful" only if no exception occurs.
try:
    a=int(input("enter a number:"))
    b=int(input("enter a number:"))
    result=a/b

except ZeroDivisionError:
    print("error cannot divisible by Zero")

except ValueError:
    print("error ValueError")

else:
    print("Result:", result)
    print("Division successful")

finally:
    print("execute the value")

#3. Divide two numbers and print "Execution completed" regardless of whether an exception occurs.
try:
    a=int(input("enter a number:"))
    b=int(input("enter a number:"))
    result=a/b

except ZeroDivisionError:
    print("error cannot divisible by Zero")

except ValueError:
    print("error ValueError")

else:
    print("Result:", result)
    print("Division successful")

finally:
    print("Execution completed")

4. Create a calculator (+, -, *, /) using try and except.
try:
    a=float(input("enter a number:"))
    symbols=(input("enter a symbols(+,-,*,/):"))
    b=float(input("enter a number:"))
    if symbols=="+":
        print('result:', a+b)
    elif symbols=="-":
        print('result:', a-b)
    elif symbols=="*":
        print('result:', a*b)
    elif symbols == "/":
        print("Result:", a / b)
    else:
        print("Invalid operator.")

except ZeroDivisionError:
    print("error cannot divisible by Zero")

except ValueError:
    print("error ValueError")

finally:
    print("Execution completed")

#5. Read numbers from the user until they enter valid integers.
while True:
    try:
        a=int(input("enter a number:"))
        b=int(input("enter a number:"))
        break
    except ValueError:
        print("Error: Please enter valid integers.")
print("First Number:", a)
print("Second Number:", b)

6.Handle IndexError while accessing list elements.
try:
    numbers = [10, 20, 30, 40, 50]
    index = int(input("Enter the index: "))
    print("Element:", numbers[index])

except IndexError:
    print("Error: Index out of range.")

except ValueError:
    print("Error: Please enter a valid integer.")

7.Handle KeyError when accessing a dictionary key.
try:
    a={"place":"puducherry"}
    key=str(input("Enter the place: "))
    print("place:",a[key])

except KeyError:
    print("Error: key not found.")

else:
    print("coversion successful")

finally:
    print("Execution completed")

#8.Handle TypeError by attempting to add an integer and a string.
try:
    a={"place":"puducherry"}
    key=str(input("Enter the place: "))
    print("place:",a[key])

except TypeError:
    print("Error: incorrect.")

else:
    print("coversion successful")

finally:
    print("Execution completed")