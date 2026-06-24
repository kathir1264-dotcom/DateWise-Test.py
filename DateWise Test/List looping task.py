# #1. Write a Python program to print all elements of a list using a loop.
# n=[10,20,30,40,50]
# for i in n:
#     print (n)

# #2. Write a Python program to print only the even numbers from a list.
# n=[10,20,30,40,50,11,77]
# for i in n:
#     if i%2==0:
#         print(i)

# #3. Write a Python program to print only the odd numbers from a list.
# n=[12,11,20,3,6,9]
# for i in n:
#     if i%3==0:
#         print(i)

# #4. Write a Python program to find the sum of all numbers in a list.
# n=[653,634,789,124]
# sum=0
# for i in n:
#     sum+=1
# print(sum)

# #5. Write a Python program to find the largest number in a list using a loop.
# n=[153,789,269,475,871]
# largest=n[0]
# for i in n:
#     if i>largest:
#         largest=i
# print(largest)

# #6. Write a Python program to find the smallest number in a list using a loop.
# n=[153,789,269,475,871]
# smallest=n[0]
# for i in n:
#     if i<smallest:
#         smallest=i
# print(smallest)

# #7. Write a Python program to count how many positive numbers are in a list.
# n=[-2, -1, 0, 1, 2]
# count=0
# for i in n:
#     if i<=0:
#         count+=1
# print(count)

# #8. Write a Python program to count how many negative numbers are in a list.
# n=[-2, -1, 0, 1, 2]
# count=0
# for i in n:
#     if i>0:
#         count+=1
# print(count)

# #9. Write a Python program to reverse a list without using the .reverse() method.
# n=[12,23,15,16,78,94]
# for i in range(len(n)-1, -1, -1):
#     print(n[i])

# #10. Write a Python program to count how many even and odd numbers are present in a list.
# n=[1,2,12,18,45,67,89]
# count1=0
# count2=0
# for i in n:
#     if i%2==0:
#         count1+=1
#     elif i%2!=0:
#         count2+=1
# print(count1)
# print(count2)

# #11. Write a Python program to find and print the index of a specific value in a list.
# n=[12,25,36,54,5]
# value=int(input("enter the value:"))
# index=0
# for i in range(len(n)):
#     if n[i]==value:
#         print("The index of the given value in the list is:",i)
#         break
# else:
#     print("value not found")

# #12. Write a Python program to replace all negative numbers in a list with 0.
# n=[-7,-6,-5,-4,-3]
# for i in range(len(n)):
#     if n[i]<0:
#         n[i]=0
# print(n)

# #13. Write a Python program to print all numbers greater than 50 from a list.
# n=[49,50,51,52,53,115]
# for i in n:
#     if i>50:
#         print(i)

#14. Write a Python program to create a new list containing the squares of each element.
# n=(15,20,11,15,14)
# square=[]
# for i in n:
#     square.append(i**2)
# print(square)

# #15. Write a Python program to print all duplicate values in a list.
n=(12,50,15,15)
duplicate=[]
for i in n:
    if n.count(i)>1:
        print(i)



 
