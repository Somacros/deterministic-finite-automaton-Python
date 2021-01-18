#Inicia llenado de Q, q0 y F (Conjunto de estados, estado inicial y estados de aceptación)
Q_data = open("D:/DevSpace/Python/AFD_Pila/configuracionEstados.txt","rt")

Q = Q_data.readline().strip().split(",")

q0 = Q_data.readline().strip()

F = Q_data.readline().strip().split(",")

Q_data.close()

#Llenado de sigma
sigma_data = open("D:/DevSpace/Python/AFD_Pila/sigma.txt","rt")

sigma = sigma_data.readline().strip().split(",")

#Llenado del alfabeto de la pila
StackData = open("D:/DevSpace/Python/AFD_Pila/stackConfig","rt")

StackAlphabet = StackData.readline().strip().split(",")

#Llenado de Delta
delta = {}
delta_data = open("D:/DevSpace/Python/AFD_Pila/delta.txt","rt")

c = 0
for row in delta_data:

    SeparatedElements = []
    #Se define vector que contiene los estados de transición
    transitions = row.strip().split(";")

    for element in transitions:
        SeparatedElements.append(element.split(","))

    actionsDictionary = {}
    actionsDictionary[SeparatedElements[0][1]] = {
        "pop": SeparatedElements[0][2],
        "insert": SeparatedElements[1][1],
        "nextState": SeparatedElements[1][0]
    }

    if SeparatedElements[0][0] in delta:
        delta[SeparatedElements[0][0]].update(actionsDictionary)
    else:
        delta[SeparatedElements[0][0]] = actionsDictionary

delta_data.close()

#EntryString

entryData = open("D:/DevSpace/Python/AFD_Pila/cadenaEntrada.txt")

entryString = entryData.read().strip()

entryData.close()


stack = []


#Main method
def accepts(Q,alphabet,transition,initial,acceptedStates, entryString, StackAlphabet):
    currentState = initial

    for char in entryString:
        if(char in alphabet):
            popItem = transition[currentState][char]['pop']
            insertItem = transition[currentState][char]['insert']
            currentState = transition[currentState][char]['nextState']

            stackAction(popItem, insertItem)
            print(stack)
            
        else:
            return "CADENA DE ENTRADA INCORRECTA"

    if(currentState in acceptedStates and len(stack) == 0):
        return "Cadena Aceptada"
    else:
        return "Cadena rechazada"

def stackAction(popItem,insertItem):
    if(popItem != "E" and len(stack) > 0): #Compara que el item a sacar no sea un Epsilum y que la pila tenga items
        if(stack[len(stack)-1] == popItem): #Compara que item de arriba de la pila sea igual al que se desea sacar
            stack.pop()
    if(insertItem != "E"): #Compara que no se desee insertar un Epsilum
        stack.append(insertItem)

print(accepts(Q,sigma,delta,q0,F,entryString,StackAlphabet))