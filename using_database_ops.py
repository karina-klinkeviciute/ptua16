from database_ops import filter_db_by


def sum_price_products() -> int:
    # Get data
    some_data = filter_db_by()

    # Perform computation
    prices = [product["price"] for product in some_data]
    return sum(prices)
