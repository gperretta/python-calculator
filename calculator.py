import tkinter as tk


SMALL_FONT_STYLE = ("Arial", 22)
LARGE_FONT_STYLE = ("Arial", 32)
BUTTON_FONT_STYLE = ("Arial", 26, "bold")
ACCENT_COLOR = "#00d1ff"
SECONDARY_COLOR = "#fe2875"
TERTIARY_COLOR = "#22252d"
BG_COLOR = "#12151d"
FONT_COLOR = "#FFFFFF"


class Calculator:

    # class initializer:
    # noinspection PyTypeChecker
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry("390x711")
        # not resizable:
        self.window.resizable(0, 0)
        self.window.title("Calculator")
        # init var:
        self.total_text = ""
        self.current_text = ""
        # attributes for the display:
        self.display = self.create_display_frame()
        self.total_label, self.current_label = self.create_display_labels()
        # attributes for the buttons:
        self.buttons = self.create_buttons_frame()
        self.number_grid = {
            7: (1, 1), 8: (1, 2), 9: (1, 3),
            4: (2, 1), 5: (2, 2), 6: (2, 3),
            3: (3, 1), 2: (3, 2), 1: (3, 3),
            '.': (4, 1), 0: (4, 2)
        }
        self.operators = {
            "/": "\u00F7", "*": "\u00D7",
            "-": "-", "+": "+"
        }
        self.create_buttons()
        # buttons grid configuration:
        self.buttons.rowconfigure(0, weight=1)
        for element in range(1, 5):
            self.buttons.rowconfigure(element, weight=1)
            self.buttons.columnconfigure(element, weight=1)
        # pc keyboard binding:
        self.keys_binding()

    # create calculator elements frames and labels:
    def create_display_frame(self):
        frame = tk.Frame(self.window, height=211, bg=BG_COLOR)
        frame.pack(expand=True, fill="both")
        return frame

    def create_display_labels(self):
        total_label = tk.Label(self.display, text=self.total_text, anchor=tk.E,
                               background=BG_COLOR, foreground=FONT_COLOR, padx=24, font=SMALL_FONT_STYLE)
        total_label.pack(expand=True, fill="both")

        current_label = tk.Label(self.display, text=self.current_text, anchor=tk.E,
                                 background=BG_COLOR, foreground=FONT_COLOR, padx=24, font=LARGE_FONT_STYLE)
        current_label.pack(expand=True, fill="both")

        return total_label, current_label

    def create_buttons_frame(self):
        frame = tk.Frame(self.window, bg=TERTIARY_COLOR)
        frame.pack(expand=True, fill="both")
        return frame

    # number grid (and dot)
    def create_number_buttons(self):
        for number, grid_value in self.number_grid.items():
            button = tk.Button(self.buttons, text=str(number), background=BG_COLOR, foreground=FONT_COLOR,
                               font=BUTTON_FONT_STYLE, borderwidth=0,
                               command=lambda temp_value=number: self.select_numbers(temp_value))
            button.grid(row=grid_value[0], column=grid_value[1], sticky=tk.NSEW)

    # elementary operators buttons
    def create_operator_buttons(self):
        i = 0
        for operator, symbol in self.operators.items():
            button = tk.Button(self.buttons, text=symbol, background=TERTIARY_COLOR, foreground=SECONDARY_COLOR,
                               font=BUTTON_FONT_STYLE, borderwidth=0,
                               command=lambda temp_value=operator: self.select_operator(temp_value))
            button.grid(row=i, column=4, sticky=tk.NSEW)
            i += 1

    # equals, clear field, square and sqrt buttons
    def create_equal_button(self):
        button = tk.Button(self.buttons, text="=", background=TERTIARY_COLOR, foreground=SECONDARY_COLOR,
                           font=BUTTON_FONT_STYLE, borderwidth=0, command=self.evaluate)
        # button.grid(row=4, column=3, columnspan=3, sticky=tk.NSEW)
        button.grid(row=4, column=4, sticky=tk.NSEW)

    def create_clear_button(self):
        button = tk.Button(self.buttons, text="C", background=TERTIARY_COLOR, foreground=ACCENT_COLOR,
                           font=BUTTON_FONT_STYLE, borderwidth=0, command=self.clear_all)
        button.grid(row=0, column=1, sticky=tk.NSEW)

    def create_square_button(self):
        button = tk.Button(self.buttons, text="x\u00b2", background=TERTIARY_COLOR, foreground=ACCENT_COLOR,
                           font=BUTTON_FONT_STYLE, borderwidth=0, command=self.square)
        button.grid(row=0, column=2, sticky=tk.NSEW)

    def create_sqrt_button(self):
        button = tk.Button(self.buttons, text="\u221ax", background=TERTIARY_COLOR, foreground=ACCENT_COLOR,
                           font=BUTTON_FONT_STYLE, borderwidth=0, command=self.sqrt)
        button.grid(row=0, column=3, sticky=tk.NSEW)

    def create_sign_button(self):
        button = tk.Button(self.buttons, text="+/-", background=BG_COLOR, foreground=FONT_COLOR,
                           font=BUTTON_FONT_STYLE, borderwidth=0, command=self.change_sign)
        button.grid(row=4, column=3, sticky=tk.NSEW)

    # (non-elementary calculation functions)
    def square(self):
        try:
            self.current_text = str(eval(f"{self.current_text}**2"))
        except SyntaxError:
            self.current_text = "SYNTAX ERROR"
        self.update_current_label()

    def sqrt(self):
        try:
            self.current_text = str(eval(f"{self.current_text}**0.5"))
        except SyntaxError:
            self.current_text = "SYNTAX ERROR"
        self.update_current_label()

    def change_sign(self):
        try:
            self.current_text = str(eval(f"{self.current_text}*-1"))
        except SyntaxError:
            self.current_text = "SYNTAX ERROR"
        self.update_current_label()

    # (cleaning up the code)
    def create_buttons(self):
        self.create_number_buttons()
        self.create_operator_buttons()
        self.create_equal_button()
        self.create_clear_button()
        self.create_square_button()
        self.create_sqrt_button()
        self.create_sign_button()

    # user inputs through the GUI:
    def select_numbers(self, value):
        self.current_text += str(value)
        self.update_current_label()

    def select_operator(self, operator):
        self.current_text += operator
        self.total_text += self.current_text
        # clear the current expression for the next input
        self.current_text = ""
        self.update_total_label()
        self.update_current_label()

    def clear_all(self):
        self.current_text = ""
        self.update_current_label()
        self.total_text = ""
        self.update_total_label()

    # update var.:
    def update_total_label(self):
        # self.result_label.config(text=self.result)
        expression = self.total_text
        # replacing operators with the appropriate symbols:
        for operator, symbol in self.operators.items():
            expression = expression.replace(operator, f'{symbol}')
        self.total_label.config(text=expression)

    def update_current_label(self):
        # truncated expression:
        self.current_label.config(text=self.current_text[:14])

    # use 'eval' function + some error handling
    def evaluate(self):
        self.total_text += self.current_text
        self.update_total_label()
        try:
            self.current_text = str(eval(self.total_text))
            self.total_text = ""
        except SyntaxError:
            self.current_text = "SYNTAX ERROR"
        except ZeroDivisionError:
            self.current_text = "MATH ERROR"
        finally:
            self.update_current_label()

    # binding the calculator keys with laptop physical keyboard:
    def keys_binding(self):
        self.window.bind("<Return>", lambda event: self.evaluate())
        # for numbers and dot:
        for key in self.number_grid:
            self.window.bind(str(key), lambda event, number=key: self.select_numbers(number))
        # for elementary operators:
        for key in self.operators:
            self.window.bind(str(key), lambda event, operator=key: self.select_numbers(operator))

    # call to Tk main loop:
    def run(self):
        self.window.mainloop()


# run config.:
if __name__ == "__main__":
    calculator = Calculator()
    calculator.run()
