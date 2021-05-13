#!/usr/bin/env python3

import sqlite3
conn = sqlite3.connect('sql_challenge.db')
print("Opened database successfully")
conn.execute('''CREATE TABLE switches
 (hostname CHAR,
 ip CHAR,
 startup_config CHAR,
 running_config CHAR,
 valid_config BOOL);''')
print("Table created successfully")
conn.close()
