class Store:
    def __init__(self, name):
        self.name = name
        self.products = []
        # self.product = Product("Carrot", 1.5, "Vegetable")
        # self.product = Product("Onion", 1, "Vegetable")
        # self.product = Product("Coke", 3, "Drink")

    def add_product(self, new_product):
        self.products.append(new_product)
    
    def sell_product(self, id):
        for i in range(0, len(self.products)-1):
            if self.products[i].id == id:
                self.products[i].print_info()
                self.products.remove(self.products[i])

    def inflation(self, percent_increase):
        for i in range(len(self.products)):
            self.products[i].update_price(percent_increase, True)
            print(self.products[i].price)

    def set_clearance(self, category, percent_discount):
        for i in range(len(self.products)):
            if self.products[i].category == category:
                self.products[i].update_price(percent_discount, False)
            print(self.products[i].price)