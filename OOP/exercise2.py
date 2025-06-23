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
    
soap = Product("Geisha",200,5)
due_price = soap.total_value()
print(f"The total cost for your {soap.name} products is KES: {due_price}")

    
        