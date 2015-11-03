class RomanNumeral():
    def arabic_to_roman(self, arabic_value):
        if arabic_value == 0:
            return ""
        if arabic_value == 5:
            return "V"

        return "I" + self.arabic_to_roman(arabic_value - 1)
