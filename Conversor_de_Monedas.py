USD = 4000
EUR = 4400
JPY = 30

while True:
    pesos = float(input("Introduce una cantidad de pesos: "))

    print("A que moneda lo quieres CONVERTIR")
    print("Dolares (USD)")
    print("Euros (EUR)")
    print("Yenes (JPY)")
    
    con = input("")

    if con == "USD":
        resul = pesos / USD
        redondeo = round(resul,2)
        print(f"EN TOTAL TIENES {redondeo} DOLARES")

    elif con == "EUR":
        resul = pesos / EUR
        redondeo = round(resul,2)
        print(f"EN TOTAL TIENES {redondeo} EUROS")
    
    elif con == "JPY":
        resul = pesos / JPY
        redondeo = round(resul,2)
        print (f"EN TOTAL TIENES {resul} YENES")
    
    else:
        print("ESTA MONEDA NO ESTA DISPONIBLE EN EL PROGRAMA")

    salir = input("Quieres salir del programa o seguir convirtiendo monedas(Y/N):")

    if salir == "Y":
        print("SALIENDO....")
        break
    
    elif salir == "N":
        print("CONTINUANDO.......")