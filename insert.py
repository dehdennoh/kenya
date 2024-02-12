import sqlite3

conn = sqlite3.connect('afternoon.db')
print("Opened database suceesfully")

conn.execute("INSERT INTO EMPLOYEES VALUES (1,'FAITH KARIMI',34, 340000.00)")
conn.execute("INSERT INTO EMPLOYEES VALUES (2,'DENNIS DENNOH',25, 250000.00)")
conn.execute("INSERT INTO EMPLOYEES VALUES (3,'IAN WIGHT',33, 110000.00)")
conn.execute("INSERT INTO EMPLOYEES VALUES (4,'SOPHY MIMO',30, 120000.00)")
conn.execute("INSERT INTO EMPLOYEES VALUES (5,'JANE CHELEGAT',40, 450000.00)")

conn.commit()
print("Employees inserted successfully")
conn.close()