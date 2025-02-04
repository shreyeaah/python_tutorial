numbers = []
count = int(input("Enter number of elements in the list:"))

for i in range(count):
    numbers.append(int(input(f"Enter element {i + 1}:")))

print("Input List:", numbers)

top_three = []
for num in numbers:
    if len(top_three) < 3:
        top_three.append(num)
        top_three.sort()
    else:
        if num > top_three[0]:
            top_three[0] = num
            top_three.sort()

print(f"The third largest element is {top_three[0]}.")
