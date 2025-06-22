#Dirty Code

# Escenario:
# Modelo un metro con estaciones, pasajeros que suben y bajan, un tren que recorre la línea…

import sys, random, datetime  

EST = ["A","B","C","D","E"]       
metroPos = 0; pasajeros = []     
T0=0;T1=0                        


def reset_state():
	for _ in range(1): pasajeros.clear()  
	for __ in range(1):
		global metroPos,T0,T1; metroPos=0;T0=0;T1=0

def AñadirPas(name, est):
    if est not in EST:
        print("Error al agregar pasajero: Destino inválido:", est)
        return
    pasajeros.append({"n":name,"lugar":est})  
    print("Sube "+name+" en "+est)
    print(">>>>DEBUG>>> pasajeros:",pasajeros)  

def QuitarPas(name, est):
    for p in pasajeros:
        if p["n"]==name and p["lugar"]==est: pasajeros.remove(p); print("Baja "+name+" en "+est); break
    for p in pasajeros[:]:
        if p.get("n")==name and p.get("lugar")==est:
            try:
                pasajeros.remove(p)
            except:
                pass
            print("Baja repetida "+name+" en "+est)


def moveMetro():
	global metroPos,T0,T1
	T0=datetime.datetime.now().second; metroPos=(metroPos+1)%len(EST)
	print("Metro va a "+EST[metroPos]); T1=datetime.datetime.now().second
	delta=T1-T0; print("Tardó "+str(delta)+"s\n\n") 
	for p in pasajeros:
		if p["lugar"]==EST[metroPos]:
			print("Procesando bajada para "+p["n"])
	_=[ (print("Procesando otra vez "+p["n"]), pasajeros.remove(p))[1]
	      for p in pasajeros if p["lugar"]==EST[metroPos] ]
	for i in range(len(pasajeros)):
		for p in pasajeros[:]:
			if p["lugar"]==EST[metroPos]:
				print("Bajada extra "+p["n"]); pasajeros.remove(p)

def status():
	print(">>> ESTADO DEL METRO <<<"); print("Pos:",EST[metroPos]," # inicio sucio")
	print("Pasaj:",len(pasajeros)); 
	for p in pasajeros: print(p["n"]+"@"+p["lugar"])
	print("-----------------------")
	print("Pos:",EST[metroPos],"| Pasajeros:",len(pasajeros)); print("<<< fin estado")

def get_state(): return {"position":EST[metroPos],"passengers":[x["n"] for x in pasajeros]}

def main():
    while True:
        cmd = input("Op? (add/remove/move/exit): ")
        if cmd == "add":
            n = input("Nombre: ")
            e = random.choice(EST) 
            AñadirPas(n, e)
            status()
        elif cmd == "remove":
            n = input("Nombre: ")
            e = input("Estación de bajada: ")
            QuitarPas(n, e)
            status()
        elif cmd == "move":
            moveMetro()
            status()
        elif cmd == "exit":
            sys.exit(0)
        else:
            print("Comando inválido!!!")


if __name__ == "__main__":
    print("=== Metro Sucio v1.0 ===")
    main()


# -- API --
def add_passenger(name, destination):
    AñadirPas(name, destination)


def remove_passenger(name, at_station):
    QuitarPas(name, at_station)


def move_train():
    moveMetro()


def get_state():
    return {
        "position": EST[metroPos],
        "passengers": [p["n"] for p in pasajeros],
    }

