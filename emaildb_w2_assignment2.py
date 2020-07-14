# Using PYthon to Access Database
# w_2 assignment 2
import sqlite3
import re

conn = sqlite3.connect('emaildb.sqlite')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Counts')

cur.execute('''
CREATE TABLE Counts (org TEXT, count INTEGER)''')

fname = input('Enter file name: ')
#if (len(fname) < 1): fname = 'mbox2.txt', this is the shorter version to test the code
if (len(fname) < 1): fname = 'mbox.txt'
fh = open(fname)
for line in fh:
    if not line.startswith('From: '): continue
    pieces = line.split()
    #email = pieces[1]
    #use this simple split method or use the following regular expression
    org = pieces[1].split('@')[1]
   

    # next line use regular expression to extract any non-blank character after "@" sign
    #org = re.findall('@([^ ]+)',pieces[1])

    #print (pieces[1],org)
    # I received an error: "Error binding parameter 0: probably unsupported type" in the next line,
    # (org,). With stackoverflow help, I convert it into string, and worked
    cur.execute('SELECT count FROM Counts WHERE org = ? ', (str(org),))
    row = cur.fetchone()
    if row is None:
        cur.execute('''INSERT INTO Counts (org, count)
                VALUES (?, 1)''', (str(org),))
    else:
        cur.execute('UPDATE Counts SET count = count + 1 WHERE org = ?',
                    (str(org),))
    conn.commit()

# https://www.sqlite.org/lang_select.html
sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10'

for row in cur.execute(sqlstr):
    print(str(row[0]), row[1])
    #print (row)

cur.close()
