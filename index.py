
print("Welcome to the tip calculator.")
total_bill = float(input("What was the total bill? £"))
tip_amount = int(input("What % tip would you like to give, 10, 12, or 15? "))
no_of_people = int(input("How many people will split the bill? "))

total_with_tip = total_bill + (total_bill * round(tip_amount/100))

calculated_amount = round(total_with_tip / no_of_people, 2)

print(f"Each person should pay: £{calculated_amount}")

