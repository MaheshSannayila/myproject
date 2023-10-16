
class calculator():
    def __init__(self):
        self.result=0
    def display_result(self):
        print(self.result)
    def adding(self,num):
        self.result+=num
    def substract(self,num):
        self.result-= num
    def multiply(self,num):
        self.result *= num
    def dividing (self,num):
        self.result =self.result/num

c=calculator()
c.adding(10)
c.substract(3)
c.multiply(3)
c.dividing(3)
c.display_result()


class cart():
    def __init__ (self):
        self.products={}
        self.prices={}
    def add_products_prices(self,product,quantity,price):
        self.products[product]=quantity
        self.prices[product]=price
    def display_products(self):
        return "product quantity: ",self.products
    def display_prices(self):
        return "product prices: ",self.prices
    def remove_priduct(self,product):
        del self.products[product]
        del self.prices[product]
    def get_total_price(self):
        self.total_price=0
        for product,quantity in self.products.items():
            self.total_price+=quantity * self.prices[product]
        return self.total_price

c=cart()
c.add_products_prices("pen",2,10)
c.add_products_prices("phone",1,10000)
c.remove_priduct("pen")
c.add_products_prices("book",10,30)
print(c.display_products())
print(c.display_prices())
print(c.get_total_price())