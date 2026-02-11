class Laptop:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    def apply_discount(self, discount_percent):
        discount_amount = (discount_percent / 100) * self.price
        self.price -= discount_amount
        return self.price

    def display_details(self):
        print("Brand:", self.brand)
        print("Model:", self.model)
        print("Price:", self.price)


laptop1 = Laptop("Dell", "Inspiron", 60000)

print("Original Price:", laptop1.price)

laptop1.apply_discount(10)  

print("Price after Discount:", laptop1.price)
laptop1.display_details()
