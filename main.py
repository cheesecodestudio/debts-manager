
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
import os


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r".\\assets\\imgs")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("620x468")
window.configure(bg = "#FFFFFF")
window.title("Administración de finanzas")

canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 468,
    width = 620,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)

# Label to visualize incomes ========================================================== #
image_rect_green = PhotoImage(
    file=relative_to_assets("rect_green.png"))
rect_green = canvas.create_image(
    85.0,
    39.0,
    image=image_rect_green
)

canvas.create_text(
    25.0,
    19.0,
    anchor="nw",
    text="Ingresos",
    fill="#1E1E1E",
    font=("RocknRollOne Regular", 14 * -1)
)

canvas.create_text(
    25.0,
    39.0,
    anchor="nw",
    text="₡ 100,000.00",
    fill="#1E1E1E",
    font=("RocknRollOne Regular", 12 * -1)
)

# Label to visualize expenses ========================================================== #
image_rect_red = PhotoImage(
    file=relative_to_assets("rect_red.png"))
rect_red = canvas.create_image(
    247.0,
    39.0,
    image=image_rect_red
)

canvas.create_text(
    187.0,
    39.0,
    anchor="nw",
    text="₡ 20,000.00",
    fill="#1E1E1E",
    font=("RocknRollOne Regular", 12 * -1)
)

canvas.create_text(
    187.0,
    19.0,
    anchor="nw",
    text="Gastos",
    fill="#1E1E1E",
    font=("RocknRollOne Regular", 14 * -1)
)

# Label to visualize balances ========================================================== #
image_rect_blue = PhotoImage(
    file=relative_to_assets("rect_blue.png"))
rect_blue = canvas.create_image(
    166.0,
    99.0,
    image=image_rect_blue
)

canvas.create_text(
    25.0,
    99.0,
    anchor="nw",
    text="₡ 80,000.00",
    fill="#1E1E1E",
    font=("RocknRollOne Regular", 12 * -1)
)

canvas.create_text(
    25.0,
    79.0,
    anchor="nw",
    text="Restante",
    fill="#1E1E1E",
    font=("RocknRollOne Regular", 14 * -1)
)

# Incomes Section ========================================================== #
canvas.create_text(
    15.0,
    139.0,
    anchor="nw",
    text="Ingreso",
    fill="#1E1E1E",
    font=("RocknRollOne Regular", 20 * -1)
)

canvas.create_text(
    15.0,
    166.0,
    anchor="nw",
    text="Monto",
    fill="#1E1E1E",
    font=("RocknRollOne Regular", 12 * -1)
)

amount_incomes_entry_image = PhotoImage(
    file=relative_to_assets("rect_entry.png"))
amount_incomes_entry_bg = canvas.create_image(
    90.0,
    198.5,
    image=amount_incomes_entry_image
)

amount_incomes_entry = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
amount_incomes_entry.place(
    x=23.0,
    y=186.0,
    width=134.0,
    height=23.0
)

incomes_button_image = PhotoImage(
    file=relative_to_assets("button_add.png"))
incomes_button = Button(
    image=incomes_button_image,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("Incomes clicked"),
    relief="flat"
)
incomes_button.place(
    x=15.0,
    y=218.0,
    width=150.0,
    height=25.0
)

# Expenses Section ========================================================== #
canvas.create_text(
    15.0,
    263.0,
    anchor="nw",
    text="Gasto",
    fill="#1E1E1E",
    font=("RocknRollOne Regular", 20 * -1)
)

canvas.create_text(
    15.0,
    290.0,
    anchor="nw",
    text="Monto",
    fill="#1E1E1E",
    font=("RocknRollOne Regular", 12 * -1)
)

amount_expenses_entry_image = PhotoImage(
    file=relative_to_assets("rect_entry.png"))
amount_expenses_entry_bg = canvas.create_image(
    90.0,
    322.5,
    image=amount_expenses_entry_image
)
amount_expenses_entry = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
amount_expenses_entry.place(
    x=23.0,
    y=310.0,
    width=134.0,
    height=23.0
)

canvas.create_text(
    15.0,
    342.0,
    anchor="nw",
    text="Tipo",
    fill="#1E1E1E",
    font=("RocknRollOne Regular", 12 * -1)
)

# ToDo: Replace to Dropdown
type_expenses_entry_image = PhotoImage(
    file=relative_to_assets("rect_entry.png"))
type_expenses_entry_bg = canvas.create_image(
    90.0,
    374.5,
    image=type_expenses_entry_image
)
type_expenses_entry = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
type_expenses_entry.place(
    x=23.0,
    y=362.0,
    width=134.0,
    height=23.0
)

expenses_button_image = PhotoImage(
    file=relative_to_assets("button_add.png"))
expenses_button = Button(
    image=expenses_button_image,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("expenses clicked"),
    relief="flat"
)
expenses_button.place(
    x=15.0,
    y=394.0,
    width=150.0,
    height=25.0
)

# General buttons ========================================================== #
report_button_image = PhotoImage(
    file=relative_to_assets("report_button.png"))
report_button = Button(
    image=report_button_image,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("report clicked"),
    relief="flat"
)
report_button.place(
    x=348.0,
    y=428.0,
    width=120.0,
    height=25.0
)

save_button_image = PhotoImage(
    file=relative_to_assets("save_button.png"))
save_button = Button(
    image=save_button_image,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("save clicked"),
    relief="flat"
)
save_button.place(
    x=480.0,
    y=428.0,
    width=120.0,
    height=25.0
)

# List of entries ========================================================== #
canvas.create_text(
    346.0,
    15.0,
    anchor="nw",
    text="Lista de movimientos",
    fill="#1E1E1E",
    font=("RocknRollOne Regular", 20 * -1)
)

clean_entries_button_image = PhotoImage(
    file=relative_to_assets("button_5.png"))
clean_entries_button = Button(
    image=clean_entries_button_image,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_5 clicked"),
    relief="flat"
)
clean_entries_button.place(
    x=572.0,
    y=17.0,
    width=33.0,
    height=25.0
)

# ToDo: Replace to Table
image_image_4 = PhotoImage(
    file=relative_to_assets("image_4.png"))
image_4 = canvas.create_image(
    475.0,
    95.0,
    image=image_image_4
)

# Separator
canvas.create_rectangle(
    326.04014579928094,
    18.00372314453125,
    330.5,
    421.0001611770167,
    fill="#AEAEAE",
    outline="")

window.resizable(False, False)
window.mainloop()
