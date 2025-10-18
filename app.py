from tkinter import Tk, Label, Button, Entry, DoubleVar
from datetime import datetime

def start():
    root = Tk()
    root.geometry("1920x1080")

    root.title(f"Granja Martinez - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

    label = Label(root, text="Granja Martinez", font=("Arial", 24))
    label.pack()

    name_entry = create_field(root, "Nombre producto:")
    price_entry = create_field(root, "Precio producto:")

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

    new_product(root, name, price, total_var, total_label)

    update_total(price, total_var, total_label)

    name_entry.delete(0, 'end')
    price_entry.delete(0, 'end')

def update_total(price: float, total_var: DoubleVar, total_label: Label):
    total_var.set(total_var.get() + price)
    total_label.config(text="Total: " + str(total_var.get()))


def create_field(root, label_text):
    label = Label(root, text=label_text, font=("Arial", 18))
    entry = Entry(root, font=("Arial", 18))
    label.pack()
    entry.pack()
    return entry

def new_product(root, name, price, total_var: DoubleVar, total_label: Label):
    product_name = Label(root, text=name or "(sin nombre)", font=("Arial", 18) )
    product_name.pack()

    product_price = Label(root, text=f"{price:.2f}", font=("Arial", 18))
    product_price.pack()

    delete_button = Button(root, text="Eliminar", font=("Arial", 14),
                           command=lambda: [product_name.destroy(), product_price.destroy(), delete_button.destroy(),
                                            update_total(-price, total_var, total_label)])
    delete_button.pack()


start()