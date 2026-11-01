# Self Assessment Questions

# 1.

# Coming from Java, I expected lists to work like arrays with a fixed size, so I was surprised that `append()` and `remove()` let a list grow and shrink whenever I want.
# I was also surprised that negative indexes like `inventory[-1]` grab items from the end of the list.

# 2.

# At my old job, I tracked ingredients by hand and had to redo the calculations every time quantities changed.
# A Python list would have let me store and update the ingredients with methods like `append()` and `remove()`, saving time and cutting down on math mistakes.

#Exercise 1

inventory = ["pen", "notebook", "stapler", "tape", "marker" ]
print(inventory)
print(len(inventory))

#Exercise 2

print((inventory[0]))
print((inventory[-1]))
print((inventory[2]))    

#Exercise 3

print(inventory[0:3])
print(inventory[3:5])
print(inventory[0::2])

#Exercise 4

inventory.append("envelope")
inventory.remove("tape")
inventory.sort()
print(inventory)

#Exercise 5

coords = (40.7128, -74.0060)
#coords [0] = 99

#The error recieved states that tuples are immutable meaning they cannot be changed after they are created.
#In this case, they are useful because coordinates shouldn't be changed after they are created to ensure the location is accurate.

#Exercise 6

sales = (100, 250, 75, 480, 200)
avg = sum(sales) / len(sales)
print(sum(sales))
print(avg)
print(max(sales))
print(min(sales))

#Exercise 7

prices = [9.99, 14.99, 4.99, 24.99, 1.99]

discounted_prices = [round(price * 0.9, 2) for price in prices]
print(prices)
print(discounted_prices)

#Exercise 8

sales = [340, 127, 589, 204, 467, 88, 731, 315, 62, 490]
high_sales = [sale for sale in sales if sale > 300]
avg_sales = sum(high_sales) / len(high_sales)
print(high_sales)
print(len(high_sales))
print(round(avg_sales, 2))