class Animal:
    def __init__(self, name: str, age: int, extinct: bool):
        self.name = name
        self.age = age
        self.extinct = extinct

    def make_sound(self) -> str:
        return "Some generic animal sound"

    def get_info(self) -> str:
        return f"Name: {self.name}, Age: {self.age}, Extinct: {self.extinct}"
