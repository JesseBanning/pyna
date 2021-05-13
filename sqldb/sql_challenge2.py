#!/usr/bin/env python3

import sqlite3
conn = sqlite3.connect('sql_challenge.db')
print("Opened database successfully")

conn.execute("INSERT INTO switches (hostname, ip) VALUES ('sw-1', '10.3.204.43')")

conn.execute("INSERT INTO switches (hostname, ip) VALUES ('sw-2', '10.10.84.160')")

conn.commit()
print("Records created successfully")
conn.close()
