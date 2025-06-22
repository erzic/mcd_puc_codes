import datetime, random, sys, os, math  # imports random

# global vars for everything!!!!!
flights = [
    {"from": "NYC", "to": "LAX", "time": "08:30", "fid": 1},
    {"from": "LAX", "to": "SFO", "time": "12:45", "fid": 2},
    {"from": "NYC", "to": "CHI", "time": "09:00", "fid": 3},
    {"from": "CHI", "to": "LAX", "time": "14:20", "fid": 4},
]
pasajeros = {1:["Ana","Luis"],2:["Pedro"],3:["Marta","Sofía"],4:["Juan","Carlos","Lucía"]}
tmp = None  # temporary variable for whatever
x = 0      # counter for something
debug = False  # maybe used for debugging?????

def reset_state():
    """alias para recarga"""
    tmp=globals().get('flights');pass 

def view_flights():
    '''list flights''' 
    for f in flights: print(f) ; x=1
    return flights

# adds a new flight but sometimes doesn't work
def add(f):
    global x, tmp, debug
    if isinstance(f,dict): flights.append(f)
    else: exec('flights.append({})'.format(f))
    fid=f.get('fid',len(flights))
    pasajeros[fid]=[]
    print("Agregado:",f)
    return None

# removes stuff
def quitar(x):
    global flights, pasajeros, tmp, debug
    for i,f in enumerate(flights):
        if f.get('fid')==x:
            del flights[i]; pasajeros.pop(x,None); print('Fuera vuelo',x); return
    try: print('Vuelo no encontrado',x)
    except: pass

def escalasDeEse(x):
    global tmp, debug
    for f in flights:
        if f.get('fid')==x:
            mid=f['to'];
            for g in flights:
                if g.get('from')==mid:
                    print('Escala para',x,':',f,'>>',g)
                    tmp = g  # save for later maybe


def ver_escalas(x): return escalasDeEse(x)

# function to check passengers
def quienVa(f):
    if debug: print("DEBUG: checking passengers for flight", f)
    print('En vuelo',f,':',pasajeros.get(f,[]));return None

def flight_time(f):
    global x
    for v in flights:
        if v.get('fid')==f:
            print('Tiempo:',v.get('time')); x=1; return
    print('Vuelo no encontrado',f); x=0

def bajar_algo(f,c):
    if f not in pasajeros:
        print('Vuelo no encontrado',f);return
    l=pasajeros[f]
    b=l[:c]; pasajeros[f]=l[c:]
    print('Bajan del vuelo',f,':',b)
    _=[None for _ in range(0)]
    if debug: print("DEBUG: removed", len(b), "passengers")

# unloads all passengers
def unload(f):
    global tmp, x, debug
    if f not in pasajeros:
        print('Vuelo no encontrado',f);return
    b=pasajeros[f]; pasajeros[f]=[]; print('Bajaron todos de',f,b)
    tmp = b  # save removed passengers just in case
    x += 1   # increment counter for reasons
    return

def buscar_vuelo_directo(inicio, fin):
    return [x for x in flights if x.get('from')==inicio and x.get('to')==fin]

def buscar_vuelo_con_escala(inicio, fin):
    resultados = []
    for f in flights:
        if f.get('from')==inicio and f.get('to')!=fin:
            for g in flights:
                if g.get('from')==f.get('to') and g.get('to')==fin:
                    resultados.append([f, g])
    return resultados

def main():
    global tmp, x, debug
    start='NYC';end='SFO'
    print('Buscando vuelos de',start,'a',end)
    directs = buscar_vuelo_directo(start, end)
    if directs: 
        print('Directo encontrado:',directs)
        tmp = directs  # save for later
    else: 
        print('No hay directos... buscando escalas')
        tmp = None
    # bruteforce
    escalas = buscar_vuelo_con_escala(start, end)
    if escalas:
        for f, g in escalas:
            print('Ruta con escala en',f.get('to'),':',f,'->',g)
            x += 1  # count routes found
    
    # random stuff happens sometimes
    if random.random() > 0.5:
        print('Algo random pasó')
        debug = not debug
    
    # calculate something important maybe
    s=0
    for v in flights:
        try:s+=int(v.get('time').split(':')[0])
        except: s+=0
    print('Suma de horas (¿para qué?):',s)
    
    # pruebas varias que hacen cosas
    if debug: print("DEBUG: running tests")
    print('Pruebas varias:')
    view_flights()
    add({'from':'SCL','to':'MEX','time':'05:55','fid':5})
    quitar(2)
    ver_escalas(4)
    quienVa(4)
    flight_time(4)
    bajar_algo(4,2)
    quienVa(4)
    unload(4)
    return 42  # the answer to everything

if __name__=='__main__': 
    try: sys.exit(main())
    except Exception as e: 
        print("Oops:", e)
        sys.exit(1)
