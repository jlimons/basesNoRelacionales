import random
import re

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

######### 5. #########
def getObservationsCount(observedValuesList):
  valuesDictionary = {
    'One': 0,
    'Two': 0,
    'Three': 0,
    'Four': 0,
    'Five': 0,
    'Six': 0
  }

  i = 0
  for item in valuesDictionary:
    valueCount = observedValuesList.count(i+1)
    valuesDictionary[item] = valueCount
    i += 1

  return valuesDictionary

def rollDice(timesToRoll):
  observedValues = []

  for i in range(timesToRoll):
    diceOneValue = random.randrange(1, 7)
    diceTwoValue = random.randrange(1, 7)
    observedValues.append(diceOneValue)
    observedValues.append(diceTwoValue)

  countDictionary = getObservationsCount(observedValues)
  print(countDictionary)

# rollDice(8)

str1 = "azcbobobegghakl"
str2 = "bob"

######### 7. #########
def stringContained(baseString, substring):
  count = 0
  containsAt = baseString.find(substring)
  
  if containsAt > -1:
    count += 1
    iterateCount = len(baseString) - containsAt
    searchBegin = containsAt + 1
    searchEnd = searchBegin + len(substring)

    for i in range(iterateCount):
      containsAt = baseString.find(substring, searchBegin, searchEnd)
      searchBegin += 1
      searchEnd += 1
      if containsAt > -1:
        count += 1

  print('Cantidad de veces que',substring,'ocurre es:', count)

# stringContained(str1, str2)
