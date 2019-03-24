import happybase as hb

# DON'T CHANGE THE PRINT FORMAT, WHICH IS THE OUTPUT
# OR YOU WON'T RECEIVE POINTS FROM THE GRADER

conn = hb.Connection()
table = conn.table('powers')
column = (b'personal:hero', b'personal:power', b'professional:name', b'professional:xp', b'custom:color')

for key, data in table.scan(columns=column, include_timestamp=True)
    print('Found: {}, {}'.format(key, data))

conn.close()
