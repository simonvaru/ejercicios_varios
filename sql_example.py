import sqlite3
import pandas as pd

connection = sqlite3.connect("gta.db")
cursor = connection.cursor()


release_list = [
    (1997, "Grand Theft Auto", "state of New Guernsey"),
    (1999, "Grand Theft Auto 2", "Anywhere, USA"),
    (2001, "Grand Theft Auto III", "Liberty City"),
    (2002, "Grand Theft Auto: Vice City", "Vice City"),
    (2004, "Grand Theft Auto: San Andreas", "state of San Andreas"),
    (2008, "Grand Theft Auto IV", "Liberty City"),
    (2013, "Grand Theft Auto V", "Los Santos")
]

city_list = [
    ("Liberty City", "New York"),
    ("state of New Guernsey", "state of New Jersey"),
    ("Anywhere, USA", "all USA cities"),
    ("Vice City", "Miami"),
    ("state of San Andreas", "state of California"),
    ("Los Santos", "Los Angeles")
]

cursor.execute("create table gta (release_year integer, release_name text, city text)")
cursor.executemany("Insert into GTA values(?, ?, ?)", release_list)

for row in cursor.execute("Select * from GTA"):
    print(row)

print("***************************")
cursor.execute("Select * from GTA where city=:c", {"c": "Liberty City"})
# cursor.execute("select * from gta where city=:c", {"c": "Liberty City"})
gta_search = cursor.fetchall()
print(gta_search)


city_list = [
    ("Liberty City", "New York"),
    ("State of New Guernsey", "State of New Jersey"),
    ("Anywhere, USA", "all USA cities"),
    ("Vice City", "Miami"),
    ("state of San Andreas", "state of California"),
    ("Los Santos", "Los Angeles")
]

cursor.execute("create table cities (gta_city text, real_city text)")
cursor.execute("insert into cities values(?, ?)", ("Liberty City", "New York"))
cursor.execute("select * from cities where gta_city=:c", {"c": "Liberty City"})
cities_search = cursor.fetchall()
print(cities_search)

print("***************************")
for i in gta_search:
    adjust = [cities_search[0][1] if value==cities_search[0][0] else value for value in i]
    print(adjust)



connection.close()