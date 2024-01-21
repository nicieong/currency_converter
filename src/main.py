import requests
from tkinter import *
import tkinter.messagebox
import sys

root = Tk()
root.title("Currency Converter")
root.geometry("800x400")
root['background'] = "#F5F5F5"

base_currency_input_label = Label(root, text="Enter the base currency code: ", width=0, font=("Helvetica"))
base_currency_input_label.grid(row=1, column=0, sticky=W, padx=3, pady=0)

base_currency_input = StringVar()
base_currency_entry = Entry(root, textvariable=base_currency_input, width=20, font=("Helvetica"))
base_currency_entry.grid(row=1, column=1, sticky=W, padx=3, pady=0)

target_currency_input_label = Label(root, text="Enter the target currency code: ", width=0, font=("Helvetica"))
target_currency_input_label.grid(row=2, column=0, sticky=W, padx=3, pady=0)

target_currency_input = StringVar()
target_currency_entry = Entry(root, textvariable=target_currency_input, width=20, font=("Helvetica"))
target_currency_entry.grid(row=2, column=1, sticky=W, padx=3, pady=0)

amount_input_label = Label(root, text="Amount for the conversion: ", width=0, font=("Helvetica"))
amount_input_label.grid(row=3, column=0, sticky=W, padx=3, pady=0)

amount_input = StringVar()
amount_entry = Entry(root, textvariable=amount_input, width=20, font=("Helvetica"))
amount_entry.grid(row=3, column=1, sticky=W, padx=3, pady=0)

rate_for_amount_label = Label(root, text="Converted amount: ", width=0, font=("Helvetica"))
rate_for_amount_label.grid(row=5, column=0, sticky=W, padx=3, pady=0)

converted_amount = Label(root, text="", width=0, font=("Helvetica"))
converted_amount.grid(row=5, column=1, sticky=W, padx=3, pady=0)

rate_label = Label(root, text="Exchange Rate: ", width=0, font=("Helvetica"))
rate_label.grid(row=6, column=0, sticky=W, padx=3, pady=0)

exchange_rate = Label(root, text="", width=0, font=("Helvetica"))
exchange_rate.grid(row=6, column=1, sticky=W, padx=3, pady=0)

API_KEY = "c5172e86dcc4fa44ea0e08ff0d4c8a2522995839"

def main():
    base_currency = base_currency_entry.get().upper().strip()
    target_currency = target_currency_entry.get().upper().strip()
    amount = amount_entry.get().strip()
    
    if not base_currency or not target_currency or not amount:
        tkinter.messagebox.showerror("Error", "Please fill in all the fields")
        return
    
    amount_value = int(amount)
    if amount_value <= 0:
        tkinter.messagebox.showerror("Error", "Amount must be greater than 0")
        return
    
    api_url = f"https://api.getgeoapi.com/v2/currency/convert?api_key={API_KEY}&from={base_currency}&to={target_currency}&amount={amount}&format=json"
    
    try:
        response = requests.get(api_url)
        response.raise_for_status()
        data = response.json()
        rate_for_amount = data["rates"][target_currency]["rate_for_amount"]
        rate = data["rates"][target_currency]["rate"]
    except requests.exceptions.RequestException as e:
        tkinter.messagebox.showerror("Error", f"Cannot fetch currency exchange data because of {e}")
    except Exception as e:
        tkinter.messagebox.showerror("Error", f"An unexpected error occurred: {e}")
    
    converted_amount.configure(text=rate_for_amount)
    exchange_rate.configure(text=rate)

def exit():
    root.destroy()
    sys.exit(0)

convert_button = Button(root, text="Convert", font=("Helvetica", 15), command=main) 
convert_button.grid(row=4, column=1, padx=3, stick=W+E+N+S) 

exit_button = Button(root, text="Exit", font=("Helvetica", 15), command=exit) 
exit_button.place(x=5, y=200) 
    
root.mainloop() 
    