import tkinter as tk
from tkinter import ttk

class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Simple Calculator")
        master.geometry("300x400")
        master.configure(bg="#f0f0f0")

        self.result_var = tk.StringVar()
        self.result_var.set("0")

        self.create_widgets()

    def create_widgets(self):
        # Result display
        result_display = ttk.Entry(self.master, textvariable=self.result_var, justify="right", font=("Arial", 24))
        result_display.grid(row=0, column=0, columnspan=4, padx=5, pady=5, sticky="nsew")

        # Buttons
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+'
        ]

        row = 1
        col = 0
        for button in buttons:
            cmd = lambda x=button: self.click(x)
            ttk.Button(self.master, text=button, command=cmd).grid(row=row, column=col, padx=5, pady=5, sticky="nsew")
            col += 1
            if col > 3:
                col = 0
                row += 1

        # Clear button
        ttk.Button(self.master, text="C", command=self.clear).grid(row=row, column=col, padx=5, pady=5, sticky="nsew")

        # Configure grid
        for i in range(5):
            self.master.grid_rowconfigure(i, weight=1)
        for i in range(4):
            self.master.grid_columnconfigure(i, weight=1)

    def click(self, key):
        if key == '=':
            try:
                result = eval(self.result_var.get())
                self.result_var.set(result)
            except:
                self.result_var.set("Error")
        else:
            if self.result_var.get() == "0" or self.result_var.get() == "Error":
                self.result_var.set(key)
            else:
                self.result_var.set(self.result_var.get() + key)

    def clear(self):
        self.result_var.set("0")