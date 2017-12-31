import sqlite3
conn = sqlite3.connect("factbook.db")
query = "select SUM(area_land), SUM(area_water) from facts where (area_land !=' ') AND (area_water !=' ' ) ;"
query1 = "select SUM(area_land) from facts where area_land != ' ' ;"

query2 = "select SUM(area_water) from facts where area_water != ' ' ;"

results1 = conn.execute(query1).fetchall()
results2 = conn.execute(query2).fetchall()
#print((results[0][0] / results[0][1]))
print(results1[0][0] / results2[0][0])
conn.close()