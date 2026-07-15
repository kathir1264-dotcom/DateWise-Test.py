# #1. Given two lists, return the set of common elements that appear more than once in both lists.
# a={1,2,2,3,4,5}
# b={1,1,2,3,4}
# print(a.intersection(b))

# #2. Create a set of unique words from a sentence, where words are separated by spaces and punctuation marks should be ignored.
# input=input("enter a value")
# sentence=""
# for i in input:
#     if i.isalnum() or i.isspace():
#         sentence+=i
# num=set(sentence.split())
# print(num)

#3. Write a function that takes a list of numbers and returns the largest subset such that the sum of the subset is even.
# total=0
# set={10,11,567,3,6}
# for i in set:
#     total+=i
# print("evennum",set)
# smallest=100
# if total % 2 !=0 :
#     for i in set:
#         if i%2!=0 and i<smallest:
#          smallest=i
#     set.remove(smallest)
#     print(set)

#5. Check if two sets are equal, considering their elements but ignoring the order (i.e., set equality).
# a={10,20,30,50,60}
# b={10,20,30,50,60}
# if a==b:
#    print("sets are equal")
# else:
#     print("sets are not equal")

# #6. Write a program that finds the intersection of multiple sets.
# a={1,2,3,4}
# b={2,3,4}
# print(a.intersection(b))

# #14. Write a function to determine whether a set is a proper subset of another set.
# a={1,2,3}
# b={1,2,3,4}
# def subset(a,b):
#     if a<b:
#         print("proper subset of another set")
#     else:
#         print("not proper subset of another set")
# subset(a,b)

#20. Write a function that finds the union of all sets, but only includes elements that appear more than once across all sets.
a={1,2,3}
b={1,2,3,4}
c={1,2,3,4,5}
def union(a,b,c):
    result=set()
    for i in a | b | c:
        count = 0
        if i in a:
            count +=1
        if i in b:
            count +=1
        if i in c:
            count +=1
        if count>1:
            result.add(i)
    return(result)
print (union(a,b,c))