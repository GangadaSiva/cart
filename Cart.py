class product:
    def __init__(self, name, price, deal_price, ratings):
        self.name = name
        self.price = price
        self.deal_price = deal_price
        self.ratings = ratings
        self.you_save = price - deal_price
    def display_items_list(self):
        print("Name: {}".format(self.name))
        print("Price: {}".format(self.price))
        print("Deal price: {}".format(self.deal_price))
        print("Rating: {}".format(self.ratings))
        print("You saved: {}".format(self.you_save))
    def Get_deal_price(self):
        return self.deal_price
class electronic_items(product):
    def __init__(self,name, price, deal_price, ratings, warranty_in_months):
        super().__init__(name, price, deal_price, ratings)
        self.warranty_in_months = warranty_in_months
        
    def display_items_list(self):
        super().display_items_list()
        print("Warranty: {} months".format(self.warranty_in_months))
class grocery_items(product):
    def __init__(self,name, price, deal_price, ratings, Expiry_date):
        super().__init__(name, price, deal_price, ratings)
        self.Expiry_date = Expiry_date
        
    def display_items_list(self):
        super().display_items_list()
        print("Warranty: {}".format(self.Expiry_date))
class lap(electronic_items):
    def __init__(self, name, price, deal_price, ratings, warranty_in_months, ram, storage):
        super().__init__(name, price, deal_price, ratings, warranty_in_months)
        self.ram = ram
        self.storage = storage
    def display_items_list(self):
        super().display_items_list()
        print("Ram: {}".format(self.ram))
        print("Storage: {}".format(self.storage))
        
class order:
    deliver_charges = {"Normal": 0, "Prime": 100}
    def __init__(self, deliver_method, delivery_address):
        self.order_items = []
        self.deliver_method = deliver_method
        self.delivery_address = delivery_address
    def add_item(self, product, qty):
        self.order_items.append((product,qty))
    def display_order_list(self):
        print("deliver method: {}".format(self.deliver_method))
        print("delivery address: {}".format(self.delivery_address))
        print("product")
        print("-----------------------------")
        for product, qty in self.order_items:
            product.display_items_list()
            print("Quantity: {}".format(qty))
            print("")
        print("-----------------------------")
        total_bill = self.get_total()
        print("Total: {}". format(total_bill))
            
    def get_total(self):
        total_price = 0
        for product, qty in self.order_items:
            total_price += product.Get_deal_price() * qty
        order_del_charges = order.deliver_charges[self.deliver_method]  
        total_price = total_price + order_del_charges
        return total_price
        
e = electronic_items("Tv", 3000, 2000, 4.5,6)
milk = grocery_items("Milk", 40, 25, 4.0, "jan 2023")
myOrder = order("Prime", "Hyderabad")
myOrder.add_item(e , 2)
myOrder.add_item(milk, 3)
myOrder.display_order_list()