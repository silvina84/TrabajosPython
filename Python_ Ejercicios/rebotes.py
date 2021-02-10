# rebotes.py
# Archivo de ejemplo
# Ejercicio
altura=100
cantidad=10
cont=0
salta=0
valor_fijo=3/5
while cont <cantidad:
    salta=valor_fijo*altura
    altura=salta
    print(cont+1,' La altura que salto es: ',round(salta,4))
    cont=cont+1

