import random
import string
import time
from statistics import mean

from mapping import mappable


def randomLetter(_): return random.choice(string.ascii_letters)


def join(x, y): return f"{x}{y}"


productLength = 5


def genProduct(_): return mappable(range(productLength)).map(randomLetter).reduce(join)


productsAmount = 10
orders = dict()
products = mappable(range(productsAmount)).flatMap(genProduct).foreach(
    lambda product: orders.__setitem__(product, [])).asList()

print_state = False


class Order:
    def __init__(self, product, side, price):
        if print_state: print(f"New order {product} {side} {price}")
        self.product = product
        self.side = side
        self.price = price


filled = []


def processOrder(new_order):
    symbol_orders = orders.get(new_order.product)
    for order in symbol_orders:
        mid_price = midPrice(order, new_order.side, new_order.price)
        if mid_price > 0:
            symbol_orders.remove(order)
            filled.append(order)
            filled.append(new_order)
            if print_state: print("Filled at", mid_price, "product", new_order.product, "filled", len(filled))
            return
    symbol_orders.append(new_order)


def midPrice(order, side, price):
    if order.side == side:
        return -1
    if order.side != side and (side == "buy" and price >= order.price or price <= order.price):
        return mean([price, order.price])
    return -1


def generate():
    start_us = time.time()
    sides = ("buy", "sell")
    for i in range(100_000):
        processOrder(Order(random.choice(products), random.choice(sides), random.random() * 100))
    print(time.time() - start_us)


generate()
