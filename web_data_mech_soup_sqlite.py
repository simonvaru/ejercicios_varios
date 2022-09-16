#scraper.py
#https://en.wikipedia.org/wiki/Comparison_of_Linux_distributions
from multiprocessing import connection
import mechanicalsoup
import pandas as pd
import sqlite3

browser = mechanicalsoup.StatefulBrowser()
browser.open("https://en.wikipedia.org/wiki/Comparison_of_Linux_distributions")


#extract table headers
th = browser.page.find_all("th", attrs= {"class": "table-rh"})
distribution = [value.text.replace("\n", "") for value in th]
distribution = distribution[:98]
# print(distribution)
print("===================================Order list===========================================")
#extract table data
td = browser.page.find_all("td")
columns = [value.text.replace("\n", "") for value in td]
columns = columns[6:1084]
# print(columns.index("AlmaLinux Foundation"))
# print(columns.index("Binary blobs"))
# print("     ...      ", td[1083])

print("==================================Enumerate Functions==================================")
column_names =["Founder",
               "Maintainer",
               "Initial release year",
               "Current stable version",
               "Security updates (years)",
               "Release date",
               "System distribution commitment",
               "Forked from",
               "Target audience",
               "Cost",
               "Status"]

dictionary = {"Distribution": distribution}
# insert column names and their data into a dictionary
for idx, key in enumerate(column_names):
    # idx = 0 key = Founder
    # idx = 1 key = Maintainer
    # idx = 2 key = Initial release year
    # idx = 3 key = Current stable version
    # idx = 4 key = Security updates (years)
    # idx = 5 key = Release date
    # idx = 6 key = System distribution commitment
    # idx = 7 key = Forked from
    # idx = 8 key = Target audience
    # idx = 9 key = Cost
    # idx = 10 key = Status
    dictionary[key] = columns[idx:][::11]
    # dictionary{Founder : [AlmaLinux Foundation, Alpine Linux Team, ALT Linux Team, ..., Zorin Group]}
    # dictionary{Maintainer : [AlmaLinux Foundation, Alpine Linux Team, ALT Linux Team ALT Linux LLC, ..., Zorin Group]}
    # dictionary{Initial release year : [2021, 2006, 2001, ..., 200]}
    # dictionary{Current stable version : [9.0, 3.16, 10.0, ..., OS 16.1]}
    # ...
    # dictionary{Status : [Active, Active, Active, ..., Active]}

df = pd.DataFrame(data = dictionary)
# print("Dataframe creada: \n", df.tail)

print("==================================Organize==================================")
connection = sqlite3.connect("linux_distro.db")
cursor =connection.cursor()

cursor.execute("create table linux (Distribution, ", ",".join(column_names), ")")
for i in range(len(df)):
    cursor.execute("insert into linux values (?,?,?,?,?,?,?,?,?,?,?,?)", df.iloc[i])

connection.commit()

connection.close()







