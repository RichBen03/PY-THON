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

    def remove_product(self, name:str)->bool:
        for product in self.products:
            if product.name == name:
                self.products.remove(product)
                return  True, f"{product.name} was removed"
        return False, f"{name} was not found"
    
    def update_quantity(self, name:str, new_quantity:int):
        for product in self.products:
            if product.name == name:
                if new_quantity <0:
                    print("Quantity cannot be zero")
                product.quantity = new_quantity
                return  True, f"{product.name} was found and updated"
            
        return False, f"{name} was not found"

          
                
       
if __name__ == "__main__":
    # Creating objects from the class Products
    soap = Product("Geisha", 200, 1)
    rice = Product("Pishori", 120, 3)
    soda = Product("Coke", 50, 2)
    milk = Product("Brookside", 60, 8)
    
    # Create the object FROM product catalog
    catalog = ProductCatalog()

    # Add products to catalog
    catalog.add_products(rice)
    catalog.add_products(soda)
    catalog.add_products(soap)
    catalog.add_products(milk)

    # List the products in the catalog
    print("\nItems in the Catalog:")
    print(catalog.list_products())

    # List the inventory value
    print("The total invetory value is: ", catalog.total_invetory_value())

    # removing an item from the catalog
    print("Removing an item")
    removed1=catalog.remove_product("Geisha")
    print(removed1)

    print("\n")

    print("Removing an item")
    removed2= catalog.remove_product("Sunlight")
    print(removed2)
     
    print("\n")

    print(catalog.update_quantity("Brookside",2 ))
   

    
        