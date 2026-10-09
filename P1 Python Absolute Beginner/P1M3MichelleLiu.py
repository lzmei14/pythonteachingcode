# [ ] create fucntion, call and test 
def cheese_order(max=100,min=5,price=2.99,order_amount=0):
    if order_amount > max:
        return str(order_amount) + " is more than currently available stock"
    elif order_amount < min:
        return str(order_amount) + " is below minimum order amount"
    else:
        total = order_amount * price
        return str(order_amount) + " costs $" + str(round(total,2))
    
name = input("Please enter your full name: ")
order_amount = float(input(name + ", enter your cheese order weight (numeric value): "))

print(cheese_order(order_amount=order_amount))