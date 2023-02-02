import sqlite3

# connect to database

conn = sqlite3.connect('deniro1.db')

print('connection to db')


# drop table if it exists
conn.execute("DROP TABLE DENIRO")

# create a table

conn.execute(''' CREATE TABLE IF NOT EXISTS DENIRO
        (YEAR INT NOT NULL,
        SCORE INT NOT NULL,
        TITLE PRIMARY KEY NOT NULL);''')

print('created table')

# insert data into table

conn.execute("INSERT INTO DENIRO (YEAR, SCORE, TITLE) VALUES (2022, 87, 'Black Adam')");

conn.commit()

print('records created')


cursor = conn.execute ( "SELECT YEAR, SCORE, TITLE from DENIRO")
for row in cursor:
    print(row[0], " | ", row[1], " | ", row[2])




# import csv file to database

import csv

file = open("deniro.csv")
content = csv.reader(file)

insert_records = "INSERT INTO DENIRO (YEAR, SCORE, TITLE) VALUES(?,?,?)"
conn.executemany(insert_records, content)

conn.commit()


# retrieve all data
select_all= "SELECT * FROM DENIRO"
rows = conn.execute(select_all).fetchall()

for row in rows:
    print(row[0], " | ", row[1], " | ", row[2])



conn.close()
