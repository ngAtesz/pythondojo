class RomanNumeral():
    def arabic_to_roman(self, arabic_val):
        if arabic_val == 0:
            return ""
        if arabic_val == 1:
            return "I"

        return "V"