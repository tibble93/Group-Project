# We will utilize this script to manage our inventory system.
# The script will allow adding, removing, and viewing items in the inventory.
# Each item will have a name, quantity, and price.
# The inventory will be stored in a dictionary for easy access and manipulation.
# The script will also include functions to calculate the total value of the inventory.
#------------------------------------------------------------------------------------------
from itemType import ItemType 
from itemUnit import ItemUnit   

from data_management import load_data, save_data
from itemUnit import ItemUnit

class Inventory:
    def __init__(self):
        self.item_types = {}
        self.item_units = []
        self._load_from_storage()

    def _load_from_storage(self):
        data = load_data()
        for item_id, item in data.items():
            self.item_units.append(ItemUnit(
                item["unit_id"],
                item["type_id"],
                item["exp_date"],
                item["source"],
                item["description"],
                item["size"]
            )
        ) 
    
    def add_item_type(self, type_id, name, category):
        self.item_types[type_id] = ItemType(type_id, name, category)

    def add_item_unit(self, unit_id, type_id, exp_date, source, description, quantity):

        unit = ItemUnit(unit_id, type_id, exp_date, source, description, quantity)
        self.item_units.append(unit)
        self._save_to_storage()

    def _save_to_storage(self):
        data = {str(unit.unit_id): unit.to_dict() for unit in self.item_units}
        save_data(data)

    def remove_multiple_items(self, unit_ids):
        self.item_units = [
            unit for unit in self.item_units 
            if str(unit.unit_id) not in unit_ids]
        self._save_to_storage()

    def get_item_types(self):
        return self.item_types
    
    def get_item_units(self):
        return self.item_units
