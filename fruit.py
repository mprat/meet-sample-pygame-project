class Fruit(object):
    def __init__(self, name, price):
        self.price = price
        self.name = name

    def __repr__(self):
        return self.name + ": " + str(self.price) + " USD"