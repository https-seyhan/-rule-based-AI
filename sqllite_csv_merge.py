import sqlite3
import pandas as pd

# Create a connection to a new SQLite database
conn = sqlite3.connect('large_data.db')

# Load the first dataset into the database
df1 = pd.read_csv('large_file1.csv')
df1.to_sql('table1', conn, if_exists='replace', index=False)

# Load the second dataset into the database
df2 = pd.read_csv('large_file2.csv')
df2.to_sql('table2', conn, if_exists='replace', index=False)

# Perform the merge using SQL
query = '''
SELECT *
FROM table1
JOIN table2 ON table1.key = table2.key
'''
merged_df = pd.read_sql_query(query, conn)

# Close the connection
conn.close()
