import pyodbc

# print(pyodbc.drivers())

for i in pyodbc.drivers():
    if 'ODBC Driver 17' in i or 'ODBC Driver 13' in i:
        print(i)