class Product:
    def __init__(self, id, name, price, category):
        self.id = id
        self.name = name
        self.price = price
        self.category = category

    def update_price(self, percent_change, is_increased):
        if is_increased == True:
            self.price += self.price * percent_change
        else:
            self.price -= self.price * percent_change
        return self
    def print_info(self):
        print('Name: {}, Price: ${}, Category: {}'.format(self.name, self.price, self.category))
        return self
