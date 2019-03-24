import happybase as hb
import csv

conn = hb.Connection()
table = conn.table('powers')
row_num = 1
file_in = open('input.csv')
for record in file_in:
        row = record.split(',')
        data = {
                b'personal:hero' : str.encode(row[1]),
                b'personal:power' : str.encode(row[2]),
                b'professional:name' : str.encode(row[3]),
                b'professional:xp' : str.encode(row[4]),
                b'custom:color' : str.encode(row[5].strip('/r/n'))
               }
        table.put(str.encode(row[0]), data)

conn.close()
