# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 09:56:40 2024

@author: KOM
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 11:29:22 2024

@author: KOM
"""

import pandas as pd
from datetime import datetime

class Item: # Paramaters for each item in inventory
    def __init__(self, category_id, category_name, product_name, description, product_id, price, quantity):
        self.category_id = category_id
        self.category_name = category_name
        self.product_id = product_id
        self.product_name = product_name
        self.description = description
        self.price = price
        self.quantity = quantity

    def update_quantity(self, amount):
        self.quantity += amount

    def __str__(self):
        return f"{self.product_name} ({self.product_id}): {self.quantity} in stock"


class Category:
    pass


class Transaction:
    pass


class Inventory:
    def __init__(self):
        self.items = []
        self.df = pd.DataFrame(columns=["Category ID", "Category Name", "Product ID", "Product Name", "Description", "Price", "Quantity"])
        
        
    def add_item(self, item):
        
        self.items.append(item)
        self.df = pd.concat([self.df, pd.DataFrame({
            "Category ID": [item.category_id],
            "Category Name": [item.category_name],
            "Product ID": [item.product_id],
            "Product Name": [item.product_name],
            "Description": [item.description],
            "Price": [item.price],
            "Quantity": [item.quantity]
        })], ignore_index=True)
        

    def remove_item(self, product_id):
        self.df = self.df.drop(self.df[self.df["Product ID"] == product_id].index)
        
        
    def update_item_quantity(self, product_id, amount):
        for item in self.items:
            if item.product_id == product_id:
                item.update_quantity(amount)
                # Update DataFrame
                self.df.loc[self.df['Product ID'] == product_id, 'Quantity'] += amount
                break

    def search_product_id(self, product_id):
        for item in self.items:
            if item.product_id == product_id:
                return item
        return None
    
    def search_product_name(self, product_name):
        for product in self.items:
            if product.product_name == product_name:
                return product
        return None

    def generate_stock_report(self):
        return self.df
    
    def record_transaction(self, transaction, buyer_id, price, amount, product_id, datetime): # record each transaction done by a buyer
        pass
            

if __name__ == "__main__":
    # Call Inventory system
    inventory_system = Inventory()
  
    #______________________________________________________________
    # Add items
    item1 = Item(1, 'Games', "Spider-Man 2", "PS5", 1, 500, 10)
    item2 = Item(2, "Clothing", "T-shirt", "Cotton t-shirt", 2, 150, 100)
    item3 = Item(3, "Clothing", "Pants", "Leather Pants", 3, 700, 100)
    inventory_system.add_item(item1)
    inventory_system.add_item(item2)
    inventory_system.add_item(item3)

    #______________________________________________________________________
    # Update item quantity    
    # inventory_system.update_item_quantity(1, -5) #update quantity by id
    # inventory_system.remove_item(2) #Remove by product id
    
    #_______________________________________________________________________
    # Generate stock report
    stock_report = inventory_system.generate_stock_report()
    print(stock_report)
    
    #________________________________________________________________________
    # Search item by ID
    # searched_item = inventory_system.search_product_id(1)
    # if searched_item:
    #     print("Searched Item:", searched_item)
    # else:
    #     print("Item not found")
    
    #_________________________________________________________________________
    # Search item by product name
    # searched_product = inventory_system.search_item('Spider-Man 2')
    # if searched_product:
    #     print("Searched Item:", searched_product)
    # else:
    #     print("Item not found")


#_______________________________________________________________________________________    
    

# =============================================================================
#  Forsoeg paa at tilfoeje en menu til koden, men da koden ikke virker helt 
#  efter hensigten, gav det ikke mening.
# =============================================================================

# class Menu:
#     inventory_system = Inventory()
#     while True:
#         user = input("If product manager enter 1: ").strip()
#         print("if buyer enter 2:")

        

#         if user != "1" or "2":
#             print("Invalid User ID - Try Again: ")
#             continue
        
#         while user == "1":
           
#             print("---Manager Menu---")
#             print("1. Look-up Product")
#             print("2. Add product")
#             print("3. Remove Product")
#             print("4. View Stock Report")
#             print("5. Exit")
#             choice = input()
            
#             if choice == "1":
#                 print("1. Search Item by item id")
#                 print("2. search Item by Product name")
#                 print("3. Exit")
#                 item_search = input("enter 1 or 2")
#                 if item_search == "1":
#                     searched_product = inventory_system.search_product_id(input("search Product by product id:"))
#                     if searched_product:
#                         print("Searched Item:", searched_product)
#                     else:
#                        print("Item not found")
#                 elif item_search =="2":
#                     searched_product = inventory_system.search_product_name(input("search Product by product id:"))
#                     if searched_product:
#                         print("Searched Item:", searched_product)
#                     else:
#                        print("Item not found")
#                 elif item_search == "3":
#                     break
#                 else:
#                     print("invalid input")
                    
#             elif choice == '2':
#                     stock_report = inventory_system.generate_stock_report()
#                     item =Item(input("Input category id, category name, Product id, Product Name, Price and Quantity in this order"))
#                     inventory_system.add_item(item)
#             elif choice == '3':
#                 pass
                
#             elif choice == '4':
#                 pass
#             elif choice == '5':
#                 break
#             else:
#                 print("Invalid Number - Try Again:")
#                 continue
            
#         while user == "2":
#             pass
