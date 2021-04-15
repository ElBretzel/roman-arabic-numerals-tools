def test_1(pos, val):
    return f"{val[pos]} is not a valid symbol."

def test_2(pos, val):
    return f"{val[pos]} must no be repeated more than 3 times in a row."

def test_3(pos, val):
    num = [(p, c, n) for p, c, n in zip(val[pos-1], val[pos], val[pos+1])]
    if num and roman_number_dict.get(num[0][0]) == roman_number_dict.get(num[0][1]) and roman_number_dict.get(num[0][1]) < roman_number_dict.get(num[0][2]):
        return f"{num[0][2]} is preceded by an {num[0][0]} symbol which is repeated more than once."
    elif num and roman_number_dict.get(num[0][0]) < roman_number_dict.get(num[0][1]) and roman_number_dict.get(num[0][1]) == roman_number_dict.get(num[0][2]):
        return f"{num[0][0]} precedes an {num[0][1]} symbol which is repeated more than once."

def test_4(pos, val):
    if val[pos] == val[pos+1] and val[pos] in ["L", "D", "V"]:
        return f"{val[pos]} appeared more than once."
    elif val[pos] == "I" and val[pos+1] not in ["I", "V", "X"]:
        return "I must only precedes an itself, V and X."
    elif val[pos] == "X" and val[pos+1] in ["D", "M"]:
        return "X must not precedes an by D or M."
    elif val[pos] == "V" and val[pos+1] not in ["I"]:
        return "V must not precedes an higher symbols."
    elif val[pos] == "L" and val[pos+1] in ["C", "D", "M"]:
        return "L must not precedes an higher symbols."

def check_input(value):
    result = ""
    
    for i in range(len(value)):
        
        if not roman_number_dict.get(value[i]): # * If the symbol don't exists
            result = test_1(i, value) or result

        if len(value)-3 > i and all(value[i] == value[i + j] for j in range(4)): # * If there is more than 3 other symbol after the current position and the same symbol is repeated more than 3 times
            result = test_2(i, value) or result

        if i >= 1 and len(value)-1 > i: # * If the current symbol position is greater than the first position and there is more than 1 other symbol after the current position
            result = test_3(i, value) or result

        if len(value)-1 >i: # * If there is more than 1 other symbol after the current position
            result = test_4(i, value) or result

        if result:
            print(f"Invalid roman numeral: {result}")
            return 0
    return 1

roman_number_dict = {"I": 1,
                   "IV": 4,
                   "V": 5,
                   "IX": 9,
                   "X": 10,
                   "XL": 40,
                   "L": 50,
                   "XC": 90,
                   "C": 100,
                   "CD": 400,
                   "D": 500,
                   "CM": 900,
                   "M": 1000
                   }

def roman_to_arab(roman_input=""):

    assert not isinstance(roman_input, int), "You can't convert already converted value."
    
    check_func = lambda val: ''.join(list(filter(check_input, val))) # * Check if the value is a roman symbol
    final_number = 0 # * The final arabic value 
    
    if roman_input: # * The roman number is already specified
        roman_input = check_func([str(roman_input)]) or "N/A" # * Check if the input is a roman numeral. Return a list str with roman numeral
    
    while not roman_input: # * The user needs to enter manually the roman numeral
        roman_input = check_func([input("Enter a roman numeral to convert: ")])

    if roman_input == "N/A": # * If the number is not a roman number
        return roman_input

    while roman_input:
        if len(roman_input) > 1 and roman_number_dict.get(roman_input[0]) < roman_number_dict.get(roman_input[1]): # * If the roman number is larger than 1 symbol and the first symbol is lower than the next
            final_number += roman_number_dict.get(roman_input[1]) - roman_number_dict.get(roman_input[0]) # * Substract the value of the highest symbol with the lowest and add the result to the final arabic result 
            roman_input = roman_input[2:] # * Delete the first two elements of the roman number
        else: # * The len of the roman number is 1 or the next symbol is lower than the first
            final_number += roman_number_dict.get(roman_input[0]) # * Adding the value of the symbol to the final arabic result
            roman_input = roman_input[1:] # * Delete the first element of the roman number

    return final_number


if __name__ == "__main__":
    print(roman_to_arab())
