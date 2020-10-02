tableData = [['apples', 'oranges', 'cherries', 'banana'],
['Alice', 'Bob', 'Carol', 'David'],
['dogs','cats','moose','goose']]

def printTable():
    colWidths = [0] * len(tableData)
    for i in range(len(tableData)):
        for j in tableData[i]:
            if colWidths[i] < len(j):
                colWidths[i] = len(j)

    for x in range(len(tableData[0])):
        for y in range(len(tableData)):
            print(tableData[y][x].rjust(colWidths[y]), end=' ')
        print()


printTable()