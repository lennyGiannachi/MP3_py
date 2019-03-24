import happybase as hb
import csv

conn = hb.Connection()
table = conn.table('powers')
row_num = 1
file_in = open('input.csv')
for record in file_in:
        values = record.split(',')
        data = {
                b'personal:hero' : values[1],
                b'personal:power' : values[2],
                b'professional:name' : values[3],
                b'professional:xp' : values[4],
                b'custom:color' : values[5]
               }
        table.put(values[0], data)

conn.close()
