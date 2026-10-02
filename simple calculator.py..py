import tkinter as tk

# Create app window
app = tk.Tk()
app.title("Calculator")
app.geometry("350x500")
app.resizable(False, False)

# Display
display = tk.Entry(
    app,
    font=("Arial", 28),
    justify="right",
    bd=10
)
display.pack(fill="x", padx=10, pady=10, ipady=15)


# Functions
def button_click(value):
    display.insert(tk.END, value)


def clear():
    display.delete(0, tk.END)


def calculate():
    try:
        result = eval(display.get())
        display.delete(0, tk.END)
        display.insert(0, str(result))
    except:
        display.delete(0, tk.END)
        display.insert(0, "Error")


# Button frame
button_frame = tk.Frame(app)
button_frame.pack(fill="both", expand=True, padx=10, pady=10)


# Buttons
buttons = [
    ("7", 0, 0), ("8", 0, 1), ("9", 0, 2), ("/", 0, 3),
    ("4", 1, 0), ("5", 1, 1), ("6", 1, 2), ("*", 1, 3),
    ("1", 2, 0), ("2", 2, 1), ("3", 2, 2), ("-", 2, 3),
    ("0", 3, 0), (".", 3, 1), ("=", 3, 2), ("+", 3, 3)
]


# Create buttons
for text, row, column in buttons:

    if text == "=":
        button = tk.Button(
            button_frame,
            text=text,
            font=("Arial", 20),
            command=calculate
        )
    else:
        button = tk.Button(
            button_frame,
            text=text,
            font=("Arial", 20),
            command=lambda value=text: button_click(value)
        )

    button.grid(
        row=row,
        column=column,
        padx=5,
        pady=5,
        sticky="nsew"
    )


# Clear button
clear_button = tk.Button(
    button_frame,
    text="C",
    font=("Arial", 20),
    command=clear
)

clear_button.grid(
    row=4,
    column=0,
    columnspan=4,
    padx=5,
    pady=5,
    sticky="nsew"
)


# Make buttons expand
for i in range(4):
    button_frame.columnconfigure(i, weight=1)

for i in range(5):
    button_frame.rowconfigure(i, weight=1)


# Start calculator
app.mainloop()
