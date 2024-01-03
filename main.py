# gui_invoicing.py
import tkinter as tk
from tkinter import messagebox


class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Invoice:
    def __init__(self, customer_name):
        self.customer_name = customer_name
        self.items = []

    def add_item(self, product, quantity=1):
        self.items.append({"product": product, "quantity": quantity})

    def calculate_total(self):
        total = sum(item["product"].price * item["quantity"] for item in self.items)
        return total

    def generate_invoice(self):
        invoice_text = f"Invoice for {self.customer_name}:\n"
        for item in self.items:
            invoice_text += f"{item['product'].name} - {item['quantity']} units - ${item['product'].price * item['quantity']}\n"
        invoice_text += f"Total: ${self.calculate_total()}"
        return invoice_text


class InvoicingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Invoicing Program")

        self.product1 = Product("Product A", 20.0)
        self.product2 = Product("Product B", 30.0)

        self.invoice = Invoice("John Doe")

        self.create_widgets()

    def create_widgets(self):
        # Customer Name Entry
        tk.Label(self.root, text="Customer Name:").pack()
        self.customer_name_entry = tk.Entry(self.root)
        self.customer_name_entry.pack()

        # Product Selection
        tk.Label(self.root, text="Select Product:").pack()

        self.product_var = tk.StringVar()
        self.product_var.set("Product A")

        product_options = ["Product A", "Product B"]
        product_dropdown = tk.OptionMenu(self.root, self.product_var, *product_options)
        product_dropdown.pack()

        # Quantity Entry
        tk.Label(self.root, text="Quantity:").pack()
        self.quantity_entry = tk.Entry(self.root)
        self.quantity_entry.pack()

        # Add Item Button
        tk.Button(self.root, text="Add Item", command=self.add_item).pack()

        # Generate Invoice Button
        tk.Button(self.root, text="Generate Invoice", command=self.generate_invoice).pack()

    def add_item(self):
        product_name = self.product_var.get()
        quantity = int(self.quantity_entry.get())

        if product_name == "Product A":
            product = self.product1
        elif product_name == "Product B":
            product = self.product2
        else:
            messagebox.showerror("Error", "Invalid product selection.")
            return

        self.invoice.add_item(product, quantity)
        messagebox.showinfo("Item Added", f"{quantity} units of {product_name} added to the invoice.")

    def generate_invoice(self):
        customer_name = self.customer_name_entry.get()
        if not customer_name:
            messagebox.showerror("Error", "Customer name cannot be empty.")
            return

        invoice_text = self.invoice.generate_invoice()
        messagebox.showinfo("Generated Invoice", invoice_text)


if __name__ == "__main__":
    root = tk.Tk()
    app = InvoicingApp(root)
    root.mainloop()
