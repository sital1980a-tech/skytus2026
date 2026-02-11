class Shop:
    def __init__(self, name):
        self.name = name
        self.products = []

    def add_product(self, product_name, price):
        product = {"name": product_name, "price": price}
        self.products.append(product)
        print(f"Product '{product_name}' added successfully!")

    def list_products(self):
        print(f"\nProducts in {self.name}:")
        if not self.products:
            print("No products available.")
        else:
            for i, product in enumerate(self.products, start=1):
                print(f"{i}. {product['name']} - Price: {product['price']}")


shop1 = Shop("Tech Store")

shop1.add_product("Laptop", 50000)
shop1.add_product("Mouse", 500)

shop1.list_products()
