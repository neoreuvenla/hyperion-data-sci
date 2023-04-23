# task 12 - lists and dictionaries
# calculates the value of held stock using both lists and dictionaries

menu = ["Bacon", "Sausage", "Egg", "Tomato"]                       # items sold
stock = {"Bacon": 16, "Sausage": 33, "Egg": 24, "Tomato": 12}      # item stock
price = {"Bacon": 0.3, "Sausage": 0.9, "Egg": 0.2, "Tomato": 0.1}  # item price

total_stock = 0  # inital stock value set to 0 prior to calculation

for item in menu:  # loops through eaach item in the menu
    
    # multiplies the item stock held by the item price
    item_value = stock[item] * price[item]

    # updates the running total with the calculated item value
    total_stock += item_value  

# prints the result calculated in the previous loop
print("The total value of currently held stock is £{:.2f}".format(total_stock))
