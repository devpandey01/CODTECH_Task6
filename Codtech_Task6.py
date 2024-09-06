class OnlineMarketplace:
    def __init__(self):
        self.sellers = {}
        self.products = {}

    def register_seller(self, seller_name):
        if seller_name not in self.sellers:
            self.sellers[seller_name] = []
            print(f"Seller '{seller_name}' registered successfully.")
        else:
            print(f"Seller '{seller_name}' already exists.")

    def add_product(self, seller_name, product_name, price):
        if seller_name in self.sellers:
            self.products[product_name] = {"seller": seller_name, "price": price}
            self.sellers[seller_name].append(product_name)
            print(f"Product '{product_name}' added by {seller_name}.")
        else:
            print(f"Seller '{seller_name}' not found. Please register the seller first.")

    def display_products(self):
        if self.products:
            print("\n--- Marketplace Products ---")
            for product, details in self.products.items():
                print(f"Product: {product}, Seller: {details['seller']}, Price: ${details['price']}")
        else:
            print("No products available in the marketplace.")

def menu():
    marketplace = OnlineMarketplace()

    while True:
        print("\n--- Online Marketplace ---")
        print("1. Register Seller")
        print("2. Add Product")
        print("3. Display Products")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            seller_name = input("Enter seller name: ")
            marketplace.register_seller(seller_name)

        elif choice == '2':
            seller_name = input("Enter seller name: ")
            product_name = input("Enter product name: ")
            try:
                price = float(input("Enter product price: $"))
                marketplace.add_product(seller_name, product_name, price)
            except ValueError:
                print("Invalid input! Please enter a numeric value for the price.")

        elif choice == '3':
            marketplace.display_products()

        elif choice == '4':
            print("Exiting...")
            break

        else:
            print("Invalid choice! Please select a valid option.")

menu()
