"""Unit tests for the calculator MCP tool."""

import importlib.util
import os

# Load calculator function directly from file to avoid circular imports
# in the agents package __init__.py
_module_path = os.path.join(
    os.path.dirname(__file__), "..", "agents", "tools", "calculator_mcp.py"
)
_spec = importlib.util.spec_from_file_location("calculator_mcp", _module_path)
_mod = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_mod)
calculator = _mod.calculator


class TestAddition:
    def test_positive_numbers(self):
        assert calculator(2, 3, "+") == "Result: 5"

    def test_negative_numbers(self):
        assert calculator(-2, -3, "+") == "Result: -5"

    def test_mixed_sign(self):
        assert calculator(-2, 3, "+") == "Result: 1"

    def test_zero(self):
        assert calculator(0, 5, "+") == "Result: 5"

    def test_decimals(self):
        assert calculator(1.5, 2.5, "+") == "Result: 4"


class TestSubtraction:
    def test_positive_numbers(self):
        assert calculator(5, 3, "-") == "Result: 2"

    def test_negative_result(self):
        assert calculator(3, 5, "-") == "Result: -2"

    def test_zero_result(self):
        assert calculator(5, 5, "-") == "Result: 0"

    def test_decimals(self):
        assert calculator(5.5, 2.3, "-") == "Result: 3.2"


class TestMultiplication:
    def test_positive_numbers(self):
        assert calculator(4, 3, "*") == "Result: 12"

    def test_by_zero(self):
        assert calculator(5, 0, "*") == "Result: 0"

    def test_negative_numbers(self):
        assert calculator(-3, -4, "*") == "Result: 12"

    def test_mixed_sign(self):
        assert calculator(-3, 4, "*") == "Result: -12"

    def test_decimals(self):
        assert calculator(2.5, 4, "*") == "Result: 10"


class TestDivision:
    def test_even_division(self):
        assert calculator(10, 2, "/") == "Result: 5"

    def test_decimal_result(self):
        assert calculator(7, 2, "/") == "Result: 3.5"

    def test_divide_by_zero(self):
        assert calculator(5, 0, "/") == "Error: Division by zero"

    def test_negative_division(self):
        assert calculator(-10, 2, "/") == "Result: -5"

    def test_zero_numerator(self):
        assert calculator(0, 5, "/") == "Result: 0"


class TestExponentiation:
    def test_square(self):
        assert calculator(3, 2, "^") == "Result: 9"

    def test_cube(self):
        assert calculator(2, 3, "^") == "Result: 8"

    def test_zero_exponent(self):
        assert calculator(5, 0, "^") == "Result: 1"

    def test_negative_exponent(self):
        assert calculator(2, -1, "^") == "Result: 0.5"


class TestSquareRoot:
    def test_perfect_square(self):
        assert calculator(9, 0, "sqrt") == "Result: 3"

    def test_non_perfect_square(self):
        result = calculator(2, 0, "sqrt")
        assert result.startswith("Result: 1.414")

    def test_zero(self):
        assert calculator(0, 0, "sqrt") == "Result: 0"

    def test_one(self):
        assert calculator(1, 0, "sqrt") == "Result: 1"

    def test_negative_number(self):
        assert calculator(-4, 0, "sqrt") == "Error: Cannot take square root of negative number"


class TestUnsupportedOperator:
    def test_modulo(self):
        assert calculator(5, 3, "%") == "Error: Unsupported operator '%'"

    def test_word_operator(self):
        assert calculator(5, 3, "add") == "Error: Unsupported operator 'add'"

    def test_empty_operator(self):
        assert calculator(5, 3, "") == "Error: Unsupported operator ''"


class TestIntegerFormatting:
    """Verify that float results that are whole numbers are formatted as ints."""

    def test_addition_returns_int_string(self):
        result = calculator(2.0, 3.0, "+")
        assert result == "Result: 5"

    def test_division_returns_int_when_even(self):
        result = calculator(10.0, 2.0, "/")
        assert result == "Result: 5"

    def test_division_keeps_decimal_when_needed(self):
        result = calculator(7, 2, "/")
        assert result == "Result: 3.5"
