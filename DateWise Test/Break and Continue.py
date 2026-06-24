#1) Write a Python program to print numbers from 1 to 20 and stop when the number reaches 10 using break.
for i in range(1, 21):
    if i == 10:
        break
    print(i)

#2) Write a Python program to print numbers from 1 to 15 except 8 using continue.
for i in range(1,16):
    if i == 8:
        continue
    print(i)

#3) Write a Python program to print numbers from 1 to 50 and stop when the first multiple of 7 greater than 20 is found.
for i in range(1, 51):
    if i > 20 and i % 7 == 0:
        break
    print(i)

#4) Write a Python program to print all odd numbers from 1 to 30 by skipping even numbers.
for i in range(1,31):
    if i%2==0:
     continue
    print(i)

#5)Write a Python program to keep adding natural numbers starting from 1 and stop when the sum exceeds 100.
n=0
for i in range(1, 100):
    n = n + i
    if n > 100:
        break
print("n =", n)

#6)Write a Python program to print numbers from 1 to 25 except the multiples of 3.
for i in range(1,26):
    if i%3==0:
        continue
    print(i)

#7) Write a Python program to print the multiplication table of 5 and stop after 5 × 7.
for i in range(1, 11):
    if i > 7:
        break
    print("5 x", i, "=", 5 * i)

#8) Write a Python program to print numbers from 1 to 100 and stop when the first number divisible by 11 is found.
for i in range(1,101):
    print(i)
    if i%11==0:
     break

#9) Write a Python program to print numbers from 1 to 20 while skipping all even numbers.
for i in range(1,21):
    if i%2==0:
        continue
    print(i)

#10) Write a Python program to print numbers from 1 to 50 and skip all numbers ending with the digit 5.
for i in range(1,51):
    if i%10==5:
        continue
    print(i)

#11) Write a Python program to find the first prime number greater than 50 and stop after finding it.
for i in range(50, 100):
    if i==53:
        break
    print(i)

#12) Write a Python program to print numbers from 1 to 30 except those divisible by 2 or 3.
for i in range(1,31):
    if i%2==0 or i%3==0:
        continue
    print(i)

#13) Write a Python program to print the characters of a string and stop when the character 'x' is encountered.
for i in ('abcdefghijklmnopqrstuvxyz'):
    print(i)
    if i=='x':
     break

#14) Write a Python program to print all characters of a string except vowels.
for i in ('kathir'):
    if i in'aeiou':
       continue
    print (i)

#15)Write a Python program to print all characters of a sentence except spaces.
for i in ('i love python'):
    if i==' ':
        continue
    print(i)

#16) Write a Python program to count vowels in a string and stop counting when a space is encountered.
count = 0
for i in "kathir is a boy":
    if i == ' ':
        break
    if i in 'aeiou':
        count += 1
print(count)

#17) Write a Python program to print only uppercase letters from a given string.
for i in "Kathir can't Done Without me":
    if i.isupper():
        print(i)

#18) Write a Python program to print only lowercase letters from a given string by skipping uppercase letters.
for i in 'Nothing can Stop me':
    if i.islower():
        print(i)
    if i.isupper():
        continue

#19) Write a Python program to read numbers from the user continuously and stop when 0 is entered.
for i in (1,2,3,4,5,6,7,0):
    if i==0:
        break
    print(i)

#20) Write a Python program to allow only three password attempts and stop when the correct password is entered.
for i in range(3):
    if i>3:
        break
    if i==0:
        print(i)


        

        
       
       



    

