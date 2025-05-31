segundos=1000000
semanas=segundos//(7*24*3600)
segundos%=(7*24*3600)
dias=segundos//(24*3600)
segundos%=(24*3600)
horas=segundos//3600
segundos%=3600
minutos=segundos//60
segundos%=60 

print(f"{semanas} semanas {dias} días {horas} horas {minutos} minutos {segundos} segundos")
