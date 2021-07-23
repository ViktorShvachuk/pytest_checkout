class Checkout:
    class Discount:
        def __init__(self, number_of_items, price):
            self.number_of_items = number_of_items
            self.price = price

    def __init__(self):
        self.discounts = {}
        self.items_prices = {}
        self.items = {}
        self.total = 0

    def add_discount(self, item, number_of_items, price) -> None:
        self.discounts[item] = self.Discount(number_of_items, price)

    def add_item_price(self, item, price) -> None:
        self.items_prices[item] = price

    def add_item(self, item) -> None:
        if item not in self.items_prices:
            raise Exception("Bad item")

        if item in self.items:
            self.items[item] += 1
        else:
            self.items[item] = 1

    def calculate_total(self) -> float:
        total = 0
        for item, count in self.items.items():
            discount_price = 0
            if item in self.discounts:
                discount = self.discounts[item]
                discount_price = (count // discount.number_of_items) * discount.price
            total += (self.items_prices[item] * count) - discount_price
        return total
