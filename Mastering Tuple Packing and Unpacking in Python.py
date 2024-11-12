# Task 1: Customer Order Processing Refine your skills in tuple unpacking by managing customer orders.

# Problem Statement: You are given a list of tuples, each representing a customer's order. Each tuple contains the customer's
# name, the product ordered, and the quantity. Your task is to unpack each tuple and print the order details in a user-friendly format.


# Sample Order Data:

# orders = [
#     ("Alice", "Laptop", 1),
#     ("Bob", "Camera", 2),
#     # More orders...
# ]
# - Write a function to iterate over the list of orders. - Unpack each tuple in the list and format the details for display.





def new_product_info(orders):
    name = input("Enter the name of the customer: ").lower().title()
    product = input("Enter name of the product ordered: ").lower().title()
    quantity = int(input("Enter the quantity of number of items ordered in interger form: "))

    orders.append((name, product, quantity))


def order_lists(orders):
    for name, product, quantity in orders:
        print(f"Customer Name: {name} -- Product Ordered: {product} -- Quantity: {quantity}")


def main():

    orders = [
    ("Alice", "Laptop", 1),
    ("Bob", "Camera", 2),
    # More orders...
]
    

    while True:
        add_orders = input("Would you like to add a new order (yes/no): ").lower()

        if add_orders == "yes":
            new_product_info(orders)

        elif add_orders == "no":
            print("Great, this is the order summary: ")
            order_lists(orders)
            break
        
        else:
            print("Invalid Entry.")

main()




