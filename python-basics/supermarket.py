import tkinter as tk
from tkinter import messagebox
import sqlite3
import datetime

# ================= DATABASE SETUP =================

conn = sqlite3.connect("supermarket_pos.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS products(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    price REAL,
    stock INTEGER
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS sales(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    total REAL,
    payment REAL,
    change REAL,
    date TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS sale_items(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    sale_id INTEGER,
    product_name TEXT,
    quantity INTEGER,
    price REAL
)
""")

conn.commit()

# ================= POS APP =================

class POS:
    def __init__(self, root):
        self.root = root
        self.root.title("Supermarket POS System")
        self.cart = []

        # Product Section
        tk.Label(root, text="Product Name").grid(row=0, column=0)
        tk.Label(root, text="Quantity").grid(row=0, column=2)

        self.product_entry = tk.Entry(root)
        self.product_entry.grid(row=0, column=1)

        self.qty_entry = tk.Entry(root)
        self.qty_entry.grid(row=0, column=3)

        tk.Button(root, text="Add to Cart", command=self.add_to_cart).grid(row=0, column=4)

        # Cart List
        self.cart_list = tk.Listbox(root, width=70)
        self.cart_list.grid(row=1, column=0, columnspan=5)

        # Total
        self.total_label = tk.Label(root, text="Total: $0.00", font=("Arial", 14))
        self.total_label.grid(row=2, column=0, columnspan=2)

        tk.Label(root, text="Payment").grid(row=3, column=0)
        self.payment_entry = tk.Entry(root)
        self.payment_entry.grid(row=3, column=1)

        tk.Button(root, text="Checkout", command=self.checkout).grid(row=3, column=2)

    # ================= ADD TO CART =================
    def add_to_cart(self):
        name = self.product_entry.get()
        qty = int(self.qty_entry.get())

        cursor.execute("SELECT price, stock FROM products WHERE name=?", (name,))
        product = cursor.fetchone()

        if product:
            price, stock = product

            if qty <= stock:
                total_price = price * qty
                self.cart.append((name, qty, price, total_price))
                self.update_cart()
            else:
                messagebox.showerror("Error", "Not enough stock!")
        else:
            messagebox.showerror("Error", "Product not found!")

    # ================= UPDATE CART =================
    def update_cart(self):
        self.cart_list.delete(0, tk.END)
        total = 0

        for item in self.cart:
            name, qty, price, total_price = item
            self.cart_list.insert(tk.END, f"{name} x{qty} - ${total_price:.2f}")
            total += total_price

        self.total_label.config(text=f"Total: ${total:.2f}")

    # ================= CHECKOUT =================
    def checkout(self):
        payment = float(self.payment_entry.get())
        total = sum(item[3] for item in self.cart)

        if payment < total:
            messagebox.showerror("Error", "Insufficient payment!")
            return

        change = payment - total
        date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Save sale
        cursor.execute("INSERT INTO sales (total, payment, change, date) VALUES (?, ?, ?, ?)",
                       (total, payment, change, date))
        sale_id = cursor.lastrowid

        for item in self.cart:
            name, qty, price, total_price = item
            cursor.execute("INSERT INTO sale_items (sale_id, product_name, quantity, price) VALUES (?, ?, ?, ?)",
                           (sale_id, name, qty, price))

            cursor.execute("UPDATE products SET stock = stock - ? WHERE name=?", (qty, name))

        conn.commit()

        # Print receipt
        self.print_receipt(sale_id, total, payment, change, date)

        messagebox.showinfo("Success", f"Change: ${change:.2f}")
        self.cart.clear()
        self.update_cart()

    # ================= RECEIPT =================
    def print_receipt(self, sale_id, total, payment, change, date):
        with open(f"receipt_{sale_id}.txt", "w") as f:
            f.write("===== SUPERMARKET RECEIPT =====\n")
            f.write(f"Date: {date}\n\n")

            for item in self.cart:
                name, qty, price, total_price = item
                f.write(f"{name} x{qty} - ${total_price:.2f}\n")

            f.write("\n------------------------------\n")
            f.write(f"Total: ${total:.2f}\n")
            f.write(f"Payment: ${payment:.2f}\n")
            f.write(f"Change: ${change:.2f}\n")
            f.write("==============================\n")

# ================= RUN APP =================

root = tk.Tk()
app = POS(root)
root.mainloop()