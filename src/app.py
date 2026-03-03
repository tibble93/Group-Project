# This is the main application file for the inventory management system.
# It will integrate the inventory management and data handling functionalities.
# The application will provide a user interface to interact with the inventory. 
#------------------------------------------------------------------------------------------
# Import necessary modules
from flask import Flask, render_template
from flask import request, redirect, url_for

from inventory import Inventory 
#from data_management import DataManagement 
from itemType import ItemType #Import the ItemType class from the itemType module made by Andrew
from itemUnit import ItemUnit #Import the ItemUnit class from the itemUnit module made by Andrew

from flask import session
from functools import wraps
from werkzeug.security import generate_password_hash, check_password_hash


#python src/app.py
#Initialize the Flask application
#the app variable is an instance of the Flask class
app = Flask(__name__)

#Set a secret key for session management. I chose to use a simple string for this project. 
app.secret_key = "project_password"

USERS = {
    "admin": "food1234"
}

def login_required(view):
    @wraps(view)
    def wrapped_view(*args, **kwargs):
        if 'user' not in session:
            return redirect(url_for('login'))
        return view(*args, **kwargs)
    return wrapped_view

inventory = Inventory()

#These are purely placeholder items
inventory.add_item_type(1, "Canned Beans", "Food")
inventory.add_item_type(2, "Rice", "Food")
inventory.add_item_type(3, "Peanut Butter", "Food")
inventory.add_item_type(4, "Tuna", "Food")
inventory.add_item_type(5, "Bottled Water", "Beverage")
inventory.add_item_type(6, "Toilet Paper", "Household")


 #Create an instance of the Inventory class to manage our inventory data 

#Define routes for the web application
# ("/") represents the home page of the application
# When a user accesses the home page, the index function is called
#The index function renders the "index.html" template

#This is the login route that handles both GET and POST requests.
@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username in USERS and USERS[username] == password:
            session['user'] = username
            return redirect(url_for('view_inventory'))
        else:
            return "Invalid login. Please try again."

    return render_template('login.html')



#This route handles user logout by clearing the session and redirecting to the login page.
@app.route("/logout")
def logout():
    session.pop('user', None)
    return redirect(url_for('login'))




@app.route("/")
def index():
    return render_template("index.html")

@app.route("/inventory")
@login_required
def view_inventory():
    return render_template(
        "inventory.html",
        item_units=inventory.get_item_units(),
        item_types=inventory.get_item_types()
    )


@app.route("/add", methods=['POST'])
@login_required
def add_item():
    name = request.form["name"]
    category = request.form["category"]
    exp_date = request.form["exp_date"]
    source = request.form["source"]
    quantity = int(request.form["quantity"])

    type_id = len(inventory.item_types) + 1
    inventory.add_item_type(type_id, name, category)

    unit_id = len(inventory.item_units) + 1
    inventory.add_item_unit(
        unit_id,
        type_id,
        exp_date,
        source,
        name,
        quantity
    )

    return redirect(url_for("view_inventory"))

@app.route("/remove_items", methods=['POST'])
@login_required
def remove_items():
    selected_items = request.form.getlist("selected_items")

    if selected_items:
        inventory.remove_multiple_items(selected_items)

    

    return redirect(url_for("view_inventory"))

@app.route("/update")
@login_required
def update_item():
    return "Update Item Page under construction"

#This block ensures that the application runs only if this script is executed directly
if __name__ == '__main__':
    app.run(debug=True) 