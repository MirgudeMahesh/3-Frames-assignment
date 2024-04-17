class Product:
    def __init__(self, product_id, name, description, category, price):
        self.product_id = product_id
        self.name = name
        self.description = description
        self.category = category
        self.price = price

class ProductDatabase:
    def __init__(self):
        self.products_by_category = {}

    def add_product(self, product):
        if product.category not in self.products_by_category:
            self.products_by_category[product.category] = []
        self.products_by_category[product.category].append(product)

    def search_by_name(self, query):
        results = []
        for category, products in self.products_by_category.items():
            for product in products:
                if query.lower() in product.name.lower():
                    results.append(product)
        return results

    def search_by_description(self, query):
        results = []
        for category, products in self.products_by_category.items():
            for product in products:
                if query.lower() in product.description.lower():
                    results.append(product)
        return results

    def search_by_category(self, category):
        return self.products_by_category.get(category, [])

    def textual_search(self, query):
        results = []
        results.extend(self.search_by_name(query))
        results.extend(self.search_by_description(query))
        return results


product_db = ProductDatabase()


product_db.add_product(Product(1, "Laptop", "Powerful laptop for work and gaming", "Electronics", 1200))
product_db.add_product(Product(2, "Desk Lamp", "Adjustable LED desk lamp", "Home & Kitchen", 35))
product_db.add_product(Product(3, "Running Shoes", "Comfortable and durable running shoes", "Sports & Outdoors", 80))
product_db.add_product(Product(4, "Garden Hose", "50 feet long heavy-duty garden hose", "Home & Kitchen", 50))

# Searching products
print("Searching by name:")
print(product_db.search_by_name("Laptop"))
print("\nSearching by category:")
print(product_db.search_by_category("Home & Kitchen"))
print("\nTextual search:")
print(product_db.textual_search("shoes"))
