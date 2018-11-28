class Vehicle(object):
    base_sale_price = 0

    def __init__(self, wheels, miles, make, model, year, sold_on):
        self.wheels = wheels
        self.miles = miles
        self.make = make
        self.model = model
        self.year = year
        self.sold_on = sold_on

    def sale_price(self):
        if self.sold_on is not None:
            return 0.0  # Already sold
        return 5000.0 * self.wheels

    def purchase_price(self, amount):
        self.amount = amount
        if self.sold_on is None:
            return 0.0  # Not yet sold
        return self.amount*10


v = Vehicle(4, 2, 'Honda', 'Accord', 2014, 800)
print(v.purchase_price(800))


class Truck(Vehicle):

    def __init__(self, wheels, miles, make, model, year, sold_on):
        """Return a new Truck object."""
        self.wheels = wheels
        self.miles = miles
        self.make = make
        self.model = model
        self.year = year
        self.sold_on = sold_on
        self.base_sale_price = 10000

    def quality(self):
        return self.base_sale_price * self.miles


v = Truck(4, 2, 'Honda', 'Accord', 2014, 800)
print(v.quality())
