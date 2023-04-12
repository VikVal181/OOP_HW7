import Product
from Beer import Beer
from Chips import Chips
from BottleOfWater import BottleOfWater
from VendingMachine import VendingMachine

vendingmachine = VendingMachine()
vendingmachine.add_product(Beer('Amstel', 100, 0.5))
vendingmachine.add_product(Beer('Nevskoe', 120, 2))
vendingmachine.add_product(Chips('Lays', 70, 100, 'Onion'))
vendingmachine.add_product(Chips('Pringles', 90, 150, 'Pepper'))
vendingmachine.add_product(BottleOfWater('Fruto niania', 80, 0.5))
vendingmachine.add_product(BottleOfWater('Bon Aqua', 60, 1))

print(str(vendingmachine.find_product("Lays")))
print(str(vendingmachine.find_product("Russkaia Kortoshka")))
print(str(vendingmachine.find_product("Nevskoe")))
print(str(vendingmachine.find_product("Bon Aqua")))