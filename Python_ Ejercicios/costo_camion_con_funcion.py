#costo_camion con funcion
def costo_camion(nombre_archivo):
    cajones =[]
    precio =[]
    costo = 0
    costo_total = 0
    f = open('camion.csv','rt')
    headers = next(f).split(',')
    headers
    for line in f:
	     row =line.split(',')
	     cajones.append(row[1])
	     precio.append(row[2])
    for c in range (len(cajones)):
        costo = int(cajones[c]) * float(precio[c])
        costo_total = costo_total + costo
    return costo_total

 



costo = costo_camion('camion.csv')
print('costo total: ',costo)
    
