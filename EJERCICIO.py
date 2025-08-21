SALUDO = print("¿HOLA, CÓMO ESTÁS? NECESITAS ALGO?")
rta = input("RESPONDE: SI o NO: ")


if rta.strip().lower() == ("si"):
    print("¡ME ALEGRO DE QUE ESTÉS BIEN!")    
elif rta.strip().lower() == ("no"):
    print("ADIOS")
else:
    print("No le entiendo, si o no??")
    rta = input("RESPONDE: SI o NO: ")

