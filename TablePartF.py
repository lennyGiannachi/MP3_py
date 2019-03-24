import happybase as hb

# DON'T CHANGE THE PRINT FORMAT, WHICH IS THE OUTPUT
# OR YOU WON'T RECEIVE POINTS FROM THE GRADER
# Select p.name, p.power, p1.name, p1.power, p.color
# From powers p
# Inner Join powers p1
# On p.color = p1.color And p.name <> p1.name

conn = hb.Connection() 
table = conn.table('powers') 

rows = 0
for key, data in table.scan():
  rows = rows + 1
    

row_num = 1
while row_num < rows:
  row = 'row'+str(row_num)
  row = table.row(str.encode(row))
  color = row[b'custom:color']
  name = row[b'professional:name']
  power = row[b'personal:power']
  
  row_num1 = 1
  while row_num1 < rows:
    row = 'row'+str(row_num1)
    row = table.row(str.encode(row))
    color1 = row[b'custom:color']
    name1 = row[b'professional:name']
    power1 = row[b'personal:power']
    
    if color == color1 and name != name1:
      print('{}, {}, {}, {}, {}'.format(name, power, name1, power1, color))
    row_num1 += 1
  row_num += 1
  
conn.close()
      


