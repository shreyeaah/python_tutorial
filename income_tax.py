salary = float(input("enter salary: "))

if salary <=300000:
    tax = 0
elif salary <=700000:
    tax = (salary-300000)*0.05
elif salary <= 1000000:
        tax = (400000 * 0.05) + (salary - 700000) * 0.1
elif salary <= 1200000:
        tax = (400000 * 0.05) + (300000 * 0.1) + (salary - 1000000) * 0.15   
elif salary <= 1500000:
        tax = (400000 * 0.05) + (300000 * 0.1) + (200000 * 0.15) + (salary - 1200000) * 0.2   
else:
        tax = (400000 * 0.05) + (300000 * 0.1) + (200000 * 0.15) + (300000 * 0.2) + (salary - 1500000) * 0.3

print("Total tax amount: ", tax)


    
