#1. Write a program to count the number of vowels in a given string.
n=input("Enter a string: ")
count=0
for char in n:
    if char.upper() in 'AEIOU':
        count+=1
    else: pass
print("Number of vowels in the string: ", count)

#2. Write a program to reverse a string using a loop (without using slicing).
n=input("Enter a string: ")
reversed_string=""
for char in n:
    reversed_string=char+reversed_string
print("Reversed string: ", reversed_string)

#3. Write a program to check if a string is a palindrome using a loop.
n=input("Enter a string: ")
reverse_text=""
for char in n:
    reverse_text=char+reverse_text
if n==reverse_text:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")

#4. Write a program to count the number of uppercase and lowercase letters in a string.
n=input("Enter a string: ")
uppercase_count = 0
lowercase_count = 0
for char in n:
    if char.isupper():
        uppercase_count+=1
    elif char.islower():
        lowercase_count+=1
    else: pass
print("Uppercase letters:", uppercase_count)
print("Lowercase letters:", lowercase_count)

#5. Write a program to remove all spaces from a string without using built-in replace().
n=input("Enter a string: ")
count = ""
for char in n:
    if char != " ":
        count += char
print("String without spaces:", count)

#6. Write a program to find the frequency of each character in a string.
n=input("Enter a string: ")
count = ""
for i in n:
    if i not in count:
        print(i, ":", n.count(i))
        count += i

#7. Write a program to count how many digits are present in a string.
n=input("Enter a string: ")
digit_count = 0
for char in n:
    if char.isdigit():
        digit_count+=1
    else: pass
print("Number of digits in the string: ", digit_count)

#8. Write a program to check if a string contains only alphabetic characters (without using isalpha()).
n=input("Enter a string: ")
k=True
for i in n:
    if not ('A'<=i<='Z'or'a'<=i<='z'):
        k=False
if k:
    print("The string contains only alphabetic characters.")
else:
    print("The string contains non-alphabetic characters.")

#9. Write a program to convert all lowercase letters in a string to uppercase manually using ASCII values.
n=input("Enter a string: ")
if n.islower():
    result=""
    for i in n:
        result+=chr(ord(i)-32)
    print("Uppercase string: ", result)

#10. Write a program to print all characters located at even indices of a string.
n = input("Enter a string: ")
for i in range(len(n)):
    if i % 2 == 0:
        print(n[i])

# 11. Write a program to count the number of words in a string without using split()
n = input("Enter a string: ")
count = 0
for i in range(len(n)):
    if n[i] != ' ' and (i == 0 or n[i-1] == ' '):
        count += 1
print("Number of words:", count)

#12. Write a program to replace all vowels in a string with * using a loop.
n = input("Enter a string: ")
result = ""
for ch in n:
    if ch in "aeiouAEIOU":
        result += "*"
    else:
        result += ch
print("Modified string:", result)

#13. Write a program to find the longest word in a sentence.
n = input("Enter a sentence: ")
words = StopIteration.split()
longest = words[0]
for word in words:
    if len(word) > len(longest):
        longest = word
print("Longest word:", longest)
print("Length:", len(longest))

#14. Write a program to check whether two strings are anagrams of each other using loops.
N="silent"
M="listen"
a=x.lower()
b=y.lower()
anagram=True
if len(a) != len(b):
    anagram=False
else:
    for i in a:
        if a.count(i) != b.count(i):
            anagram=False
            break
if anagram:
    print("The strings are anagrams.")
else:
    print("The strings are not anagrams.")

#15.Write a program to count how many special characters are present in a string.
x=input("Enter first word: ")
count=0
for i in x:
    if not i.isalnum() and i!=" ":
        count+=1
print("Number of special characters in the string: ", count)

#16. Write a program to print each character of a string a given number of times.
n=input("Enter a string: ")
k=int(input("Enter the number of times to print each character: "))
for i in n:
    print(i * k, end="")

#17.Write a program to remove duplicate characters from a string using loops.
n=input("Enter a string: ")
r=''
for i in n:
    if i not in r:
        r+=i
print("String without duplicate characters:", r)

#18. Write a program to count the number of consonants in a given string.
n=input("Enter a string: ")
count=0
for i in n:
    if i  not in 'AEIOUaeiou':
        count+=1
print("Number of consonants in the string: ", count)

#19. Write a program to capitalize the first letter of a string manually (without using capitalize()).
n=input("Enter a string: ")
print(n[0].upper() + n[1:])

#20.Write a program to print characters of a string until a vowel is encountered.
n=input("Enter a string: ")
result=0
for i in n:  
    if i in 'aeiou':
        result+=1
print("Characters until a vowel is encountered: ", result)