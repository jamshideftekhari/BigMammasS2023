import mysql.connector

class PersistMySql:
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.connection = None
        self.cursor = None

    def connect(self):
        self.connection = mysql.connector.connect(host=self.host, user=self.user, password=self.password, database=self.database)
        self.cursor = self.connection.cursor()

    def close(self):
        self.connection.close()
        
    def select(self, query):
        self.cursor.execute(query)
        return self.cursor.fetchall()
    
    def insertQuery(self):
        #self.cursor.execute(query)
        self.cursor.execute("""INSERT INTO pizza values (61, 'BIG MAMMA','Tomato & Cheese & gorgonzola & shirimp & aspargas & parma ham', 90);""")
        self.connection.commit()
        
    # for later use
    def insert(self, query, value):
        self.cursor.executemany(query, value)
        print(self.cursor.rowcount())
        self.connection.commit()

    def delete(self, query):
        self.cursor.execute(query)
        self.connection.commit()

    def update(self, query, values):
        self.cursor.execute(query, values)
        self.connection.commit()
        
if __name__ == '__main__':
    dbHost = "localhost"
    dbUser = "root"
    dbpassword = "jam2003eft"
    dbDatabase = "bigmamma2023"
    BigMammaDB = PersistMySql(dbHost, dbUser, dbpassword, dbDatabase)   
    
    BigMammaDB.connect()
    print(BigMammaDB.select("SELECT * FROM pizza"))
    pizzaName = "Test"
    pizzaIngredients = "ingredients"
    BigMammaDB.insertQuery()
    BigMammaDB.close()