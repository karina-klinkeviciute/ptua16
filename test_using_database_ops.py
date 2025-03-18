# test_using_database_ops.py
from unittest.mock import patch
from using_database_ops import sum_price_products


@patch('using_database_ops.filter_db_by')
def test_sum_price_products(mock_filter_db_by):
   mock_filter_db_by.return_value = [
      { "name": "stuff", "price": 12.45 },
      { "name": "more_stuff", "price": 16.6 },
    ]

   print(type(mock_filter_db_by))

   result = sum_price_products()
   assert result == 12.45 + 16.6


def test_foo():
   with patch('using_database_ops.filter_db_by', return_value=[
      {"name": "stuff", "price": 12.45},
      {"name": "more_stuff", "price": 16.6},
   ]):
      result = sum_price_products()
      assert result == 12.45 + 16.6

   # Note! When calling sum_price_products here, filter_db_by
   # won't be mocked and will take a long time again
   result2 = sum_price_products()
