class VendingMachine:
    def __init__(self):
        list = []
        self._product_list = list

    def add_product(self, product):
        self._product_list.append(product)

    def find_product(self, product_name):
        for product in self._product_list:
            if product.get_name() == product_name:
                return product
        return f"Продукт с названием \"{product_name}\" не найден"