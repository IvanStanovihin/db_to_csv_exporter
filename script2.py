import sys, psycopg2, time

DATABASE_NAME = 'rshb_files_exporter_db'
DATABASE_USER = 'postgres'
DATABASE_PASSWORD = 'admin'

CSV_FILE_PATH = 'C:/RSHB/exported_files/result2.csv'

conn = psycopg2.connect("dbname={} user={} password={}".format(DATABASE_NAME, DATABASE_USER, DATABASE_PASSWORD))
cur = conn.cursor()

sql = "COPY (SELECT * FROM statistic) TO stdout DELIMITER ';' CSV HEADER"
while(True):
    with open(CSV_FILE_PATH, "w") as file:
        cur.copy_expert(sql, file)
        print('Data from database {} copied to file {} successful'.format(DATABASE_NAME, CSV_FILE_PATH))
    #copy frequency in seconds
    time.sleep(30)
cur.close()
conn.close()

