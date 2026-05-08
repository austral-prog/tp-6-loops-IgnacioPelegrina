# Replace the "ANSWER HERE" for your answer

def index_of(target, lst):
    """
    Retorna el indice de la primera ocurrencia de target en lst.
    Si no se encuentra, retorna -1.

    Ejemplo: index_of("Black", ["Red", "Green", "Black"]) -> 2
    """
    indice = -1
    i = 0
    while i < len(lst) and indice == -1:
        if lst[i] == target:
            indice = i
        i += 1
    return indice

def index_of_by_index(target, lst, start):
    """
    Retorna el indice de la primera ocurrencia de target en lst,
    buscando a partir del indice start (inclusive).
    Si no se encuentra, retorna -1.

    Ejemplo: index_of_by_index("Black", ["Red", "Black", "Green", "Black"], 2) -> 3
    """
    indice = -1
    i = start
    while i < len(lst) and indice == -1:
        if lst[i] == target:
            indice = i
        i += 1
    return indice

def index_of_empty(lst):
    """
    Retorna el indice del primer string vacio ("") en lst.
    Si no hay ninguno, retorna -1.

    Ejemplo: index_of_empty(["Red", "", "Green"]) -> 1
    """
    indice = -1
    i = 0
    while i < len(lst):
        if lst[i] == "":
            indice = i
        i += 1
    return indice
