import sqlite3

# Connect to database
conn = sqlite3.connect('orders.db')
cursor = conn.cursor()

# Function to add a customer
def add_customer(name, email):
    cursor.execute("INSERT INTO customers (name, email) VALUES (?, ?)", (name, email))
    conn.commit()
    print(f"Customer {name} added.")

# Function to place an order
def place_order(customer_id, product, quantity):
    cursor.execute("INSERT INTO orders (customer_id, product, quantity) VALUES (?, ?, ?)", (customer_id, product, quantity))
    conn.commit()
    print(f"Order placed for {product} (Quantity: {quantity})")

# Function to fetch all customers
def get_customers():
    cursor.execute("SELECT * FROM customers")
    return cursor.fetchall()

# Function to fetch all orders
def get_orders():
    cursor.execute("SELECT * FROM orders")
    return cursor.fetchall()
