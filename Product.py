
class Product:
    def __init__(self, name, cost):
        self._name = name
        self._cost = cost

    def get_name(self):
        return self._name

    def get_cost(self):
        return self._cost

    def __str__(self):
        return f"Product [ name = {self._name}, cost = {self._cost} ]"