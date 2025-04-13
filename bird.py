from animal import Animal

class Bird(Animal):
    def __init__(self, name: str, age: int, extinct: bool, can_fly: bool):
        super().__init__(name, age, extinct)
        self.can_fly = can_fly

    def make_sound(self) -> str:
        return "Bird chirp"

    def get_info(self) -> str:
        base_info = super().get_info()
        return f"{base_info}, Can Fly: {self.can_fly}"
