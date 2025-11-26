# Contrato: init(vals), step() -> {"a": int, "b": int, "swap": bool, "done": bool}

items = []
n = 0
i = 0      # elemento que queremos insertar
j = None   # cursor de desplazamiento hacia la izquierda (None = empezar)

def init(vals):
    global items, n, i, j
    items = list(vals)
    n = len(items)
    i = 1      # común: arrancar en el segundo elemento
    j = None


def step():
    # TODO:
    global n , i , j , items
    # Si i >= n: devolver {"done": True}.
    if i>=n:
        return {"done": True}
    
    # Si j es None: empezar desplazamiento para el items[i] (p.ej., j = i) y devolver un highlight sin swap.
    if j == None:
        j=i
        a=i-1
        b=i
        swap = False
        return {"a": a, "b": b, "swap": False, "done": False}

    
    # Mientras j > 0 y items[j-1] > items[j]: hacer UN swap adyacente (j-1, j) y devolverlo con swap=True.
    if j>0 and items[j-1]>items[j]:
        a = j - 1
        b = j
        aux=items[j-1]
        items[j-1]=items[j]
        items[j]=aux
        swap = True
        j -= 1
        return {"a": a, "b": b, "swap": True, "done": False}
    
    # Si ya no hay que desplazar: avanzar i y setear j=None.
    i = i+1 
    j=None
    swap = False
    return {"a": 0 , "b": 0 , "swap": swap  , "done": False}