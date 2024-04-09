import os
import settings
import sys
from time import sleep


def is_windows():
    return os.name == "nt"


class Terminal:

    def __init__(self) -> None:
        self.windows = is_windows()

    def clear(self):
        if self.windows:
            os.system("cls")
        else:
            os.system("clear")

    @staticmethod
    def print_center(text: str):
        print(text.center(os.get_terminal_size().columns, " "))

    @staticmethod
    def print_line():
        print("=".center(os.get_terminal_size().columns, "="))

    @staticmethod
    def print_loading_bar():
        wait_time_s = settings.DRAWN_RATE
        for i in range(wait_time_s, -1, -1):
            width = os.get_terminal_size().columns - 3
            load = width - int(i * (width / wait_time_s))
            bar = "[" + ">" * load + ">" + "-" * (width - load) + "]"
            sys.stdout.write("\r")
            sys.stdout.write(" " * width)
            sys.stdout.write("\r")
            sys.stdout.write(bar)
            sys.stdout.flush()
            sleep(1)

    @staticmethod
    def tabellone_print(numbers_extracted: list):

        def tabellone_cell(num, space=1, extracted=True):
            # not extracted
            if not extracted:
                _num = "  "
            else:
                _num = f"{num:02d}"
            # left margin
            if str(num).endswith("1"):
                return "|" + " " * space + str(_num) + " " * space + "|"
            # mid column
            if str(num).endswith("5"):
                return " " * space + str(_num) + " " * space + "||"
            # else
            return " " * space + str(_num) + " " * space + "|"

        width = os.get_terminal_size().columns
        tab_width = 52
        h_line = "=" * tab_width

        print(h_line.center(width, " "))
        for i in range(0, 90, 10):
            row = ""
            for j in range(1, 11):
                num = j + i
                row += tabellone_cell(num, extracted=num in numbers_extracted)
            print(row.center(width, " "))
            if i in [20, 50]:
                print(h_line.center(width, " "))
        print(h_line.center(width, " "))
