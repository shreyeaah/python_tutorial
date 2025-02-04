amount = float(input("Enter the amount invested: "))
year = int(input("Enter the time period (in years): "))
interest_rate = float(input("Enter the rate of interest: "))


total_interest = (amount * year * interest_rate) / 100
total_amount = amount + total_interest


print(f"\nTotal Interest: {total_interest:.2f}")
print(f"Total Amount: {total_amount:.2f}\n")


print(f"{'Year':<10}{'Interest':<15}{'Total Amount':<15}")
print("-" * 40)


for current_year in range(1, year + 1):
    yearly_interest = (amount * current_year * interest_rate) / 100
    yearly_amount = amount + yearly_interest
    print(f"{current_year:<10}{yearly_interest:<15.2f}{yearly_amount:<15.2f}")
