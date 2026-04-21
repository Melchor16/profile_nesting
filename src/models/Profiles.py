class Profile:
    def __init__(self, name: str, length: float):
        self.name = name
        self.length = length

    @classmethod
    def from_row(cls, row):
        return cls(
            str(row["name"]),
            float(row["length"]),
        )