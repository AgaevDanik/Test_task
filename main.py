class Frame:

    def __init__(self, data_list: list, border_sign: str, name: str):
        self.data_list = data_list
        self.border_sign = border_sign
        self.name = name

    def get_a_border_width(self) -> int:
        return self.get_max_len() + 4

    def get_max_len(self) -> int:
        max_len = 0
        for i in self.data_list:
            if i.__len__() > max_len:
                max_len = i.__len__()

        return max_len

    def get_delta(self, item) -> int:
        return self.get_max_len() - item.__len__()

    def print_frame(self) -> None:
        self.print_horizontal_border()
        self.print_content()
        self.print_horizontal_border()

    def print_content(self) -> None:
        for item in self.data_list:
            print(self.make_content_row(item))

    def make_content_row(self, item):
        return f"{self.border_sign} " + item + (" " * (self.get_delta(item) + 1)) + self.border_sign

    def print_horizontal_border(self) -> None:
        print(self.border_sign * self.get_a_border_width())


if __name__ == '__main__':
    pyramid = Frame(['    _',
                     '   ___',
                     '  _____',
                     ' _______',
                     '_________',
                     '   _'], '*', 'pyramid')
    pyramid.print_frame()
