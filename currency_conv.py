# ----------------------------
# Currency Converter - GUI App
# By: Rithvik Reddy Gudipati
# Internship Project - CodeClause
# ----------------------------

import tkinter as tk
from tkinter import ttk, messagebox
import requests

API_KEY = "619e38f2216cb880ea252399"

currency_list = ["USD", "INR", "EUR", "GBP", "JPY", "AUD", "CAD", "CNY"]

# Function to get live rates for a selected base currency
def get_exchange_rates(base_currency):
    url = f"https://v6.exchangerate-api.com/v6/{API_KEY}/latest/{base_currency}"

    try:
        response = requests.get(url)
        data = response.json()
        return data["conversion_rates"]
    except:
        messagebox.showerror("Error", "Could not connect to exchange rate API.")
        return None

def perform_conversion():
    try:
        amount = float(amount_input.get())
        from_curr = from_combo.get()
        to_curr = to_combo.get()

        if from_curr == to_curr:
            result_label.config(text="Both currencies are the same.")
            return

        rates = get_exchange_rates(from_curr)
        if rates and to_curr in rates:
            result = amount * rates[to_curr]
            result_label.config(text=f"{amount} {from_curr} = {round(result, 2)} {to_curr}")
        else:
            result_label.config(text="Conversion failed.")
    except ValueError:
        messagebox.showwarning("Invalid Input", "Please enter a valid amount.")

def clear_fields():
    amount_input.delete(0, tk.END)
    result_label.config(text="")
    from_combo.set("USD")
    to_combo.set("INR")

# ---------------- UI SETUP ----------------
root = tk.Tk()
root.title("Currency Converter - Rithvik")
root.geometry("360x350")
root.configure(bg="#f5f5f5")

title_label = tk.Label(root, text="💱 Currency Converter", font=("Segoe UI", 16, "bold"), bg="#f5f5f5")
title_label.pack(pady=10)

tk.Label(root, text="Amount", bg="#f5f5f5").pack()
amount_input = tk.Entry(root, font=("Arial", 12), justify="center")
amount_input.pack(pady=5)

tk.Label(root, text="From Currency", bg="#f5f5f5").pack()
from_combo = ttk.Combobox(root, values=currency_list, state="readonly", width=15, justify="center")
from_combo.set("USD")
from_combo.pack(pady=5)

tk.Label(root, text="To Currency", bg="#f5f5f5").pack()
to_combo = ttk.Combobox(root, values=currency_list, state="readonly", width=15, justify="center")
to_combo.set("INR")
to_combo.pack(pady=5)

convert_btn = tk.Button(root, text="Convert", command=perform_conversion, bg="#4CAF50", fg="white", font=("Arial", 12, "bold"))
convert_btn.pack(pady=10)

clear_btn = tk.Button(root, text="Clear", command=clear_fields, bg="#d9534f", fg="white", font=("Arial", 10))
clear_btn.pack(pady=2)

result_label = tk.Label(root, text="", font=("Segoe UI", 14), bg="#f5f5f5", fg="#333")
result_label.pack(pady=15)

root.mainloop()
