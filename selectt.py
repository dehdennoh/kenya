import sqlite3


conn = sqlite3.connect('afternoon.db')
print("Opened database suceesfully")

let = conn.execute("SELECT * FROM EMPLOYEES")
for row in let:
    print("ID :", row[0])
    print("NAME:", row[1])
    print("AGE :", row[2])
    print("SALARY :", row[3])

print("Records found")
conn.close()