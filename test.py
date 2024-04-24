# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 11:01:27 2024

@author: KOM
"""

import pandas as pd
from datetime import datetime

class Item:
    def __init__(self, item_id, name, description, category_id, price, quantity):
        self.item_id = item_id
        self.name = name
        self.description = description
        self.category_id = category_id
        self.price = price
        self.quantity = quantity

    def update_quantity(self, amount):
        self.quantity += amount

    def __str__(self):
        return f"{self.name} ({self.item_id}): {self.quantity} in stock"


class Category:
    def __init__(self, category_id, name, description):
        self.category_id = category_id
        self.name = name
        self.description = description

    def __str__(self):
        return f"{self.name} ({self.category_id})"


class Transaction:
    def __init__(self, transaction_id, item_id, date_time, amount, transaction_type):
        self.transaction_id = transaction_id
        self.item_id = item_id
        self.date_time = date_time
        self.amount = amount
        self.transaction_type = transaction_type

    def __str__(self):
        return f"Transaction ID: {self.transaction_id}, Item ID: {self.item_id}, Amount: {self.amount}, Type: {self.transaction_type}"


class InventoryManagementSystem:
    def __init__(self):
        self.items = []
        self.categories = []
        self.transactions = []
        self.df = pd.DataFrame(columns=["Category ID", "Category Name", "Product ID", "Product Name", "Description", "Price"])

    def add_item(self, item):
        self.items._append(item)
        self.df = self.df._append({
            "Category ID": item.category_id,
            "Category Name": "",
            "Product ID": item.item_id,
            "Product Name": item.name,
            "Description": item.description,
            "Price": item.price
        }, ignore_index=True)

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

    def generate_stock_report(self):
        return self.df

    def record_transaction(self, item_id, amount, transaction_type):
        transaction_id = len(self.transactions) + 1
        transaction = Transaction(transaction_id, item_id, datetime.now(), amount, transaction_type)
        self.transactions._append(transaction)


# Test the implementation
if __name__ == "__main__":
    # Create an inventory management system
    inventory_system = InventoryManagementSystem()

    # Add categories
    category1 = Category(1, "Electronics", "Electronic gadgets")
    category2 = Category(2, "Clothing", "Apparel and accessories")
    inventory_system.categories.extend([category1, category2])

    # Add items
    item1 = Item(1, "Laptop", "High-performance laptop", 1, 1500, 10)
    item2 = Item(2, "T-shirt", "Cotton t-shirt", 2, 20, 100)
    inventory_system.add_item(item1)
    inventory_system.add_item(item2)

    # Update item quantity
    inventory_system.update_item_quantity(1, -5)  # Sold 5 laptops

    # Generate stock report
    stock_report = inventory_system.generate_stock_report()
    print(stock_report)

    # Search item by ID
    searched_item = inventory_system.search_item_by_id(1)
    if searched_item:
        print("Searched Item:", searched_item)
    else:
        print("Item not found")

    # Export to Excel
    stock_report.to_excel("inventory.xlsx", index=False)