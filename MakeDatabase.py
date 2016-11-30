import sqlite3

conn  = sqlite3.connect("ScamBase.db")

c = conn.cursor()

c.execute("""CREATE TABLE ScamBase
          (id INTEGER PRIMARY KEY,
          company_name  TEXT ,
          number  TEXT ,
          etc  TEXT ,
          date DATE)""")

conn.commit()

print("table has been created")
