# tests/order_calculator/test_order_calculator_methods.py

from calculator import OrderCalculator
import pytest


@pytest.fixture
def new_order_calculator():
    return OrderCalculator()


@pytest.fixture
def order_calculator_with_one_item(new_order_calculator):
    # calculator = OrderCalculator()
    item = ("Apples", 2, 4)
    new_order_calculator.add_item(item)
    return new_order_calculator, item


@pytest.fixture
def order_calculator_with_multiple_items(order_calculator_with_one_item):
    # calculator = OrderCalculator()
    # item = ("Apples", 2, 4)
    calculator, item1 = order_calculator_with_one_item
    item2 = ("Pears", 2.5, 3)
    item3 = ("Oranges", 1.2, 1)

    # order_calculator.add_item(item1)
    # calculator.add_item(item)
    calculator.add_item(item2)
    calculator.add_item(item3)
    
    return calculator, (item1, item2, item3)


def test_add_one_item_correct(order_calculator_with_one_item):
    # Setup object
    # order_calculator = OrderCalculator()
    # Each item is a tuple of name, price, and quantity
    # item = ("Apples", 2, 4)
    # Execute main method to test
    # new_order_calculator.add_item(item)
    # Test the functionality
    assert order_calculator_with_one_item[0].get_items() == [order_calculator_with_one_item[1]]


def test_add_multiple_items_correct(order_calculator_with_multiple_items):
    # order_calculator = OrderCalculator()
    # 
    # item1 = ("Apples", 2, 4)
    calculator, items = order_calculator_with_multiple_items
    print(items)
    # item2 = ("Pears", 2.5, 3)
    # item3 = ("Oranges", 1.2, 1)

    # calculator.add_item(item1)
    # calculator.add_item(item2)
    # calculator.add_item(item3)

    assert calculator.get_items() == [items[0], items[1], items[2]]


def test_add_item_raises_error_if_item_less_than_len_3(new_order_calculator):
    # order_calculator = OrderCalculator()
    item = ("Apples", 2)

    # Execute main method to test
    with pytest.raises(ValueError):
        new_order_calculator.add_item(item)


def test_add_item_raises_error_if_none_first_in_item():
    order_calculator = OrderCalculator()

    item = (None, 2, 8)
    # Execute main method to test
    with pytest.raises(ValueError):
        order_calculator.add_item(item)


def test_add_item_raises_error_if_none_second_in_item():
    order_calculator = OrderCalculator()

    item = ("Apples", None, 8)
    # Execute main method to test
    with pytest.raises(ValueError):
        order_calculator.add_item(item)


def test_add_item_raises_error_if_none_third_in_item():
    order_calculator = OrderCalculator()

    item = ("Apples", 2, None)
    # Execute main method to test
    with pytest.raises(ValueError):
        order_calculator.add_item(item)


def test_calculate_subtotal_one_item(order_calculator_with_one_item):
    # Setup object
    # order_calculator = OrderCalculator()
    # item = ("Apples", 2, 4)
    # order_calculator.add_item(item)
    # Execute main method to test
    calculator, _ = order_calculator_with_one_item
    res = calculator.calculate_subtotal()
    # Execute main method to test and test the functionality
    assert res == 8


def test_calculate_subtotal_multiple_items(order_calculator_with_one_item):
    # order_calculator = OrderCalculator()

    calculator, _ = order_calculator_with_one_item

    # item1 = ("Apples", 2, 4)
    item2 = ("Pears", 2.5, 3)
    item3 = ("Oranges", 1.2, 1)

    # order_calculator.add_item(item1)
    calculator.add_item(item2)
    calculator.add_item(item3)

    res = calculator.calculate_subtotal()

    assert res == 16.7

