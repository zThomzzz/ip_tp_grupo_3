def init(vals):
    global items, n, i, j, min_idx, fase
    items = list(vals)
    n = len(items)
    i = 0
    j = i + 1
    min_idx = i
    fase = "buscar"

def step():
    global items, n, i, j, min_idx, fase
    if i >= n - 1:
        return {"done": True} #para q no sobrepase el rango de la lista
    #fase "buscar" el indice menor
    if fase=="buscar":
        a = min_idx  #variables locales para el UI q pide el contrato
        b=j
        swap=False 
        
        if items[j] < items[min_idx]: #siempre que haya uno menor lo guarda en min_indx
            min_idx=j
        j+=1
        
        if j>=n: #ya recorrio toda la lista, por lo tanto tenemos el minimo
            fase="swap"
        return {"a": a, "b": b, "swap": False, "done": False} #return que es parte del contrato
    
    #fase "swap" intercambia el minimo por la posicion correspondiente
    if fase == "swap":
        a=i #variable para el visualizador
        b=min_idx # variable para el visualizador
        if min_idx!=i:
            aux=items[min_idx] #guardo el valor del elemento minimo
            items[min_idx] = items[i] #en lo q era la posicion del elemento minimo ponemos lo q estaba al comienzo de la parte desordenada de la lista
            items[i]=aux #guardamos el elemento del minimo en la primera posicion de la parte desordenada
            swap = True
        else:
            swap = False #el valor minimo ya estaba ordenado por lo tanto no se hace ningun cambio
        i+=1
        j=i+1
        min_idx=i #preparamos valores para la siguiente fase de busqueda
        fase="buscar"
        return {"a": a, "b": b, "swap": swap, "done": False}
    return {"done": True}
