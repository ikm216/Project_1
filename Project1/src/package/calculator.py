import re

#Doing the math of the Roman Numerial equation
def math(input):
    romans_nums = {'I':'1', 'V':'5', 'X':'10', 'L': '50', 'C':'100', 'D': '500', 'M': '1000'} #Use a dictionary to set the roman numerials
    
    #Replacing the the Roman Numerials with integers
    def replace(prob):
        return romans_nums[prob.group(0)]
    
    roman = re.sub(r'\b(I|V|X|L|C|D|M)\b', replace, input) #Using re to replace the roman numerials with the value 
    
    #Checks if the equation is valid
    try:
        roman = eval(roman) #Converts the string in a actual math expression and do the equation
        return check(roman) #Return the integer in the check function
    except Exception as e:
        print(f"Error: {e}")
        return None   
#Checks to see if the integer meets all the requirements in the project 1 rubric
def check(result):
    if result == 0:
        print("0 does not exist in Roman numerals.")
    elif isinstance(result, float):
        print("There is no concept of a fractional number in Roman numerals.")
    elif result < 0:
        print("Negative numbers can’t be represented in Roman numerals.")
    elif result > 3999:
        print("You’re going to need a bigger calculator.")
    else:
        #Once it checks all the requirements it will convert the integer in a Roman numerials
        def converttoRom(result):
            values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
            romans = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]

            fin_result = ""
            i = 0

            #While the result is greater than zero, it will keep the subtracting with the highest value
            #to put the Roman numerials in order
            while result > 0:
                for _ in range(result // values[i]):
                    fin_result += romans[i]
                    result -= values[i]
                i += 1
            return fin_result #Return the final result of the roman numerial result
        print(converttoRom(result))

        

user = input("Enter your problem: ")
user = user.upper()

result = math(user)

print(result)

