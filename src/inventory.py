# We will utilize this script to manage our inventory system.
# The script will allow adding, removing, and viewing items in the inventory.
# Each item will have a name, quantity, and price.
# The inventory will be stored in a dictionary for easy access and manipulation.
# The script will also include functions to calculate the total value of the inventory.
#------------------------------------------------------------------------------------------
from itemType import ItemType 
from itemUnit import ItemUnit   

class Inventory:
    def __init__(self):
        self.item_types = {}
        self.item_units = []    
    
    def add_item_type(self, type_id, name, category):
        self.item_types[type_id] = ItemType(type_id, name, category)

    def add_item_unit(self, unit_id, type_id, exp_date, source, description, quantity):

        unit = ItemUnit(unit_id, type_id, exp_date, source, description, quantity)
        self.item_units.append(unit)

    def get_item_types(self):
        return self.item_types
    
    def get_item_units(self):
        return self.item_units
