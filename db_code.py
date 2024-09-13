# Database initiation
import sqlite3
import pandas as pd

# Connect to SQLite database (creates if it doesn't exist)
conn = sqlite3.connect('STAFF.db')

# Create and Load the table
table_name = 'INSTRUCTOR'
attribute_list = ['ID', 'FNAME', 'LNAME', 'CITY', 'CCODE']  # Added LNAME to match the append operation

# Reading the CSV file
file_path = '/home/project/INSTRUCTOR.csv'  # Adjust this path as necessary
df = pd.read_csv(file_path, names=attribute_list)

# Loading the data into a table
df.to_sql(table_name, conn, if_exists='replace', index=False)
print('Table is ready')

# Running basic queries on data
query_statement = f"SELECT * FROM {table_name}"
query_output = pd.read_sql(query_statement, conn)
print(query_statement)
print(query_output)

query_statement = f"SELECT FNAME FROM {table_name}"
query_output = pd.read_sql(query_statement, conn)
print(query_statement)
print(query_output)

query_statement = f"SELECT COUNT(*) FROM {table_name}"
query_output = pd.read_sql(query_statement, conn)
print(query_statement)
print(query_output)

# Appending new data
data_dict = {
    'ID': [100],
    'FNAME': ['John'],
    'LNAME': ['Doe'],  # Ensure LNAME is included
    'CITY': ['Paris'],
    'CCODE': ['FR']
}
data_append = pd.DataFrame(data_dict)

data_append.to_sql(table_name, conn, if_exists='append', index=False)
print('Data appended successfully')

# Close the connection
conn.close()
