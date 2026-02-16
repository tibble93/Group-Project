# This is the main application file for the inventory management system.
# It will integrate the inventory management and data handling functionalities.
# The application will provide a user interface to interact with the inventory. 
#------------------------------------------------------------------------------------------
# Import necessary modules
from flask import Flask, render_template

import inventory
from itemType import ItemType #Import the ItemType class from the itemType module made by Andrew
from itemUnit import ItemUnit #Import the ItemUnit class from the itemUnit module made by Andrew



#python src/app.py
#Initialize the Flask application
#the app variable is an instance of the Flask class
app = Flask(__name__)

#Define routes for the web application
# ("/") represents the home page of the application
# When a user accesses the home page, the index function is called
#The index function renders the "index.html" template
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/inventory")
def view_inventory():
    item_types = {
        1: ItemType(1, "Apples", "Food"),
        2: ItemType(2, "Blanket", "Clothing"),
        3: ItemType(3, "Canned Beans", "Food"),
        4: ItemType(4, "Water Bottles", "Beverages" )
    }

    item_units = [
        ItemUnit(101, 1, "12/31/2025", "Donation", "Apples bag", 100),
        ItemUnit(102, 2, "N/A", "Community Drive", "Winter blanket", 20),
        ItemUnit(103, 3, "12/31/2024", "Donation", "Canned beans box", 50),
        ItemUnit(104, 4, "5/24/2027", "Donation", "Water bottles pack", 200)
    ]   

    return render_template(
        "inventory.html",
        item_units=item_units,
        item_types=item_types
    )
@app.route("/remove")
def remove_item():
    return "Remove Item Page under construction"

@app.route("/add")
def add_item():
    return "Add New Item Page under construction"

@app.route("/update")
def update_item():
    return "Update Item Page under construction"

#This block ensures that the application runs only if this script is executed directly
if __name__ == '__main__':
    app.run(debug=True) 