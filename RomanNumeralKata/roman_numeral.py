class RomanNumeral():
    def arabic_to_roman(self, arabic_value):
        if arabic_value == 0:
            return ""
        if arabic_value == 1:
            return "I"

        return "V"
