import json

# Task 1: Read the inventory 
with open('inventory.json', 'r') as file:
    inventory = json.load(file)
print(f"Total items in inventory: {len(inventory)}")

# Add New Book
new_book = {
    "title": "Atomic Habits", 
    "author": "James Clear", 
    "price": 14.99, 
    "in_stock": True
 }

# Task 2: Update and save the inventory
titles = [book['title'] for book in inventory]
if new_book['title'] not in titles:
    inventory.append(new_book)
    
print("New book added to inventory and saved successfully.")

# Task 3: Display the inventory
print("\nUpdated Inventory:")
with open('inventory.json','r') as file:
    updated_inventory = json.load(file)
for book in updated_inventory:
    print(f"Title: {book['title']} | Author: {book['author']} | Price: ${book['price']}")