import pytest
import calculator

def math_equation():
    """
    Test function to detect mathematical operations.
    """
    assert calculator.has_math_operations("X + V") == True, "Should return True for 'X + V'"
    assert calculator.has_math_operations("X V") == False, "Should return False for 'X V'"

def math_equation2():
    """
    Test the math function with a valid mathematical operation.
    """
    assert calculator.math("(X+V)*2") == 30, "Should evaluate '(X+V)*II' to 30"
    assert calculator.math("M+D") == 1500, "Should evaluate 'M+D' to 1500"

def math_withno_mathoperations():
    """
    Test the math function with no mathematical operations.
    """
    assert calculator.math("X") == 10, "Should convert 'X' to 10"
    assert calculator.math("IV") == 4, "Should convert 'IV' to 4"

def check_zero():
    """
    Test that check function returns None for zero result.
    """
    assert calculator.check(0) == None, "Should return None for result = 0"

def check_negative():
    """
    Test that check function returns None for negative result.
    """
    assert calculator.check(-10) == None, "Should return None for negative numbers"

def check_float():
    """
    Test that check function returns None for float numbers.
    """
    assert calculator.check(5.5) == None, "Should return None for float numbers"

def check_large_value():
    """
    Test that check function returns None for values greater than 3999.
    """
    assert calculator.check(4000) == None, "Should return None for values > 3999"

def test_converttoRom():
    """
    Test that converttoRom function correctly converts integers to Roman numerals.
    """
    assert calculator.converttoRom(50) == "L", "Should convert 50 to 'L'"
    assert calculator.converttoRom(100) == "C", "Should convert 100 to 'C'"
    assert calculator.converttoRom(3999) == "MMMCMXCIX", "Should convert 3999 to 'MMMCMXCIX'"