import tkinter as tk
import math
import re

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("계산기")
        self.root.geometry("300x450")

        self.expression = ""

        self.entry = tk.Entry(root, font=("Arial", 24), justify="right")
        self.entry.grid(row=0, column=0, columnspan=4, sticky="nsew", padx=10, pady=10, ipadx=8, ipady=15)

        self.root.bind("<Key>", self.on_keypress)
        self.root.bind("<Return>", lambda event: self.on_click('='))
        self.root.bind("<BackSpace>", lambda event: self.on_click('←'))

        buttons = [
            ['(', ')', 'C', '←'],
            ['7', '8', '9', '/'],
            ['4', '5', '6', '*'],
            ['1', '2', '3', '-'],
            ['0', '.', '.', '+'],
            ['x²', '√', '%' ,'=']
        ]

        for r, row in enumerate(buttons, start=1):
            c = 0
            while c < len(row):
                char = row[c]

                btn = tk.Button(
                    self.root,
                    text=char,
                    font=("Arial", 18),
                    command=lambda ch=char: self.on_click(ch)
                )

                if char == '=':
                    btn.grid(row=r, column=c, columnspan=2, sticky="nsew", padx=2, pady=2)
                    c += 2
                    continue
                elif char == '0':
                    btn.grid(row=r, column=c, columnspan=2, sticky="nsew", padx=2, pady=2)
                    c += 2
                    continue
                else:
                    btn.grid(row=r, column=c, sticky="nsew", padx=2, pady=2)
                    c += 1

        # grid 비율 조정
        total_rows = len(buttons) + 1  # entry 포함
        for i in range(total_rows):
            self.root.grid_rowconfigure(i, weight=1)

        for j in range(4):  # 4열 기준
            self.root.grid_columnconfigure(j, weight=1)

    def on_click(self, char):
        if char == 'C':
            self.expression = ""
        elif char == '←':
            self.expression = self.expression[:-1]
        elif char == '=':
            try:
                expr = re.sub(r'(\d+)%(\D|$)', r'(\1/100)\2', self.expression)
                self.expression = str(eval(expr))
            except Exception:
                self.expression = "에러"
        elif char == 'x²':
            try:
                self.expression = str(eval(f"({self.expression})**2"))
            except Exception:
                self.expression = "에러"
        elif char == '√':
            try:
                self.expression = str(math.sqrt(eval(self.expression)))
            except Exception:
                self.expression = "에러"
        else:
            self.expression += str(char)

        self.update_entry()

    def on_keypress(self, event):
        key = event.char

        if key in '0123456789+-*/().%':
            self.expression += key
        elif key == '\r':
            pass
        elif key == '\x08':
            self.expression = self.expression[:-1]

        self.update_entry()

    def update_entry(self):
        self.entry.delete(0, tk.END)
        self.entry.insert(tk.END, self.expression)

if __name__ == "__main__":
    root = tk.Tk()
    calc = Calculator(root)
    root.mainloop()
