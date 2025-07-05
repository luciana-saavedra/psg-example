postres_jane = {"Lemon Pie", "Brownie", "Tarta de Manzana", "Helado de Chocolate", "Flan"}
postres_jhon = {"Carrot Cake", "Croissant de Chocolate", "Lemon Pie", "Tarta de Manzana", "Pudding"}

postres_en_comun = postres_jane & postres_jhon
porcentaje = (len(postres_en_comun) / len(postres_jane)) * 100

mensaje = "son compatibles" if porcentaje > 50 else "deben replantear su relación"
print(f"Jane y Jhon {mensaje}")