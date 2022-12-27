import tkinter as tk


class Calculator:

    # class initializer:
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry("390x711")
        # not resizable:
        self.window.resizable(0, 0)
        self.window.title("Calculator")

    # call to Tk main loop:
    def run(self):
        self.window.mainloop()


# run config.:
if __name__ == "__main__":
    calculator = Calculator()
    calculator.run()
