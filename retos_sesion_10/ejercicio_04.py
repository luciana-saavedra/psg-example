postres_jane = {"Lemon Pie", "Brownie", "Tarta de Manzana", "Helado de Chocolate", "Flan"}
postres_jhon = {"Carrot Cake", "Croissant de Chocolate", "Lemon Pie", "Tarta de Manzana", "Pudding"}

#Postres en común
postres_en_comun = postres_jane & postres_jhon

#Porcentaje de postres
total_postres = len(postres_jane | postres_jhon)
porcentaje = (len(postres_en_comun) / total_postres) * 100

#Mensaje basado en porcentaje
if porcentaje > 50:
    mensaje = "son compatibles"
else:
    mensaje = "deben replantear su relación"

print(f"Jane y Jhon {mensaje}")