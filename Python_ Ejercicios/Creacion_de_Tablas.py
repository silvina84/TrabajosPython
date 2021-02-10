#Creando tablas

from selenium import webdriver
import xlsxwriter
import time

driver = webdriver.Chrome("C:\\chromedriver_win32\\chromedriver.exe")
driver.get("https://www.w3schools.com/html/html_tables.asp")

#Creamos el archivo y el la hoja donde guardar los ddatos en Excel
libro = xlsxwriter.Workbook('Datos_Tabla_Web.xlsx')
hoja = libro.add_worksheet()
time.sleep(2)

valor = driver.find_element_by_xpath("//*[@id='customers']/tbody/tr[1]/th[1]").text

filas = len(driver.find_elements_by_xpath("//*[@id='customers']/tbody/tr"))
col = len(driver.find_elements_by_xpath("//*[@id='customers']/tbody/tr[1]/th"))

#Definimos el ancho de la columna para escribir el texto
hoja.set_column('A:A', 30)
hoja.set_column('B:B', 30)
hoja.set_column('C:C', 30)

#Damos algunos formatos a la cabecera
cabecera = libro.add_format()
cabecera.set_font_color('blue')
cabecera.set_font_size(16)
cabecera.set_bold()

#Escribimos la cabecera
for j in range(1,col+1):
    titulo = driver.find_element_by_xpath("//*[@id='customers']/tbody/tr[1]/th["+str(j)+"]").text
    print(titulo, end='           ')
    c = j-1
    hoja.write(0,c,titulo)

#Damos formato a esa cabecera
hoja.write('A1','Company',cabecera)
hoja.write('B1','Contact',cabecera)
hoja.write('C1','Country',cabecera)
  
print("\n")
#Escribimos los datos en el archivo excel
for n in range(2, filas+1):
    for b in range(1, col+1):
        dato = driver.find_element_by_xpath("//*[@id='customers']/tbody/tr["+str(n)+"]/td["+str(b)+"]").text
        print(dato, end='           ')
        a= n-1
        k= b-1
        hoja.write(a,k,dato)
    print()

libro.close()
driver.quit()    
          
          
          
          
