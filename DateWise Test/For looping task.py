#print numbers from 1 to 10 using a for loop.
for i in range(1,11):
    print(i)

#Print the even numbers from 1 to 20 using a for loop.
for i in range(1,21): 
    if i % 2 == 0: 
        print(i)

#Print the odd numbers from 1 to 20 using a for loop.
for i in range(1,21):
    if i % 2 != 0:
        print(i)

#print numbers from 10 to 1 in reverse order.
for i in range(10,0,-1):
    print(i)

#print the square of each number from 1 to 10.
for i in range(1,11):
    print(i*i)

# print the multiples of 5 up to 50.
for i in range(1,51):
    if i % 5 == 0:
        print(i)

#find the sum of numbers from 1 to 10.
for i in range(1,11):
    sum = 0
    sum += i
    print(sum)

#find the sum of even numbers from 1 to 20.
for i in range(1,21):
    sum = 0
    if i % 2 == 0:
        sum += i
        print(sum)

#find the sum of odd numbers from 1 to 20.
for i in range(1,21):
    sum = 0
    if i % 2 !=0:
        sum +=i
        print(sum)

#print the multiplication table of 5.
x=7
for i in range(1,11):
    print(x, i, x*i)

#print numbers divisible by 3 from 1 to 30.
x=3
for i in range(1,31):
    if i % x == 0:
        print(i)

#find the factorial of 5 using a for loop.
x=5
for i in range(1,6):
    x*=i
print(x)

#print numbers from 1 to n (take any fixed n like 15).
n=15
for i in range(1,n+1):
    print(i)
