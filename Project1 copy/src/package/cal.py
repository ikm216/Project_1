import re
import sys

def math_express(input_string):
    """
    Check if the input string has any common mathematical operations.

    Args:
        input_string (str): The input string to check.

    Returns:
        bool: True if mathematical operations exist, False otherwise.
    """
    return bool(re.search(r'[+\-*/()^]', input_string)) #Searches for any math operations


def math(input):
    """
    Perform math equations on a Roman numeral expression by replacing 
    Roman numerals with integers and evaluating the expression.

    Args:
        input (str): A string containing a Roman numeral math expression.

    Returns:
        int or None: The result of the math equation if valid, None otherwise.
    
    Raises:
        ValueError: If the input contains invalid Roman numerals or if the expression is invalid.
    """
    romans_nums = {
        'I': '1', 'IV': '4', 'V': '5', 'IX': '9', 'X': '10', 'XL': '40',
        'L': '50', 'XC': '90', 'C': '100', 'CD': '400', 'D': '500', 'M': '1000'}

    def replace(prob):
        """
        Replace Roman numeral with the integer value.

        Args:
            prob: A regex match object containing a Roman numeral.

        Returns:
            str: The corresponding integer value for the Roman numeral.
        """
        return romans_nums[prob.group(0)]
    
    if not math_express(input):
        roman_value = re.sub(r'\b(I|IV|V|IX|X|XL|L|XC|C|CD|D|M)\b', replace, input)
        print(int(roman_value)) # Convert the string result to an integer

    try:
        roman = re.sub(r'\b(I|IV|V|IX|X|XL|L|XC|C|CD|D|M)\b', replace, input)  # Replace Roman numerals in the input with their integer values.
        roman = eval(roman) # Evaluate the mathematical expression.
        return check(roman)
    except Exception as e:
        print(f"Error: {e}")
        return None

def check(result):
    """
    Check the result to see if it's valid and convert it back to a Roman numeral if valid.

    Args:
        result (int): The integer result of the Roman numeral expression.

    Returns:
        str: The Roman numeral equivalent of the result if valid.

    Exceptions:
        Prints messages for invalid results like zero, negative numbers, fractions, and numbers over 3999.
    """
    if result == 0:
        print("0 does not exist in Roman numerals.")
    elif isinstance(result, float):
        print("There is no concept of a fractional number in Roman numerals.")
    elif result < 0:
        print("Negative numbers can’t be represented in Roman numerals.")
    elif result > 3999:
        print("You’re going to need a bigger calculator.")
    else:
        return converttoRom(result)

def converttoRom(result):
    """
    Convert an integer result back to Roman numerals.

    Args:
        result (int): The integer to be converted to Roman numerals.

    Returns:
        str: The Roman numeral equivalent of the integer.
    """
    values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    romans = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]

    fin_result = ""
    i = 0

    while result > 0:
        for _ in range(result // values[i]):
            fin_result += romans[i]
            result -= values[i]
        i += 1
    return fin_result

if __name__ == "__main__":
    """
    Main entry point of the script. Takes a Roman numeral expression from the command line
    and processes it to perform mathematical calculations.
    
    Usage:
        python calculator.py 'ROMAN_EXPRESSION'

    Example:
        python calculator.py "(X*V)*IV" will calculate and print "LIV"
    """
    if len(sys.argv) != 2:
        print("Usage: python calculator.py 'ROMAN_EXPRESSION'")
    else:
        input = sys.argv[1]
        math(input)
