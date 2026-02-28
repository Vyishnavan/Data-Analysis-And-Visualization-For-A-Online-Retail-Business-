# Task 2
import pandas as pd
import sqlite3 as sq3

# The total quantity sold for each product monthly
def Total_quantity_sold(connection):
    query = """SELECT STRFTIME('%Y-%m', InvoiceDate) AS Month, StockCode, SUM(Quantity) AS Quantity FROM Transactions GROUP BY Month, StockCode ORDER BY Month, StockCode;"""
    df = pd.read_sql_query(query, connection)
    return df

# The sales trends for each product
def Sales_trends_each_product(connection):
    query = """SELECT STRFTIME('%Y-%m', InvoiceDate) AS Month, StockCode, SUM(TotalAmount_GBP) AS Total FROM Transactions GROUP BY Month, StockCode ORDER BY Month, Total DESC;"""
    df = pd.read_sql_query(query, connection)
    return df

# Top 5 customers by total sales
def Top_five_customers(connection):
    query = """SELECT t.CustomerID, SUM(t.TotalAmount_GBP) AS Total FROM Transactions t JOIN Customers c ON t.CustomerID = c.CustomerID GROUP BY t.CustomerID ORDER BY Total DESC LIMIT 5; """
    df = pd.read_sql_query(query, connection)
    return df

# The revenue contribution by each product
def Revenue_contribution(connection):
    query = """SELECT p.StockCode, SUM(t.TotalAmount_GBP) AS Revenue FROM Transactions t JOIN Products p ON t.StockCode = p.StockCode GROUP BY p.StockCode ORDER BY Revenue DESC;"""
    df = pd.read_sql_query(query, connection)
    return df