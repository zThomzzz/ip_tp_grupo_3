# Contrato: init(vals), step() -> {"a": int, "b": int, "swap": bool, "done": bool}

items = []
n = 0
i = 0
j = 0

def init(vals):
    global items, n, i, j
    items = list(vals)
    n = len(items)
    i = 0
    j = 0

def step():
    global items, n, i, j
    a=j
    b=j+1
    swap=False
    if i==n-1:
        return {"done": True}
    if items[a]>items[b]:
        aux=items[a]
        items[a]=items[b]
        items[b]=aux
        swap=True 
    if j+1==n-i-1:
        i=i+1
        j=0
    else:
         j=j+1
    return {"a": a, "b": b, "swap": swap, "done": False}
 # TODO:
    # 1) Elegir índices a y b a comparar en este micro-paso (según tu Bubble).
    # 2) Si corresponde, hacer el intercambio real en items[a], items[b] y marcar swap=True.
    # 3) Avanzar punteros (preparar el próximo paso).
    # 4) Devolver {"a": a, "b": b, "swap": swap, "done": False}.
    #
    # Cuando no queden pasos, devolvé {"done": True}.