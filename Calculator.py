
import tkinter as tk

def button_click(value):
    global expression
    expression += str(value)
    display.delete(0, tk.END)
    display.insert(tk.END, expression)


def clear():
    global expression
    expression = ""
    display.delete(0, tk.END)


def calculate():
    global expression
    try:
        result = eval(expression)
        display.delete(0, tk.END)
        display.insert(tk.END, str(result))
        expression = str(result)

    except:
        display.delete(0, tk.END)
        display.insert(tk.END, "ERROR")
        expression = ""


# Main Window
root = tk.Tk()
root.title("Blue Season Calculator")
root.geometry("320x450")
root.resizable(False, False)

# Color Palette
BG = "#A9C5E8"
FRAME = "#DCEBFF"
BORDER = "#6686B3"
NUMBER = "#FFFFFF"
OPERATOR = "#6686B3"
EQUALS = "#29466D"
TEXT = "#29466D"
WHITE = "#FFFFFF"

root.configure(bg=BG)

expression = ""

# Display
display = tk.Entry(
    root,
    font=("Arial", 26),
    bg=WHITE,
    fg=TEXT,
    justify="right",
    bd=0,
    relief="flat"
)

display.pack(
    fill="x",
    padx=18,
    pady=20,
    ipady=20
)

# Prevent manual typing
def val_input(event):
    if event.char.isdigit() or event.keysym in (
        "BackSpace", "Delete", "Left", "Right"
    ):
        return None
    return "break"

display.bind("<KeyPress>", val_input)


# Button Frame
button_frame = tk.Frame(
    root,
    bg=FRAME,
    highlightbackground=BORDER,
    highlightthickness=2
)

button_frame.pack(
    expand=True,
    fill="both",
    padx=12,
    pady=10
)

# Clear Button
clear_button = tk.Button(
    button_frame,
    text="CLEAR",
    font=("Arial", 16, "bold"),
    bg=OPERATOR,
    fg=WHITE,
    bd=0,
    activebackground="#52749F",
    command=clear
)

clear_button.grid(
    row=0,
    column=0,
    columnspan=4,
    sticky="nsew",
    padx=5,
    pady=5
)

# Calculator Buttons
buttons = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    [".", "0", "=", "+"]
]

for row_index, row in enumerate(buttons, start=1):
    for col_index, value in enumerate(row):

        if value == "=":
            command = calculate
            color = EQUALS
            text_color = WHITE

        elif value in ["+", "-", "*", "/"]:
            command = lambda v=value: button_click(v)
            color = OPERATOR
            text_color = WHITE

        else:
            command = lambda v=value: button_click(v)
            color = NUMBER
            text_color = TEXT

        button = tk.Button(
            button_frame,
            text=value,
            font=("Arial", 18, "bold"),
            bg=color,
            fg=text_color,
            bd=0,
            activebackground=BG,
            command=command
        )

        button.grid(
            row=row_index,
            column=col_index,
            sticky="nsew",
            padx=5,
            pady=5
        )

# Grid Configuration
for i in range(5):
    button_frame.grid_rowconfigure(i, weight=1)

for i in range(4):
    button_frame.grid_columnconfigure(i, weight=1)

root.mainloop()
