from tkinter import Tk, Label, Button, Entry, DoubleVar
from datetime import datetime

def start():
    root = Tk()
    root.geometry("1920x1080")

    root.title(f"Granja Martinez - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

    label = Label(root, text="Granja Martinez", font=("Arial", 24))
    label.pack()

    product_name = Label(root, text="Nombre producto:", font=("Arial", 18))
    name_entry = Entry(root, font=("Arial", 18))
    product_name.pack()
    name_entry.pack()

    product_price = Label(root, text="Precio producto:", font=("Arial", 18))
    price_entry = Entry(root, font=("Arial", 18))
    product_price.pack()
    price_entry.pack()

    total_var = DoubleVar(value=0.0)

    add_button = Button(root, text="Agregar producto", font=("Arial", 18),
                        command=lambda: add_entry(root, name_entry, price_entry, total_var, total_label))
    add_button.pack()

    total_label = Label(root, text="Total: 0.0", font=("Arial", 18))
    total_label.pack()
    

    root.mainloop()

def add_entry(root, name_entry, price_entry, total_var: DoubleVar, total_label: Label):
    name = name_entry.get().strip()
    price_text = price_entry.get().strip()

    try:
        price = float(price_text) if price_text else 0.0
    except ValueError:
        price = 0.0
        err = Label(root, text=f"Precio inválido: '{price_text}' — se tomó como 0", fg="red", font=("Arial", 12))
        err.pack()

    product_name = Label(root, text=name or "(sin nombre)", font=("Arial", 18))
    product_name.pack()

    product_price = Label(root, text=f"{price:.2f}", font=("Arial", 18))
    product_price.pack()

    total_var.set(total_var.get() + price)
    total_label.config(text="Total: " + str(total_var.get()))

    name_entry.delete(0, 'end')
    price_entry.delete(0, 'end')


start()