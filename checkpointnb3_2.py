    def takeSecond(elem):
        return elem[1]

    random = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]


    random.sort(key=takeSecond)


    print('Sorted list:', random)

