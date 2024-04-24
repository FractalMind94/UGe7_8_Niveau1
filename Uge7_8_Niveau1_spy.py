# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 11:29:22 2024

@author: KOM
"""

import pandas as pd
from datetime import datetime

class Item:
    def __init__(self, item_id, category_name, product_name, description, category_id, price, quantity):
        self.item_id = item_id
        self.category_name = category_name
        self.product_name = product_name
        self.description = description
        self.category_id = category_id
        self.price = price
        self.quantity = quantity

    def update_quantity(self, amount):
        self.quantity += amount

    def __str__(self):
        return f"{self.product_name} ({self.item_id}): {self.quantity} in stock"


class Category:
    def __init__(self, category_id, category_name, description):
        self.category_id = category_id
        self.category_name = category_name
        self.description = description

    def __str__(self):
        return f"{self.category_name} ({self.category_id})"


class Transaction:
    def __init__(self, transaction_id, item_id, date_time, amount, transaction_type):
        self.transaction_id = transaction_id
        self.item_id = item_id
        self.date_time = date_time
        self.amount = amount
        self.transaction_type = transaction_type

    def __str__(self):
        return f"Transaction ID: {self.transaction_id}, Item ID: {self.item_id}, Amount: {self.amount}, Type: {self.transaction_type}"


class Inventory:
    def __init__(self):
        self.items = []
        self.categories = []
        self.transactions = []
        self.df = pd.DataFrame(columns=["Category ID", "Category Name", "Product ID", "Product Name", "Description", "Price", "Quantity"])

    def add_item(self, item):
        self.items.append(item)
        self.df = pd.concat([self.df, pd.DataFrame({
            "Category ID": [item.category_id],
            "Category Name": [item.category_name],
            "Product ID": [item.item_id],
            "Product Name": [item.product_name],
            "Description": [item.description],
            "Price": [item.price],
            "Quantity": [item.quantity]
        })], ignore_index=True)

    def remove_item(self, item_id):
        self.items = [item for item in self.items if item.item_id != item_id]
        self.df = self.df.drop(self.df[self.df["Product ID"] == item_id].index)

    def update_item_quantity(self, item_id, amount):
        for item in self.items:
            if item.item_id == item_id:
                item.update_quantity(amount)
                break

    def search_item_by_id(self, item_id):
        for item in self.items:
            if item.item_id == item_id:
                return item
        return None
    
    def search_item_by_product_name(self, product_name):
        for product in self.items:
            if product.product_name == product_name:
                return product
        return None

    def generate_stock_report(self):
        return self.df

    def record_transaction(self, item_id, amount, transaction_type):
        transaction_id = len(self.transactions) + 1
        transaction = Transaction(transaction_id, item_id, datetime.now(), amount, transaction_type)
        self.transactions.append(transaction)

class Menu: #Not finished
    inventory_system = Inventory()
    while True:
        user = input("If product manager enter 1: ").strip()
        print("if buyer enter 2:")

        

        if user != 1 or 2:
            print("Invalid User ID - Try Again: ")
            continue
        
        while user == 1:
           
            print("---Manager Menu---")
            print("1. Look-up Product")
            print("2. Add product")
            print("3. Remove Product")
            print("4. View Stock Report")
            print("5. Exit")
            choice = input()
            
            if choice == "1":
                searched_product = inventory_system.search_item_by_product_name(input("search Product by Product Name:").strip())
                if searched_product:
                    print("Searched Item:", searched_product)
                else:
                    print("Item not found")
        
            elif choice == '2':
                   stock_report = inventory_system.generate_stock_report()
                   item =Item(input("Input category id, category name, Product id, Product Name, Price and Quantity in this order"))
                   inventory_system.add_item(item)
            elif choice == '3':
                pass
                
            elif choice == '4':
                pass
            elif choice == '5':
                break
            else:
                print("Invalid Number - Try Again:")
                continue
            
# Test the implementation
if __name__ == "__main__":
    # Create an inventory management system
    inventory_system = Inventory()

    # Add categories
    # category1 = Category(3, "Lol", "Lol")
    # category2 = Category(2, "Clothing", "Apparel and accessories")
    # inventory_system.categories.extend([category1])

    # Add items
    item1 = Item(1, 'Games', "Spider-Man 2", "PS5", 1, 500, 10)
    item2 = Item(2, "Apparel and accessories", "T-shirt", "Cotton t-shirt", 2, 150, 100)
    inventory_system.add_item(item1)
    inventory_system.add_item(item2)

    # Update item quantity
    # inventory_system.update_item_quantity(1, -5)  # Sold 5 laptops

    # Generate stock report
    stock_report = inventory_system.generate_stock_report()
    print(stock_report)

    # Search item by ID
    # searched_item = inventory_system.search_item_by_id(1)
    # if searched_item:
    #     print("Searched Item:", searched_item)
    # else:
    #     print("Item not found")
        
    # searched_product = inventory_system.search_item_by_product_name('Spider-Man 2')
    # if searched_product:
    #     print("Searched Item:", searched_product)
    # else:
    #     print("Item not found")

    # Export to Excel
    stock_report.to_excel("inventory.xlsx", index=False)
