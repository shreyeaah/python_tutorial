
number = int(input("Enter number: "))


if number < 0:
    print("Square root of a negative number is not a real number.")
else:
    z = 1
    err = abs(number - (z * z))
    while err > 1.0e-20:
        z = (z + (number / z)) / 2
        err = abs(number - (z * z))

    print("Square root is: ", z)


