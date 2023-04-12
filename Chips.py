from Product import Product

class Chips(Product):
    def __init__(self, name, cost, weight, flavor):
        super().__init__(name, cost)
        self._weight = weight
        self._flavor = flavor

    def get_weight(self):
        return self._weight

    def get_flavor(self):
        return self._flavor

    def __str__(self):
        return f"Chips [ name = {super().get_name()} " \
               f"weight = {self._weight} flavor = {self._flavor} cost = {super().get_cost()} ]"