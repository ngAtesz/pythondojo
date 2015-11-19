class FizzBuzz:
    def generate(self):
        number_list = []
        for n in range(1, 101):
            number_list.append(self._convert_num_to_fizz_buzz(n))
        return number_list

    def _convert_num_to_fizz_buzz(self, number):
        result = ""
        if self._should_append_fizz(number):
            result += "Fizz"

        if self._should_append_buzz(number):
            result += "Buzz"

        if result == "":
            result += str(number)

        return result

    def _should_append_fizz(self, number):
        return ("3" in str(number)) or (number % 3 == 0)

    def _should_append_buzz(self, number):
        return ("5" in str(number)) or (number % 5 == 0)
