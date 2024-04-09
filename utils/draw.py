from os import path
from random import choice


class Draw:

    def __init__(
        self,
        total_numbers: int,
        numbers_extracted_file: str,
        print_last_n_drawn: int = 5,
    ) -> None:
        self.numbers_list = set(range(1, total_numbers + 1))
        self.numbers_extracted_file = numbers_extracted_file
        self.print_last_n_drawn = print_last_n_drawn

        if not path.exists(numbers_extracted_file):
            with open(numbers_extracted_file, "w") as f:
                pass

    def number_draw(self):
        numbers_extracted = self.number_get_drawn()
        with open(self.numbers_extracted_file, "a+") as file:
            numbers_possible = list(self.numbers_list - set(numbers_extracted))
            if not numbers_possible:
                return
            number_extracted = choice(numbers_possible)
            print(number_extracted, file=file)
            return number_extracted

    def number_get_drawn(self):
        with open(self.numbers_extracted_file, "r") as file:
            numbers_extracted = [line.rstrip() for line in file]
            numbers_extracted = [l for l in numbers_extracted if l != ""]
            if numbers_extracted:
                numbers_extracted = [int(n) for n in numbers_extracted]
            return numbers_extracted

    def number_get_lasts(self):
        with open(self.numbers_extracted_file, "r") as file:
            numbers_extracted = [line.rstrip() for line in file]
            numbers_extracted = [l for l in numbers_extracted if l != ""]
            if numbers_extracted:
                numbers_extracted = [int(n) for n in numbers_extracted]
            return numbers_extracted[-self.print_last_n_drawn :]
