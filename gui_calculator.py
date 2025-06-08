# gui_calculator.py
import tkinter as tk

expression = ""

def press(symbol):
    global expression
    expression += str(symbol)
    equation.set(expression)

def evaluate():
    global expression
    try:
        result = str(eval(expression))
        equation.set(result)
        expression = result
    except:
        equation.set("Error")
        expression = ""

def clear():
    global expression
    expression = ""
    equation.set("")

# Create GUI window
root = tk.Tk()
root.title("Calculator")
root.geometry("300x400")

equation = tk.StringVar()

display = tk.Entry(root, textvariable=equation, font=('Arial', 20), bd=10, insertwidth=2, width=14, borderwidth=4, justify='right')
display.grid(row=0, column=0, columnspan=4)

# Button definitions
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('C', 4, 2), ('+', 4, 3),
    ('=', 5, 0, 4)
]

for (text, row, col, colspan) in [(*btn, 1) if len(btn) == 3 else btn for btn in buttons]:
    action = evaluate if text == '=' else clear if text == 'C' else lambda x=text: press(x)
    tk.Button(root, text=text, padx=20, pady=20, font=('Arial', 18), command=action)\
        .grid(row=row, column=col, columnspan=colspan, sticky="nsew")

# Make rows/columns expand to fill space
for i in range(6):
    root.grid_rowconfigure(i, weight=1)
    root.grid_columnconfigure(i, weight=1)

root.mainloop()
