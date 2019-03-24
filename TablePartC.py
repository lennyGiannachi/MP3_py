import happybase as hb
import csv

conn = hb.Connection()
table = conn.table('powers')
row_num = 1
file_in = open('input.csv')
csv_reader = csv.reader(file_in, delimiter=',')
for row in file_in:
        data = {
                b'personal:hero' : row[1],
                b'personal:power' : row[2],
                b'professional:name' : row[3],
                b'professional:xp' : row[4],
                b'custom:color' : row[5]
               }
        table.put(row[0], data)

conn.close()
