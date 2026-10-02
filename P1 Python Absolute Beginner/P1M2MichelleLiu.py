full_name = "Michelle Liu"

def fishstore(fish, price):
    return "Report for " + full_name + ". Fish Type: " + fish + " costs $" + price

fish_entry = input("Enter the fish type: ").title()
price_entry = input("Enter the fish price: ")

print(fishstore(fish_entry,price_entry))
