import sqlite3

# Class to create a local database and perform CRUD operations

class persistLocalDB:
    def __init__(self, dbPath):
        self.dbPath = dbPath
        self.conn = sqlite3.connect(self.dbPath)
        self.c = self.conn.cursor()

    # Create Pizza Table
    def createPizzaTable(self):
        self.c.execute("CREATE TABLE IF NOT EXISTS pizza (id INTEGER PRIMARY KEY, name TEXT, ingredients TEXT, price REAL)")
        self.conn.commit()
    
    # create customer table
    def createCustomerTable(self):
        self.c.execute("CREATE TABLE IF NOT EXISTS customer (id INTEGER PRIMARY KEY, name TEXT, address TEXT, phone TEXT, email TEXT)")
        self.conn.commit()
        
    # create order table
    def createOrderTable(self):
        self.c.execute("CREATE TABLE IF NOT EXISTS orders (id INTEGER PRIMARY KEY, customer_id INTEGER, order_date TEXT, order_status TEXT, order_price REAL, FOREIGN KEY(customer_id) REFERENCES customer(id))")
        self.conn.commit()
    # create ingeredients table
    # create pizza ingredients table
    # create order details table
    # create order status table
    
    # insert pizza
    def insertPizza(self, name, ingredients, price):
        self.c.execute("INSERT INTO pizza (name, ingredients, price) VALUES (?, ?, ?)", (name, ingredients, price))
        self.conn.commit()
        
    # insert customer    
    def insertCustomer(self, name, address, phone, email):
        self.c.execute("INSERT INTO customer (name, address, phone, email) VALUES (?, ?, ?, ?)", (name, address, phone, email))
        self.conn.commit()
        
    # insert order
    def insertOrder(self, customer_id, order_date, order_status, order_price):
        self.c.execute("INSERT INTO orders (customer_id, order_date, order_status, order_price) VALUES (?, ?, ?, ?)", (customer_id, order_date, order_status, order_price))
        self.conn.commit()
        
    # insert order details
    # insert ingredients
    # insert pizza ingredients 
    # ????
    
    # select pizza
    def selectPizza(self, id):
        self.c.execute("SELECT * FROM pizza WHERE id = ?", (id,))
        return self.c.fetchall()
    
    # select all pizzas
    def selectAllPizzas(self):
        self.c.execute("SELECT * FROM pizza")
        return self.c.fetchall()
    
    # select customer
    def selectCustomer(self, id):
        self.c.execute("SELECT * FROM customer WHERE id = ?", (id,))
        return self.c.fetchall()
    
    # select all customers           
    def selectAllCustomers(self):
        self.c.execute("SELECT * FROM customer")
        return self.c.fetchall()   
    
        
    # Create a tables with parameters: tableName, columns not used in this release
    def createTable(self, tableName, columns):
        self.c.execute("CREATE TABLE IF NOT EXISTS " + tableName + " (" + columns + ")")

    def insertData(self, tableName, columns, values):
        self.c.execute("INSERT INTO " + tableName + " (" + columns + ") VALUES (" + values + ")")
        self.conn.commit()

    def selectData(self, tableName, columns, condition):
        self.c.execute("SELECT " + columns + " FROM " + tableName + " WHERE " + condition)
        return self.c.fetchall()

    def updateData(self, tableName, columns, values, condition):
        self.c.execute("UPDATE " + tableName + " SET " + columns + " = " + values + " WHERE " + condition)
        self.conn.commit()

    def deleteData(self, tableName, condition):
        self.c.execute("DELETE FROM " + tableName + " WHERE " + condition)
        self.conn.commit()
    
    # not used in this release    

    def closeConnection(self):
        self.conn.close()
        
if __name__ == '__main__':
    # Create a local database
    localDB = persistLocalDB("pizza.db")
    # Create tables
    localDB.createPizzaTable()
    localDB.createCustomerTable()
    localDB.createOrderTable()
    # insert pizzas
    localDB.insertPizza("Pepperoni", "Pepperoni, Cheese, Sauce", 44.99)
    localDB.insertPizza("Hawaiian", "Ham, Pineapple, Cheese, Sauce", 55.99)
    localDB.insertPizza("Meat Lovers", "Pepperoni, Ham, Sausage, Bacon, Cheese, Sauce", 66.99)
    
    # insert customers
    localDB.insertCustomer("John Smith", "123 Main St", "555-555-5555", "john@mail.dk")
    localDB.insertCustomer("Jane Doe", "456 Main St", "555-555-5555", "jane@mail.dk")
    
    # insert orders
    localDB.insertOrder(1, "2020-01-01", "In Progress", 44.99)
    localDB.insertOrder(2, "2020-01-01", "In Progress", 55.99)
    
    # select pizzas
    print(localDB.selectAllPizzas())
    print(localDB.selectPizza(1))
    
        