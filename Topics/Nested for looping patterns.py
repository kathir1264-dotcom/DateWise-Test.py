 #Right-Angled Triangle Pattern in Python
rows = int(input("Enter the row size for the pattern: "))
for i in range(0, rows):  
    for j in range(0, i + 1): 
        print("*", end=" ") 
    print()
#Inverted Right-Angled Triangle Pattern in Python
rows = int(input("Enter the row size for the pattern: "))
for i in range(rows, 0, -1):  
    for j in range(0, i): 
        print("*", end=" ") 
    print()
#Pyramid Pattern in Python
rows = int(input("Enter the row size for the pattern: "))