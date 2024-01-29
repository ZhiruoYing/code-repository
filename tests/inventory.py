# Inventory Management System

# The inventory is stored in a dictionary.
# Keys are item names and values are quantities.
inventory = {}

# Function to add an item to the inventory

#input item和quantity应该在函数外面,不应该在函数里面

def add_item(item, quantity):
    if item in inventory:
        used_quantity=float(inventory.get(item))
        inventory[item]=quantity+used_quantity
    else:
        inventory[item]=quantity
    return(f"{quantity} {item}(s) have been added.")#应该在if-else语句外面
    # Implementation Instructions:
    # 1. Check if the item exists in the inventory dictionary.
    # 2. If it does, increase its quantity.
    # 3. If not, add the item to the inventory with the given quantity.
# Function to view all items in the inventory

#应该遍历函数不能直接打印

def view_inventory():
        for item,quantity in inventory.items():
             print(f"{item}:{quantity}")
  # Implementation Instructions:
    # 1. Loop through the inventory dictionary.
    # 2. Print each item's name and its quantity.

# Function to update the quantity of an existing item in the inventory
def update_item(item, quantity):
    if item in inventory:
         inventory[item]=quantity
    else:
         print("Not Found")
    # Implementation Instructions:
    # 1. Check if the item exists in the inventory.
    # 2. If it does, update its quantity.
    # 3. If the item doesn't exist, print a message indicating it's not found.

# Main function to manage the inventory
def manage_inventory():
    while True:
        print("\nInventory Management System")
        print("1. Add Item")
        print("2. View Inventory")
        print("3. Update Item Quantity")
        print("4. Exit")
        choice = input("Enter choice (1/2/3/4): ")

        if choice =="1":
             item=input("input item:")
             quantity=float(input("input quantity:"))
             print(add_item(item, quantity))
        elif choice =="2":
             print(view_inventory())
        elif choice =="3":
             item=input("input item:")
             quantity=float(input("input quantity:"))
             print(update_item(item, quantity))
        elif choice=="4":
             print("Exit")
             break
        else:
             print( "an error message")
             


#应该用print这样程序才会一直执行，不然就退出了

        # Process the user's choice
        # Implementation Instructions:
        # 1. If the choice is '1', prompt the user to enter an item name and quantity,
        #    and then call the add_item function.
        # 2. If the choice is '2', call the view_inventory function.
        # 3. If the choice is '3', prompt the user to enter an item name and new quantity,
        #    and then call the update_item function.
        # 4. If the choice is '4', break the loop to exit the program.
        # 5. For any other input, display an error message.

manage_inventory()

# Entry point of the program
if __name__ == "__main__":
    manage_inventory()
