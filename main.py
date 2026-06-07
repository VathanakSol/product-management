from repository.product import ProductRepository
from service.product import ProductService

repository = ProductRepository()
service = ProductService(repository)

while True:

    print("------Product Management System--------")
    print("1/. View All Products")
    print("2/. Add New Product")
    print("3/. Update Product")
    print("4/. Delete Product")
    print("5/. Exit App")

    option = input("Enter Option (1-5): ")

    match option:
        case "1":
            print("----View Product-----")
            service.get_product()

        case "2":
            print("-----Add Product-----")

            id = int(input("Enter Product ID: "))
            name = input("Enter Product Name: ")
            price = float(input("Enter Product Price: "))

            service.add_product(
                id,
                name,
                price
            )

        case "3":
            print("-------Update Product--------")

            id = int(input("Enter Product ID: "))
            name = input("Enter New Name: ")
            price = float(input("Enter New Price: "))

            service.update_product(
                id,
                name,
                price
            )

        case "4":
            print("----Delete Product------")
            id = int(input("Enter Product ID: "))
            service.remove_product(id)

        case "5":
            print("Thank you for using this system")
            break

        
        
        case _:
            print("INVALID")


