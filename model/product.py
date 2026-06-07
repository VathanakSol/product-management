from model.base import Base

class Product(Base):
    def __init__(self, id, name, price):
        super().__init__(id, name)
        self.__price = price

    # Getter
    @property
    def get_price(self):
        return self.__price
    
    # Setter
    @get_price.setter
    def set_price(self, value):
        self.__price = value

    def display(self):
        print("------Product Overview-------")
        print(f"Product ID        : {self.get_id}")
        print(f"Product Name      : {self.get_name}")
        print(f"Product Price     : {self.get_price}")
    