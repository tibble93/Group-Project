class ItemUnit:
    def __init__(self, unit_id: int, type_id: int, exp_date: str, source: str,
                 description: str, size: int):
        self.unit_id = unit_id
        self.type_id = type_id
        self.exp_date = exp_date
        self.source = source
        self.description = description
        self.size = size