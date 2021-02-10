##Tranformar una frase en una frase inclusiva
frase = 'todos somos programadores'
frase_final = ''
palabras = frase.split(" ")
for palabra in palabras:
    print('palabra: ',palabra)
    longitud = len(palabra)
    for c in range(len(palabra)):
        if c == longitud-2:
            corta_palabra = palabra[0:longitud-2]
            corta1=palabra[longitud-2]
            corta2=palabra[longitud-1]
            if corta1 == 'a' or corta1 == 'o':
                corta1 = 'e'
            palabra_nueva = corta_palabra + corta1 +corta2+' '
            frase_final += palabra_nueva
           
print('frase_inclusiva: ',frase_final)            








            
        
