import random

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

#----------ejercicio 2---------------


def tuplaPares(tuplaT): #función que  recibe una tupla
    temp=[] #se crea una lista vacia para agregar los elementos pares
    a=() # tupla final
    for indice, item in enumerate(tuplaT,1): #función que enumera lista
        if(indice%2): 
            #se resta 1 al indice ga que iniciamos del primer elemento
            temp.insert(indice,tuplaT[indice-1]) 
            a=tuple(temp) # se convierte la lista a una tupla
    return a #regresa tupla de los elementos pares

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
#---------ejercicio 4------------------


def cuentaPalabras(cadena): #función que recibe una cadena
    extra=[] # se crea una lista auxiliar donde se ponen los datos finales
    listaPalabras=cadena.split() #se crea una lista con los elementos de cade
    x=0
    frecuencia=[] # lista auxiliar para contar las frecuencias de cada palabra
    for cuent in listaPalabras:
        frecuencia.append(listaPalabras.count(cuent)) #lista de frecuencias d
        #de cada palabra
        extra.insert(x,(listaPalabras[x],frecuencia[x]))# se agregan a la list
        #final los elementos de frecuencia y palabras
        x=x+1
    return dict(set(extra))#se convierte en diccionario los elementos de la li
#utilizando la función set para quitar elementos repetidos

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

#------------ejercicio 6---------------


def multMatrices(a,b): #se reciben 2 listas con listas de cada vector(xyz)
    r1=[]  # se crean listas auxiliares para almacenar los resultados
    r2=[]
    
    while len(a)>0: #se recorre el # de veces del tamaño de a
        recorrido=0 #variable para recorrer cada vector dentro de la matriz
        a1=a[:1:] #se obtiene el primer vector
        
        
        while recorrido<len(a1): #se recorre cada vector
            for x in b: #recorrer cada vector dentro del # de columnas de b
                for x1 in x: #recorre el numero de elementos anterior
                    r1.append(x1*a1[0][recorrido])#se agrega al resultado la m
                    #multiplicacion del elmento de laprimer fila de a por la 
                    #columna de b
                recorrido=recorrido+1# se recorre cada elemento
        a.pop(0)# se elimina elemento de la lista
        
    r1=[r1[i:i+len(b[0])] for i in range(0,len(r1),len(b[0]))]
    # range crea una lista desde 0 hasta el tamaño de la lista r1, avanzando 
    #depende el tamño de be esa lista se recorre por i , y el valor actual 
    # de i que avanza en la lista de resulados sumando con el el valor de la
    #multiplicación almacenado en r1
    
    suma=0
    
    while len(r1)>0:#recorremos mientras r1>0 
        for x in range(len(r1[0])):# se recorre una lista ordenada del numero
       # de valores que tenemos en la lista de resultados r1
            for y in range(len(b)):# se recorre cada vector dentr # col de b
                suma=suma+r1[y][x] # se toman los valores de las multiplicaciones
                #almacenados en r1 para sumar cada elemento por cada x y z
            r2.append(suma)# se agregan los valor a lista de resultados r2
            suma=0
        for s in range(len(b)):
            r1.pop(0)
    
    r2=[r2[i:i+len(b[0])] for i in range(0, len(r2),len(b[0]))]
     # range crea una lista desde 0 hasta el tamaño de la lista r2, avanzando 
    #depende el tamño de b esa lista se recorre por i , y el valor actual 
    # de i que avanza en la lista de resulados  r2 sumando con el el valor de la
    #multiplicación almacenado en r2 que se agregaron a traves de la variable 
    #suma en cada iteracion 
    
    
    return (r2)
    
        
    
