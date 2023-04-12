from Product import Product

class Beer(Product):
    def __init__(self, name, cost, volume):
        super().__init__(name, cost)
        self._volume = volume

    def get_volume(self):
        return self._volume

    def __str__(self):
        return f"Beer [ name = {super().get_name()} volume = {self._volume} cost = {super().get_cost()} ]"