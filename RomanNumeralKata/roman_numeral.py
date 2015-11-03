class RomanNumeral():
    def arabic_to_roman(self, number_to_convert):
        result = ""
        roman_symbols = ["V", "IV", "I"]
        arabic_values = [5, 4, 1]

        while number_to_convert > 0:
            for i in range(len(roman_symbols)):
                if number_to_convert >= arabic_values[i]:
                    result += roman_symbols[i]
                    number_to_convert -= arabic_values[i]

        return result
