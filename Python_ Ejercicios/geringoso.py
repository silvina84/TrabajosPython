#Ejercicio geringoso
cadena = 'boligoma'
cadena_total = ' '
print('Palabra a transformar en geringoso: ',cadena)
for c in range(len(cadena)):
    caracter = cadena[c]
    if caracter == 'a':
        ger1='pa'
        corta_a = cadena[c-1:c+1]
        ger_a = corta_a+ger1
        cadena_total+=ger_a
    if caracter == 'e':
        ger2='pe'
        corta_e = cadena[c-1:c+1]
        ger_e = corta_e+ger2
        cadena_total+=ger_e
    if caracter == 'i':
        ger3='pi'
        corta_i = cadena[c-1:c+1]
        ger_i =corta_i+ger3
        cadena_total+=ger_i
    if caracter == 'o':
        ger4='po'
        corta_o = cadena[c-1:c+1]
        ger_o =corta_o+ger4
        cadena_total+= ger_o
    if caracter == 'u':
        ger5='pu'
        corta_u = cadena[c-1:c+1]
        ger_u = corta_u+ger5
        cadena_total+=ger_u


print('Palabra formada en geringoso: ',cadena_total)
    

    
    
   
     
        

       
        
    
    
    
    
       
