from random import randint, sample, uniform
from acme import Product

# Useful to use with random.sample to generate names
ADJECTIVES = ["Awesome", "Shiny", "Impressive", "Portable", "Improved"]
NOUNS = ["Anvil", "Catapult", "Disguise", "Mousetrap", "???"]


def generate_products(num_products=30):
    """function to generate new products"""
    products = []
    for i in range(num_products):
        name = sample(ADJECTIVES, 1) + sample(NOUNS, 1)
        prod = Product(name)
        prod.price = randint(5, 100)
        prod.weight = randint(5, 100)
        prod.flammability = uniform(0, 2.5)
        products.append(prod)
    return products


def inventory_report(products):
    """Function to report statistics of product list"""
    unique = set(products)
    print("Unique product names:", len(unique))

    prices = []
    for product in products:
        prices.append(product.price)
    avg_price = sum(prices) / len(prices)
    print("Average price:", avg_price)

    weights = []
    for product in products:
        weights.append(product.weight)
    avg_weight = sum(weights) / len(weights)
    print("Average weight:", avg_weight)

    flam = []
    for product in products:
        flam.append(product.flammability)
    avg_flam = sum(flam) / len(flam)
    print("Average flammability:", avg_flam)


if __name__ == "__main__":
    inventory_report(generate_products())
