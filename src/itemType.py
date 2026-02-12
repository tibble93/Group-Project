class ItemType:
    def __init__(self, type_id: int, name: str, category: str):
        self.type_id = type_id
        self.name = name
        self.category = category
        
    def to_dict(self):
        return {
            "type_id": self.type_id,
            "name": self.name,
            "category": self.category
        }
        