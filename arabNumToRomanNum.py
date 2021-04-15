def check_input(value):
    
    def test_1(value):
        if not value.isdigit():
            print("Your answer needs to be a natural integer.")
            return 0
        return 1
    def test_2(value):
        if value.isdigit() and not 0 < int(value) <= 3999:
            print("Your answer needs to be between 0 and 3999.")
            return 0
        return 1
    return all([test_1(value), test_2(value)])


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

def arab_to_roman(arabic_input=0):
    check_func = lambda val: [int(i) for i in filter(check_input, val)] # * Check if the value is an arabic number
    final_number = [] # * To list where the final roman number will be stocked

    if arabic_input: # * The arabic numeral is already specified
        arabic_input = check_func([str(arabic_input)]) or "N/A" # * Check if the input is an arabic numeral. Return a list with the arabic numeral
        
    while not arabic_input: # * The user needs to enter manually the arabic numeral
        arabic_input = check_func([input("Enter an arabic numeral to convert: ")])

    if arabic_input == "N/A": # * If the number is not an arabic number
        return arabic_input
    
    while arabic_input[0] > 0: # * The arabic numeral will be substracted until it reaches 0
        lock_sort = [0, "symbol"] # * It will check if the roman symbols are written in order. The first element will be the arabic number of the second element

        for key, value in roman_number_dict.items(): # * Iterate through the dict of roman characters
            if int(arabic_input[0])-value >= 0 and lock_sort[0] < value: # * Write the roman symbols from the lower symbol
                lock_sort[0], lock_sort[1] = value, key

        arabic_input[0] -= lock_sort[0] # * Substract the value of the roman symbol
        final_number.append(lock_sort[1]) # * Add the symbol to the final result
    return ''.join(final_number)

if __name__ == "__main__":
    print(arab_to_roman())
