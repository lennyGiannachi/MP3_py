import happybase as hb

conn = hb.Connection()

p = {
        'personal': dict(),
        'professional': dict(),
        'custom' : dict()
    }

f = {
        'nutrition' : dict(),
        'taste' : dict()
    }

conn.create_table('powers', p)
conn.create_table('food', f)
conn.close()
