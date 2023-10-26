# Se tiene un diccionario con las fechas de nacimiento de un conjunto de personas. 
# Las fechas están en formato `DD/MM/YYYY`. Ejemplo:
# 
# {
#   "Juan": "27/05/1993", 
#   "Alicia": "30/02/1990", 
#   "Alan": "23/06/1921", 
#   "Barbara": "07/11/1929", 
#   "Grace": "09/12/1906"
# }
# 
# Se pide escribir una función que reciba un diccionario con esta forma y devuelva una lista con 
# los meses del año (escritos como `MM`) donde no haya cumpleaños.
# Ejemplo:
# 
# ['01', '03', '04', '07', '08', '09', '10']

# Escribir el codigo debajo de esta linea
def meses_sin_cumpleanios(cumpleanios):
  meses_cumpleanios = ["01","02","03","04","05","06","07","08","09","10","11","12"]
  for clave in cumpleanios:
    mes = cumpleanios[clave].split("/")[1]
    if mes in meses_cumpleanios:
      meses_cumpleanios.remove(mes)
  
  return meses_cumpleanios

# Pruebas
cumpleanios = {
  "Juan": "27/05/1993", 
  "Alicia": "30/02/1990", 
  "Alan": "23/06/1921", 
  "Barbara": "07/11/1929", 
  "Grace": "09/12/1906"
}
assert meses_sin_cumpleanios(cumpleanios) == ['01', '03', '04', '07', '08', '09', '10']
