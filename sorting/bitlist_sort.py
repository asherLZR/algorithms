def bitlist_sort(data):
    returnArray = []
    largestNumber = data[0]
    for i in range(1, len(data)):
        if data[i] > largestNumber:
            largestNumber = data[i]
    bList = [0]*largestNumber
    for j in range(0, len(data)):
        index = data[j] - 1
        bList[index] += 1
    for k in range(0, len(bList)):
        if bList[k] != 0:
            returnArray.append(k + 1)
    return returnArray
