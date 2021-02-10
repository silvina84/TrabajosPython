# hipoteca.py
# Archivo de ejemplo
# Ejercicio de hipoteca
saldo = 500000.0
tasa = 0.05
pago_mensual = 2684.11
total_pagado = 0.0
ultimo_pago_mensual = 0
mes=1

while saldo > 0:
    if round(saldo, 2) < pago_mensual:
       ultimo_pago_mensual = saldo
       saldo = ultimo_pago_mensual - saldo
    else:
        saldo = saldo * (1+tasa/12) - pago_mensual
    
    total_pagado = total_pagado + pago_mensual
    print('Mes: ',mes,' Total pagado: ',round(total_pagado, 2), 'Saldo: ',saldo)
    mes=mes+1


