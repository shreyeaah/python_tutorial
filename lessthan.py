lst = []  
n = int(input("Enter number of elements: "))  

for i in range(n):  
    num = int(input(f"Enter element {i + 1}: "))  
    lst.append(num)  

num = int(input("Enter number to compare: "))  

less_than_list = []  
for i in lst:  
    if i < num:  
        less_than_list.append(i)  

print(f"Numbers less than {num} are: {less_than_list}")
