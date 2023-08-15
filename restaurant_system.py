class MenuItem:
    def __init__(self, name, description, price, ingredients) :
        self.name = name
        self.description = description
        self.price = price
        self.ingredientes = ingredients

class Order:
    def __init__ (self):
        self.items = []
    
    def add_item(self, item):
        self.items.append(item)
    
    def calculate_total(self):
        total = sum(item.price for item in self.item)
        return total

class Table:
    def __init__(self, table_number):
        self.table_number = table_number
        self.orders = []

    def place_order(self, order):
        self.orders.append(order)

class Restaurant:
    def __init__(self, name):
        self.name = name
        self.tables = []

    def add_tables(self, table):
        self.tables.append(table)

    def get_table_by_number(self, table_number):
        for table in self.tables:
            if table.table_number == table_number:
                return table
        return None

# Create menu items:
burger = MenuItem("Burger", "Juicy beef burger", 10.99, ["beef patty", "lettuce", "tomato"])
pizza = MenuItem("Pizza", "Classic Margherita", 12.99, ["dough", "tomato sauce", "cheese"])

#Create orders
order1 = Order()
order1.add_item(burger)
order1.add_item(pizza)

#create tables
table1 = Table(1)
table1.place_order(order1)

#create restaurant
restaurant = Restaurant("My Restaurant")
restaurant.add_tables(table1)

#Print total for a table;s order
table = restaurant.get_table_by_number(1)
if table:
    total = table.orders[0].calculate_total()
    print(f"Table {table.table_number} total: $ {total}")
else:
    print ("Table not found")