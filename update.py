import sqlite3

conn = sqlite3.connect('afternoon.db')
print("Opened database suceesfully")

conn.execute("UPDATE EMPLOYEES SET SALARY =500000.00 WHERE ID=5")
conn.commit()

let = conn.execute("SELECT * FROM EMPLOYEES")
for row in let:
    print("ID :", row[0])
    print("NAME:", row[1])
    print("AGE :", row[2])
    print("SALARY :", row[3])

print("Updated successfully")
conn.close()