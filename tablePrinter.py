tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

#def printTable(tableData):

colWidths = colWidths = [0] * len(tableData)


# for i in tableData:
#     p = len(i)
#     t = len(i[p])
#     print(t)

# print(colWidths)
# for i in tableData:
#     for x in i:
#         print(x.rjust(10))

for a in zip(*tableData):
    print(*a)

