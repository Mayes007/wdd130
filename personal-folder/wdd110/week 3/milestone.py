#python

#prices

child_meal_price=4.50
print(f"What is the price of a child's meal? {child_meal_price}  ")
adult_meal_price=9.00
print(f"What is the price of an adult meal? {adult_meal_price}  ")

#number of guests
number_children=4
print(f"How many children are there? {number_children} ")
number_adults=2
print(f"How many adults are there? {number_adults}")

#sales tax rate
sales_tax_rate=6
print(f"What is the sales tax rate? {sales_tax_rate}")
#calculate subtotal
subtotal=(child_meal_price*number_children) + (adult_meal_price*number_adults)

#calulate sales tax
sales_tax=(sales_tax_rate/ 100)* subtotal

#calculate total
total=subtotal+sales_tax

#payment amount
payment_amount=40.00
print(f"What is the payment amount? {payment_amount}")

#calculate change
change=payment_amount-total

#print the results
print("Subtotal: ${:.2f}".format(subtotal))
print("Sales Tax: ${:.2f}".format(sales_tax))
print("Total: ${:.2f}".format(total))
print("Payment Amount: ${:.2f}".format(payment_amount))
print("Change: ${:.2f}".format(change))

