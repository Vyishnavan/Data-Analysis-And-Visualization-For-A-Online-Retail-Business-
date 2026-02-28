# Task 1
import pandas as pd
import sqlite3 as sq3

def create_sqlite_database(location_path, database_name):
    path = location_path + database_name # Corrected variable names
    connection = sq3.connect(path) # Use the correct path
    cur = connection.cursor()

    # Create Customer table
    cur.execute(''' 
    CREATE TABLE IF NOT EXISTS Customers(
    CustomerID INT PRIMARY KEY, 
    Country TEXT NOT NULL 
    ) 
    ''')
    
    # Create Product table
    cur.execute(''' 
    CREATE TABLE IF NOT EXISTS Products(
    StockCode TEXT PRIMARY KEY,
    Description TEXT, 
    UnitPrice REAL
    ) 
    ''')

    #Create Transaction table
    cur.execute(''' 
    CREATE TABLE IF NOT EXISTS Transactions(
    InvoiceNo TEXT PRIMARY KEY, 
    CustomerID INT, 
    StockCode TEXT, 
    Quantity INT, 
    InvoiceDate TEXT, 
    UnitPrice REAL, 
    TotalAmount_GBP REAL,
    FOREIGN KEY(CustomerID) REFERENCES Customers(CustomerID),
    FOREIGN KEY(StockCode) REFERENCES Products(StockCode)
    )
    ''')
    print('Database created.')
    return connection  # 'commit()' is unnecessary for just creating a connection
    
def populate_table(loc,fname):
    locateFile = loc + fname
    df = pd.read_csv(locateFile)
    df.dropna(inplace=True)
    return df

def writecsv_to_db(tableName, connection, df):
    df.to_sql(tableName, connection, if_exists='replace', index=False)
    print('Database created.')







    