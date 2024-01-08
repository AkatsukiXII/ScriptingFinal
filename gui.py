import tkinter as tk
import sqlite3

def open_new_window(parent, title, geometry):
    """
    Open a new window with given title and geometry.
    """
    new_window = tk.Toplevel(parent)
    new_window.title(title)
    new_window.geometry(geometry)
    return new_window

def add_button(parent, text, command, width=20):
    """
    Add a button to a given parent widget.
    """
    button = tk.Button(parent, text=text, command=command, width=width)
    button.pack(pady=10)

def open_query_window():
    query_window = open_new_window(window, "查詢資料", "250x250")
    add_button(query_window, "客戶資料", open_customer)
    add_button(query_window, "商品資料", open_product)
    add_button(query_window, "門市資料", open_store)
    add_button(query_window, "交易資料", open_trade)

def open_add_window():
    add_window = open_new_window(window, "新增資料", "250x250")
    # Add widgets for adding data here

def open_customer():
    """
    Open a new window for customer data and display data from the database.
    """
    customer_window = open_new_window(window, "客戶資料", "800x800")
    
    text_area = tk.Text(customer_window, height=40, width=100)
    text_area.pack()

    data = fetch_customer_data()
    text_area.insert(tk.END, "客戶資料:\n")
    for row in data:
        text_area.insert(tk.END, f'cid:{row[0]} ,cname:{row[1]}, cphone:{row[2]}, cadd:{row[3]}\n')
    text_area.config(state='disabled')  # Make the text area read-only


def fetch_customer_data():
    """
    Fetch customer data from the database and return it.
    """
    try:
        conn = sqlite3.connect('C:/Users/94202/Desktop/Final/SQL/final.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM customer')
        result = cursor.fetchall()
        conn.close()
        return result
    except sqlite3.Error as e:
        print("Database error:", e)
        return []


def open_product():
    product_window = open_new_window(window, "商品資料", "1000x1000")
    text_area = tk.Text(product_window, height=40, width=100)
    text_area.pack()

    data = fetch_product_data()
    text_area.insert(tk.END, "商品資料:\n")
    for row in data:
        text_area.insert(tk.END, f'pid:{row[0]} ,pname:{row[1]}, price:{row[2]}, pstock:{row[3]}\t\n')
    text_area.config(state='disabled')  # Make the text area read-only

def fetch_product_data():
    """
    Fetch customer data from the database and return it.
    """
    try:
        conn = sqlite3.connect('C:/Users/94202/Desktop/Final/SQL/final.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM product')
        result = cursor.fetchall()
        conn.close()
        return result
    except sqlite3.Error as e:
        print("Database error:", e)
        return []

def open_store():
    store_window = open_new_window(window, "門市資料", "1000x1000")
    # Add widgets for store data here
    text_area = tk.Text(store_window, height=40, width=100)
    text_area.pack()

    data = fetch_store_data()
    text_area.insert(tk.END, "門市資料:\n")
    for row in data:
        text_area.insert(tk.END, f'sid:{row[0]} ,scode:{row[1]}, sname:{row[2]}, sadd:{row[3]}\n')
    text_area.config(state='disabled')  # Make the text area read-only

def fetch_store_data():
    """
    Fetch customer data from the database and return it.
    """
    try:
        conn = sqlite3.connect('C:/Users/94202/Desktop/Final/SQL/final.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM store')
        result = cursor.fetchall()
        conn.close()
        return result
    except sqlite3.Error as e:
        print("Database error:", e)
        return []
    
def open_trade():
    trade_window = open_new_window(window, "交易資料", "1000x1000")
    # Add widgets for trade data here
    text_area = tk.Text(trade_window, height=40, width=100)
    text_area.pack()

    data = fetch_trade_data()
    text_area.insert(tk.END, "交易資料:\n")
    for row in data:
        text_area.insert(tk.END, f'cid:{row[0]} ,cname:{row[1]}, cphone:{row[2]}, cadd:{row[3]}\n')
    text_area.config(state='disabled')  # Make the text area read-only
    
def fetch_trade_data():
    """
    Fetch customer data from the database and return it.
    """
    try:
        conn = sqlite3.connect('C:/Users/94202/Desktop/Final/SQL/final.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM trade')
        result = cursor.fetchall()
        conn.close()
        return result
    except sqlite3.Error as e:
        print("Database error:", e)
        return []
# Create the main window
window = tk.Tk()
window.title("主頁面")
window.geometry("250x100")

# Create buttons for the main window
add_button(window, "查詢資料", open_query_window)
add_button(window, "新增資料", open_add_window)

# Start the GUI event loop
window.mainloop()
