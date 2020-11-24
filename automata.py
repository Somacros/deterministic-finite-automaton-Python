#Inicia llenado de Q, q0 y F (Conjunto de estados, estado inicial y estados de aceptación)
Q_data = open("D:/DevSpace/Python/AFD_Experimental/configuracion.txt","rt")

Q = Q_data.readline().strip().split(",")

q0 = Q_data.readline().strip()

F = Q_data.readline().strip().split(",")

Q_data.close()

#Llenado de sigma
sigma_data = open("D:/DevSpace/Python/AFD_Experimental/sigma.txt","rt")

sigma = sigma_data.readline().strip().split(",")

#Llenado de Delta
delta = {}
delta_data = open("D:/DevSpace/Python/AFD_Experimental/delta.txt","rt")

c = 0
for row in delta_data:

    #Se define vector que contiene los estados de transición
    transitions = row.strip().split(",")

    #Se inicializa un diccionario que será el que contenga los datos de transición.
    rowdelta = {}
    j = 0
    for char in sigma:
        #El diccionario se llena con 'char' siendo el caracter de sigma y su valor con el orden
        #correspondiente al vector transactions
        rowdelta[char] = transitions[j]
        j+=1
    
    #Se añade un nuevo elemento al diccionario delta el cual tiene como llave el nombre del estado
    #y como valor un diccionario que contiene sus clave/valor de transición.
    delta[Q[c]] = rowdelta
    c+=1

delta_data.close()

#EntryString

entryData = open("D:/DevSpace/Python/AFD_Experimental/cadenaEntrada.txt")

entryString = entryData.read().strip()

entryData.close()

#Main method
def accepts(Q,alphabet,transition,initial,acceptedStates, entryString):
    currentState = initial

    for char in entryString:
        if(char in alphabet):
            currentState = transition[currentState][char]
        else:
            return "CADENA DE ENTRADA INCORRECTA"

    if(currentState in acceptedStates):
        return "Cadena Aceptada"
    else:
        return "Cadena rechazada"

print(accepts(Q,sigma,delta,q0,F,entryString))