#!/usr/bin/env python3

import sqlite3

conn = sqlite3.connect('test.db')
print("Opened database successfully")

cursor = conn.execute("SELECT salary from COMPANY")
for row in cursor:
    print("SALARY = ", row[3], "\n")

print("Operation done successfully")
conn.close()

