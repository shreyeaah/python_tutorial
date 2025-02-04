lst = []  
n = int(input("Enter number of elements: "))  

for i in range(n):  
    num = int(input(f"Enter element {i + 1}: "))  
    lst.append(num)  

lst.sort()  
print(f"Largest element is : {lst[-1]}, Smallest  element is : {lst[0]}")
