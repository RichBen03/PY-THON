# Creating a Product Catalog

# Instruction:

# Define a Product class with attributes like name, price, and quantity. Implement a method to calculate the total value of products in stock.

class Product:
    def __init__(self, name: str, price: float, quantity:int):
        self.name = name
        self.price = price
        self.quantity = quantity

    def total_value(self) -> float:
        return self.quantity * self.price
    
    def __str__(self):
        return f"{self.name}: {self.quantity} each costing KES {self.price}, will all amount to {self.total_value()}"


class ProductCatalog:
    def __init__(self):
        self.products = []

    def add_products(self, product:Product):
        self.products.append(product)

    def total_invetory_value(self)-> float:
         return sum(product.total_value() for product in self.products) 
    
    def list_products(self):
        print("The product catalog includes: ")
        for product in self.products:
            print("-", product)
            
    
if __name__ == "__main__":
    # Creating objects from the class Products
    soap = Product("Geisha", 200, 1)
    rice = Product("Pishori", 120, 3)
    soda = Product("Coke", 50, 2)
    
    # Create the object FROM product catalog
    catalog = ProductCatalog()
    catalog.add_products(rice)
    catalog.add_products(soda)
    catalog.add_products(soap)

    # List the products in the catalog
    catalog.list_products()

    # List the inventory value
    print("The total invetory value is: ", catalog.total_invetory_value())



    
        