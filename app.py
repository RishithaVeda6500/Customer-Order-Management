import database

def main():
    while True:
        print("\nCustomer Order Management")
        print("1. Add Customer")
        print("2. Place Order")
        print("3. View Customers")
        print("4. View Orders")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            name = input("Enter customer name: ")
            email = input("Enter customer email: ")
            database.add_customer(name, email)

        elif choice == "2":
            customer_id = input("Enter customer ID: ")
            product = input("Enter product name: ")
            quantity = input("Enter quantity: ")
            database.place_order(customer_id, product, int(quantity))

        elif choice == "3":
            customers = database.get_customers()
            for c in customers:
                print(c)

        elif choice == "4":
            orders = database.get_orders()
            for o in orders:
                print(o)

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
