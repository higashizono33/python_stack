from product import Product
from store import Store

# walMart.inflation(0.05)
potato = Product(1, "Potato", 2, "Vegetable")
# potato.update_price(0.05, True).print_info()
carrot = Product(2, "Carrot", 1.5, "Vegetable")
onion = Product(3, "Onion", 1, "Vegetable")
coke = Product(4, "Coke", 3, "Drink")
pepsi = Product(5, "Pepsi", 2.8, "Drink")
chips = Product(6, "Chips", 3, "Snack")
cake = Product(7, "Cake", 3, "Snack")
candy = Product(8, "Candy", 3, "Snack")

walMart = Store('Wal Mart')
walMart.add_product(potato)
walMart.add_product(carrot)
walMart.add_product(onion)
walMart.add_product(coke)
walMart.add_product(pepsi)
walMart.add_product(chips)
walMart.add_product(cake)
walMart.add_product(candy)
walMart.sell_product(6)
# print(walMart.products)
# walMart.set_clearance("Vegetable", 0.05)

# class Store:
#     def __init__(self, name):
#         self.name = name
#         self.products = []
#         # self.product = Product("Carrot", 1.5, "Vegetable")
#         # self.product = Product("Onion", 1, "Vegetable")
#         # self.product = Product("Coke", 3, "Drink")

#     def add_product(self, new_product):
#         self.products.append(new_product)
    
#     def sell_product(self, id):
#         self.products[id].print_info()
#         self.products.pop(id)

#     def inflation(self, percent_increase):
#         for i in range(len(self.products)):
#             self.products[i].update_price(percent_increase, True)
#             print(self.products[i].price)

#     def set_clearance(self, category, percent_discount):
#         for i in range(len(self.products)):
#             if self.products[i].category == category:
#                 self.products[i].update_price(percent_discount, False)
#             print(self.products[i].price)

# class Product:
#     def __init__(self, name, price, category):
#         self.name = name
#         self.price = price
#         self.category = category

#     def update_price(self, percent_change, is_increased):
#         if is_increased == True:
#             self.price += self.price * percent_change
#         else:
#             self.price -= self.price * percent_change
#         return self
#     def print_info(self):
#         print('Name: {}, Price: ${}, Category: {}'.format(self.name, self.price, self.category))
#         return self

