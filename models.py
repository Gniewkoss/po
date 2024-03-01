class User:
    def __init__(self, first_name, last_name, birth_year, group):
        self.id = None
        self.first_name = first_name
        self.last_name = last_name
        self.birth_year = birth_year
        self.group = group

    def serialize(self):
        return {
            "id": self.id,
            "firstName": self.first_name,
            "lastName": self.last_name,
            "age": 2024 - self.birth_year,
            "group": self.group
        }
