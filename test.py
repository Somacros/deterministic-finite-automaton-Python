#Llenado de Delta
delta = {}
delta_data = open("D:/DevSpace/Python/AFD_Experimental/delta.txt","rt")

c = 0
for row in delta_data:

    SeparatedElements = []
    #Se define vector que contiene los estados de transición
    transitions = row.strip().split(";")

    for element in transitions:
        SeparatedElements.append(element.split(","))

    print(SeparatedElements)

    deltaDictionary = {}
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
    
    
    print(delta)

delta_data.close()