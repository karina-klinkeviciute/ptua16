from unittest.mock import patch


def test_calculator():
    with patch("calculator2.Calculator", autospec=True) as calculator:
        # Instantiate mocked Calculator class
        calc = calculator()
        # multiply does not exist in Calculator
        calc.add.return_value = 8
        assert calc.add(3, 5) == 8
