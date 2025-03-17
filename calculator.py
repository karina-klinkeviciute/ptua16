class OrderCalculator:
    def __init__(self):
        self._items = []

    def get_items(self) -> list:
        """Returns the list of items in the order."""
        return self._items

    def add_item(self, item: tuple) -> None:
        """Adds an item to the order."""
        if len(item) < 3:
            raise ValueError("The item consists of 3 values: name, price, and quantity")

        if None in item:
            raise ValueError("There must be no None in the item!")

        self._items.append(item)

    def calculate_subtotal(self) -> float:
        """Calculates the price of all items in the order without tax."""
        subtotal = 0
        for item in self._items:
            price = item[1]
            quantity = item[2]
            subtotal += price * quantity
        return subtotal
    