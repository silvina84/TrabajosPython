#Ejemplo guardar en excel

import xlsxwriter

libro = xlsxwriter.Workbook('Mi_ejemplo.xlsx')
hoja = libro.add_worksheet()

#Definimos el ancho de la columna para escribir el texto
hoja.set_column('A:A', 30)

#Definimos el ancho de la columna para escribir el texto
hoja.set_column('B:B', 30)

cabecera = libro.add_format()
cabecera.set_font_color('blue')
cabecera.set_bold()
cabecera.set_font_size(16)

#Agregamos un formato de tipo de letra a la celda
bold = libro.add_format({'bold':True})
hoja.write('A1', 'Hello world',cabecera)
# Texto con formato
hoja.write('A2','World',bold) 
hoja.write(2,0,'Hola')
hoja.write(3,0,'Mundo')

#Insertar una imagen
#hoja.insert_image('B10','logo.png')

libro.close()
