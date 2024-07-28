def bestFit(arr, memBlock):
    space = len(memBlock)
    arrLen = len(arr)
    dic = {}

    for val in arr:
        
        temp = []
        if space == 0 or arrLen == 0:
            break

        for lo, blockVal in enumerate(memBlock):
            if blockVal >= val and lo not in dic and space > 0:
                temp.append((blockVal, lo))

        if temp:
            minTuple = min(temp, key=lambda x: x[0])
            space -= 1
            arrLen -= 1
            dic[minTuple[1]] = 1
        
    if space <= 0 or arrLen <= 0:
        return 0
    else:
        return 1