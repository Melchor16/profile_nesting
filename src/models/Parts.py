class Part:
    def __init__(self, item: int, length: float, qty: int, profile: str):
        self.item = item
        self.length = length
        self.qty = qty
        self.profile = profile

    @classmethod
    def from_row(cls, row):
        return cls(
            int(row["item"]),
            float(row["length"]),
            int(row["qty"]),
            str(row["profile"]),
        )
    def clone(self):
        return Part(self.item, self.length, 1, self.profile)