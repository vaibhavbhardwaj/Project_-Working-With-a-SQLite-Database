import sqlite3
conn = sqlite3.connect("factbook.db")
query = "select * from facts order by population asc limit 10;"
results = conn.execute(query).fetchall()
print(results)
conn.close()