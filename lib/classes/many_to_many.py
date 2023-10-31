class Coffee:
    all = []
    def __init__(self, name):
        self.name = name
        Coffee.all.append(self)

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if isinstance(name, str) and not hasattr(self, "name"):
            self._name = name
        
    def orders(self):
        return [coffee for coffee in Order.all if coffee.coffee is self]
    
    def customers(self):
        return list({coffee.customer for coffee in self.orders()})
    
    def num_orders(self):
        return len(self.orders())
    
    def average_price(self):
        return sum([order.price for order in self.orders()]) / len(self.orders())

class Customer:
    all = []
    def __init__(self, name):
        self.name = name
        Customer.all.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if type(name) is str and 1 <= len(name) <= 15:
            self._name = name

    def orders(self):
        return [order for order in Order.all if order.customer is self]
    
    def coffees(self):
         return list({customer.coffee for customer in self.orders()})
    
    def create_order(self, coffee, price):
        return Order(self, coffee, price)
    
class Order:
    all = []
    def __init__(self, customer, coffee, price):
        self.customer = customer
        self.coffee = coffee
        self.price = price
        Order.all.append(self)

    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self, price):
        if type(price) is float and not hasattr(self, "price"):
            self._price = price

    @property
    def customer(self):
        return self._customer
    
    @customer.setter
    def customer(self, customer):
        if type(customer) is Customer:
            self._customer = customer

    @property
    def coffee(self):
        return self._coffee
    
    @coffee.setter
    def coffee(self, coffee):
        if type(coffee) is Coffee:
            self._coffee = coffee