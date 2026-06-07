
class ProductRepository:
    # Storage 
    def __init__(self):
        self.products = []

    # View Product
    def get_product(self):
        return self.products
    
    # Add Product
    def add_product(self, product):
        self.products.append(product)

    # Update Product 
    def update_product(self, id, name, price):
        for product in self.products:
            if product.get_id == id:
                product.set_name = name
                product.set_price = price
                return True
        return False

    # Remove Product
    def remove_product(self, id):
        for product in self.products:
            if product.get_id == id:
                self.products.remove(product)
                return True
        return False

