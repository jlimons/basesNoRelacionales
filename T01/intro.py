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

# sumMatrices(matrixA, matrixB)

######### 3. #########

listA = ['uno', 2, 'tres', 8]
listB = ['lol', 8 , 'cinco', 15]

def intersection(listA, listB):
  hasValueInCommon = False

  if len(listA) - len(listB) > 0:
    listToIterate = listB
    listToCompareWith = listA
  else:
    listToIterate = listA
    listToCompareWith = listB

  i = 0
  while i < len(listToIterate) and hasValueInCommon == False:
    if listToIterate[i] in listToCompareWith:
      hasValueInCommon = True
    i += 1

  print(hasValueInCommon)

# intersection(listA, listB)
