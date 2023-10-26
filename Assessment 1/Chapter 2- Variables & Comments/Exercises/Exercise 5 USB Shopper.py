#Define the cost of one USB stick and total budget
usb_cost = 6
total_budget = 50
#Calculate the maximum number of USB sticks she can buy
number_usb_sticks = total_budget // usb_cost
#Calculate the amount of money left after buying USB sticks
money_left = total_budget % usb_cost
#Print the results
print(f"she can buy {number_usb_sticks} USB sticks.")
print(f"she will have £{money_left} left.")