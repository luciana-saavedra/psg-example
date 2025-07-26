for i in range(1, 101):
    #Primero verificamos si es divisible entre 5 y 7
    if i % 5 == 0 and i % 7 == 0:
        print("FizzBuzz")
    #Si solo es divisible entre 5
    elif i % 5 == 0:
        print("Fizz")
    #Si solo es divisible entre 7
    elif i % 7 == 0:
        print("Buzz")
    # Si no es divisible entre ninguno de los dos, imprimimos el número
    else:
        print(i)