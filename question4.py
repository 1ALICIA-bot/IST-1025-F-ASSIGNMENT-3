
def input_sales_data(num_salemen, num_items):
    sales_data = {}

    for _ in range(num_salemen):
        salesman_name = input("Enter salesman name: ")
    

    for item_index in range(1, num_items + 1):
        while True:
            try:
                sales = float(input(f"Enter sales for item {item_index}: "))
                break
            except ValueError:
                print("Invalid input. Please enter a valid number.")

        sales_data[salesman_name] = sales

    return sales_data

def display_sales_data(sales_data):
    print("\nName\tItem1\tItem2\tItem3\tItem4\tItem5\tTotalSales")
    print("____________________________________________________")

    grand_total = 0
    for salesman, sales in sales_data.items():
        total_sales = sum(sales)
        grand_total += total_sales
        sales_str ="\t".join(map(str, sales))
        print(f"{salesman}\t{sales_str}\t{total_sales}" )

        print("________________________________________________")
        print(f"Grand Total\t{grand_total}")
       

num_salesmen=2
num_items=5

sales_data = input_sales_data(num_salesmen, num_items)
display_sales_data(sales_data)
