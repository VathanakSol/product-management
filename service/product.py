from model.product import Product

class ProductService:
    def __init__(self, repository):
        self.repository = repository

    def get_product(self):
        products = self.repository.get_product()

        if len(products) == 0:
            print("No Product Available")

        for product in products:
            product.display()


    def add_product(self, id, name, price):
        product = Product(
            id,
            name,
            price
        )
        self.repository.add_product(product)
        print("Product added successfully")

    def update_product(self, id, name, price):
        product = self.repository.update_product(
            id,
            name,
            price
        )
        if product:
            print("Product updated successfully")
        else:
            print("Product not found")
    
    def remove_product(self, id):
        product = self.repository.remove_product(id)

        if product:
            print("Product deleted successfully")
        else:
            print("Product not found")