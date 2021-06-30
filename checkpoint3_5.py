def takeSecond(elem):
    return elem[1]

random = [('item1', '12.20'), ('item2', '15.10'), ('item3', '24.5')]


random.sort(key=takeSecond,reverse=True)


print('Sorted list:', random)
