######### 1. #########

# a)
testList = [1,2,3,4,5,6,7,8,9]
n = len(testList)

def shiftList(shiftCount, listLength, listToShift):
  if shiftCount >= 0:
    newList = listToShift[shiftCount:]
    for i in range(shiftCount):
      newList.insert(i, 0)
  else:
    newList = listToShift[:shiftCount]
    for x in range(shiftCount * -1):
      newList.append(0)

  print(newList)

# Uncomment the following to test
# shiftList(-3,n,testList)

# b)
matrixA = [[1,2], [3,4], [5,6]]
matrixB = [[7,8], [9,10], [11,12]]

def sumMatrices(ma, mb):
  rows = len(ma)
  cols = len(ma[0])
  res = []

  for i in range(rows):
    res.append([])
    for j in range(cols):
      res[i].append(ma[i][j] + mb[i][j])

  print(res)

sumMatrices(matrixA, matrixB)