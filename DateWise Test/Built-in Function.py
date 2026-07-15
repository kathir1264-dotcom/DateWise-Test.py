#Python Practice Questions – map(), filter(), reduce()
#1. Double All Numbers
# a=[1,2,3,4,5]
# result=list(map(lambda x: x*2, a))
# print(result)

# #2. Square All Numbers
# a=[2,3,4,5]
# result=list(map(lambda x: x**2,a))
# print(result)

# #3.Convert Strings to Integers
# a=["10", "20", "30", "40"]
# def strings(a):
#     result= list(map(int, a))
#     return(result)
# print (strings(a))

# #4. Convert Names to Uppercase
# input=["john", "alice", "bob"]
# result=list(map(str.upper, input))
# print(result)

# #5. Find Length of Each Word
# a=["apple", "banana", "kiwi"]
# result=list(map(len,a))
# print(result)

# #6. Filter Even Numbers
# members=[1, 2, 3, 4, 5, 6]
# result=list(filter(lambda x: x%2==0, members))
# print(result)

# #7. Filter Odd Numbers
# members=[1, 2, 3, 4, 5, 6]
# result=list(filter(lambda x: x%2!=0, members))
# print(result)

# #8. Filter Positive Numbers
# a=[-5, -2, 0, 3, 8]
# result=tuple(filter(lambda x: x>0, a))
# print(result)

# # 9. Filter Words Longer Than 4 Characters
# a=["cat", "elephant", "dog", "tiger"]
# result=list(filter(lambda x: len(x)>4,a))
# print(result)

# #10. Extract Vowels from a String
# a="programming"
# result=list(filter(lambda x: x in"aeiou",a))
# print(result)

#11. Sum of All Numbers
from functools import reduce
# a=[1, 2, 3, 4, 5]
# result=(reduce(lambda x,y: x+y, a))
# print(result)

# #12. Product of All Numbers
# a=[1, 2, 3, 4]
# result=(reduce(lambda x,y: x*y,a))
# print(result)

# #13. Find Maximum Number
# a=[4, 10, 7, 25, 3]
# result=(reduce(lambda x,y: x if x>y else y,a ))
# print(result)

# #14. Find Minimum Number
# a=[4, 10, 7, 25, 3]
# result=(reduce(lambda x,y: x if x<y else y,a ))
# print(result)

# # 15. Join Words into a Sentence
# a=["Python", "is", "awesome"]
# result=(reduce(lambda x,y: x + " " + y, a))
# print(result)

# #16. Square Only Even Numbers
# a=[1, 2, 3, 4, 5, 6]
# result = list(map(lambda x: x**2, filter(lambda x: x % 2 == 0, a)))
# print(result)

# # #17. Sum of Even Numbers
# a=[1, 2, 3, 4, 5, 6]
# result=reduce(lambda x,y: x+y,filter(lambda z: z%2==0,a))
# print(result)

# #18. Count Words with Length Greater Than 3
# a=["cat", "apple", "dog", "banana"]
# result=list(filter(lambda x: len(x)>3,a))
# count=len(result)
# print(count)

# #19. Sum of Squares of Odd Numbers
# a=[1, 2, 3, 4, 5]
# result = reduce(lambda x, y: x + y, map(lambda x: x**2, filter(lambda x: x % 2 != 0, a)))
# print(result)

#20. Sum of Cubes of Even Numbers
a=[1, 2, 3, 4, 5, 6]
result = reduce(
    lambda x, y: x + y,
    map(
        lambda x: x ** 3,
        filter(lambda x: x % 2 == 0, a)
    )
)
print(result)








