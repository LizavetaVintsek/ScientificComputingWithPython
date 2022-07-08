#Find Unicode code points (int) for all characters of your name.
l = ord("l")
i = ord("i")
z = ord("z")
a = ord("a")
print (l, i, z, a)

#Prepare the periodic table as a list
#var1
from tabulate import tabulate
table = [['No.', 'Name (en)', 'Symbol', 'Weight (u)'], [1,"Hydrogen", "H", 1], [2, "Helium", "He", 4], [3, "Lithium", "Li", "7"]]
print(tabulate(table, headers='firstrow', tablefmt='grid'))
#var2
line1 = '+---+--------------------+------+----------+'
line2 = '|No.|Name (en)           |Symbol|Weight (u)|'
pt = [(1,"Hydrogen","H",1), (2,"Helium","He",4), (3, "Lithium", "Li", 7)]
L = [line1, line2, line1]
for t in pt: L.append('|{}|{}|{}|{}|'.format
                     (str(t[0]).rjust(3),
                      t[1].ljust(20),
                      t[2].center(6),
                      str(t[3]).rjust(10)))
L.append(line1)
print('\n'.join(L))
#var3
line1 = '+---+--------------------+------+----------+'
line2 = '|{0:>3}|{1:<20}|{2:^6}|{3:>10}|'.format('No.', 'Name (en)', 'Symbol', 'Weight (u)')
pt = [(1,"Hydrogen","H",1), (2,"Helium","He",4), (3, "Lithium", "Li", 7)]
M = [line1, line2, line1]
for t in pt: M.append ('|{0:>3}|{1:<20}|{2:^6}|{3:>10}|'.format(t[0], t[1], t[2], t[3]))
M.append(line1)
print('\n'.join(M))
#var4
from prettytable import PrettyTable
pt = [(1,"Hydrogen","H",1), (2,"Helium","He",4), (3, "Lithium", "Li", 7)]
head = ['No.', 'Name (en)', 'Symbol', 'Weight (u)']
myTable = PrettyTable(head)
for row in pt:
    myTable.add_row(row)
print(myTable)
#var5
from prettytable import PrettyTable
pt = [(1,"Hydrogen","H",1), (2,"Helium","He",4), (3, "Lithium", "Li", 7)]
head = ['No.', 'Name (en)', 'Symbol', 'Weight (u)']
myTable = PrettyTable(head)
for row in pt:
    myTable.add_row(row)
print(myTable)
