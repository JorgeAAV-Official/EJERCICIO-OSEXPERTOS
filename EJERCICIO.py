def revision_destartalado():
    while True: 
        print("¿Hola, cómo está? necesita que le colabore con algo?")
        rta = input("RESPONDA: si o no: ")
        
        while rta.strip().lower() not in ("si", "no"):
            print("No le entiendo, si o no??")
            rta = input("RESPONDA: si o no: ").strip().lower()

        if rta.strip().lower() == "si":
            print("Ok, cuéntame qué sucede con el destartalado. \n") 
            opciones = "1. El carro no arranca. 2. El carro arranca pero se apaga al acelerar. 3. El carro arranca pero el color del humo es... "
            print(opciones)
            respuesta = input("Vea, lo que pasa es que: ")

            if respuesta == "1":  
                print("Las luces del tablero están apagadas o prendidas?")
                luces_tablero = input("¿Apagadas o Prendidas? Responda. ").strip().lower()
                while luces_tablero.strip().lower() not in ("prendidas", "apagadas"):
                 print("No le entiendo, vuelva a repetir. ")
                 luces_tablero = input("RESPONDA: prendidas o apagadas: ").strip().lower()
                if luces_tablero == "prendidas":
                    print("\n Ahhhh no, eso es pq tiene un fallo en el motor de arranque ")
                elif luces_tablero == "apagadas":
                    print("\n Ahhhh no, eso es pq tiene la batería descargada ")

            elif respuesta == "2":
                print("\n Ahhhh no, eso es pq tiene un problema en el suministro de combustible ")

            elif respuesta == "3":
                color_humo = input("¿Blanco o Negro? Responda. ").strip().lower()
                while color_humo.strip().lower() not in ("blanco", "negro"):
                 print("No le entiendo, vuelva a repetir. ")
                 color_humo = input("¿Blanco o Negro? Responda. ").strip().lower()
                if color_humo == "negro":
                    print("\n Ahhhh no, lo más seguro es que eso sea pq tiene una buena mezcla de combustible ")
                elif color_humo == "blanco":
                    print("\n Ahhhh no, lo más probable es que eso sea pq tiene una falla en la junta de culata ")
                

        elif rta.strip().lower() == "no":
            print("ADIOS")
            break 

        print("\n¿¿Necesita que revise algo más??")
        final = input("RESPONDA: si o no: ").strip().lower()
        if final == "no":
            print("Nos vemos.")
            break  

revision_destartalado()










