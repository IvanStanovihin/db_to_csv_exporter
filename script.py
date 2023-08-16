import sys, psycopg2, csv
# conn = psycopg2.connect("dbname=rshb_files_exporter_db user=postgres password=admin")

conn = psycopg2.connect(
    host="localhost",
    database="rshb_files_exporter_db",
    user="postgres",
    password="admin"
)

cur = conn.cursor()
cur.execute("SELECT * FROM statistic")

rows = cur.fetchall()

with open('C:/RSHB/exported_files/results.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["column1", "column2", "column3"])
    writer.writerows(rows)

cur.close()
conn.close()

