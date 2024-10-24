"""
Create a Python script that will generate a list of 1000 random numbers between 1 and 200. After the list is generated using either the collections of math library determine if there is a pattern to how the computer generates a random number.

Create a python script that simulates a vending machine. The user is presented with a list of options and the price. A user can then select one item to be "vended" to them. Use lists to keep track of the inventory. Each time a user makes a purchase log the sale to a text file called "VendLog.txt"
"""

inventory = {
    "chocolate": {"label": "A1", "price": 1.75, "quantity": 40},
    "cookies": {"label": "B1", "price": 0.50, "quantity": 40},
    "chips": {"label": "C1", "price": 0.75, "quantity": 40},
    "candy": {"label": "D1", "price": 1.00, "quantity": 40}
}

for i in inventory:
    print(inventory[i])


def vend_item(inventory, item):
    inventory[item]["quantity"] -= 1


while True:
    print(inventory)
    item = input("What would you like?")

    if item == "A1":
        print("Vending Chocolate, One moment please...\nChocolate Vended")
        vend_item(inventory, item)




