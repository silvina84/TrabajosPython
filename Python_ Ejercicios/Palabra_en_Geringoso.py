#Mostramos una palabra en geringoso
cadena = 'boligoma'
vocal_a = cadena.find('a')
vocal_i = cadena.find('i')
vocal_o = cadena.find('o')
vocal_oo = cadena.rfind('o')
corta1 = cadena[vocal_a-1:vocal_a+1]
ger1 = 'pa'
corta2 = cadena[vocal_i-1:vocal_i+1]
ger2 = 'pi'
corta3 = cadena[vocal_o-1:vocal_o+1]
ger3 = 'po'
corta4 = cadena[vocal_oo-1:vocal_oo+1]
ger4 = 'po'
cadena_total =corta3+ger3+corta2+ger2+corta4+ger4+corta1+ger1
print(vocal_a,' ',corta1,' ',corta2,' ',corta3,' ',corta4,' ',cadena_total)
