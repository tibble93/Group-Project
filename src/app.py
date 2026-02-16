# This is the main application file for the inventory management system.
# It will integrate the inventory management and data handling functionalities.
# The application will provide a user interface to interact with the inventory. 
#------------------------------------------------------------------------------------------
# Import necessary modules
from flask import Flask, render_template

from inventory import Inventory 
#from data_management import DataManagement 
from itemType import ItemType #Import the ItemType class from the itemType module made by Andrew
from itemUnit import ItemUnit #Import the ItemUnit class from the itemUnit module made by Andrew


#python src/app.py
#Initialize the Flask application
#the app variable is an instance of the Flask class
app = Flask(__name__)

inventory = Inventory()


inventory.add_item_type(1, "Canned Beans", "Food")
inventory.add_item_type(2, "Rice", "Food")

inventory.add_item_unit(1, 1, "2024-12-31", "Donation", "Canned Beans from local food drive", 100)
inventory.add_item_unit(2, 2, "2025-01-31", "Purchase", "Rice purchased from supplier", 200)    

 #Create an instance of the Inventory class to manage our inventory data 

#Define routes for the web application
# ("/") represents the home page of the application
# When a user accesses the home page, the index function is called
#The index function renders the "index.html" template
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/inventory")
def view_inventory():
    return render_template(
        "inventory.html",
        item_units=inventory.get_item_units(),
        item_types=inventory.get_item_types()
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