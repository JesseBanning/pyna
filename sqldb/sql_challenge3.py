import os.path
import sys
from napalm import get_network_driver # import code from NAPALM
if len(sys.argv) != 2:
  print("You supplied ", len(sys.argv)-1, " arguments but 1 is needed")
  print("getrun.py requires: IP")
  print("example: python3 getrun.py  a.b.c.d")
  sys.exit()
ip = sys.argv[1]
from napalm import get_network_driver # import code from NAPALM
driver = get_network_driver('eos') # get the driver for Arista devices
device = driver(ip, 'admin', 'alta3') # apply the switch credentials
device.open() # start the connection
config = device.get_config()
# This next line EXTRACTS the running config from the glob
running_config = config['running']
startup_config = config['startup']

import sqlite3

conn = sqlite3.connect('sql_challenge.db')
print("Opened database successfully")
conn.execute(f"UPDATE switches SET running_config = '{running_config}' WHERE hostname = 'sw-2'")
conn.execute(f"UPDATE switches SET startup_config = '{startup_config}' WHERE hostname = 'sw-2'")
conn.commit()

print("Total number of rows updated :", conn.total_changes)

print("Operation done successfully")
conn.close()
