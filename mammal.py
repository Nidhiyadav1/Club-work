from animal import Animal

class Mammal(Animal):
    def __init__(self, name: str, age: int, extinct: bool, colour: str):
        super().__init__(name, age, extinct)
        self.colour = colour

    def make_sound(self) -> str:
        return "Mammal sound"

    def get_info(self) -> str:
        base_info = super().get_info()
        return f"{base_info}, Colour: {self.colour}"
