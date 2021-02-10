#camion_commandline.py
import csv
import sys

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

if len(sys.argv) == 2:
    nombre_archivo = sys.argv[1]
else:
    nombre_archivo = 'Data/camion.csv'

costo = costo_camion(nombre_archivo)
print('Costo total:', costo)
