customers = []
products = []
sales = []

def add_customer(name):
    customers.append(name)
    print("Customer added:", name)

def add_product(name, price):
    products.append({"name": name, "price": price})
    print("Product added:", name)

def register_sale(product, quantity):
    sales.append({"product": product, "quantity": quantity})
    print("Sale registered")

add_customer("Maria")
add_product("Coffee", 15)

register_sale("Coffee", 2)

print("Customers:", customers)
print("Products:", products)
print("Sales:", sales)
