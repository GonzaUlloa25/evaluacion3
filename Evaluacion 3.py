"""
La empresa de tours y expediciones “SurExplora” necesita desarrollar un sistema que permita registrar las reservas de sus
clientes para sus tours en la Patagonia Chilena. Para el funcionamiento del sistema se requiere las siguientes funcionalidades:
1. Registrar Reserva
2. Listar Todas las Reservas
3. Imprimir Detalle de Reservas por Destino
4. Salir del Programa

Registrar Reserva Para registrar una reserva se requiere lo siguiente: Nombre y apellido del cliente, ciudad de origen, detalle del
tour. Por ejemplo, la empresa ofrece tours a Torres del Paine, Carretera Austral y Chiloé. Debe permitir seleccionar entre 1 de las
3 opciones e ingresar la cantidad de personas para el tour. Por lo tanto, un detalle de reserva podría verse registrado de la
siguiente manera:
Debe validar que todos los datos sean ingresados.
Listar Reservas Debe mostrar en la pantalla la lista de todas las reservas realizadas similar al ejemplo anterior de registro de
reservas.
Imprimir Detalle de Reservas por Destino Para imprimir el detalle de reservas, el usuario debe seleccionar alguno de los destinos
donde es posible realizar un tour. Estos destinos deben estar previamente definidos en algún tipo de colección de Python en el
código y por lo menos deben ser tres. Por ejemplo: Torres del Paine, Carretera Austral, Chiloé. Al seleccionar uno de los destinos,
se generará un archivo de texto (.txt) con el detalle de las reservas que se deberá llevar a ese destino. Este debe tener la misma
forma del registro completo de las opciones anteriores pero en archivo de texto.
"""
reservas = []
# El menú de acciones
def mostrar_menu():
    print("Bienvenido a SurExplora")
    print("1. Registrar Reserva")
    print("2. Listar todas las reservas")
    print("3. Imprimir detalle de reservas por destino")
    print("4. Salir del programa")

# El usuario ingresa sus datos
def registrar_reserva():
    nombre = input("Ingrese su nombre: ")
    apellido = input("Ingrese su apellido: ")
    ciudad = input("Ingrese su ciudad de origen: ")
    personas = int(input("Ingrese la cantidad de personas: "))
    destino = elegir_destino()
    reserva = {
        "nombre": nombre,
        "apellido": apellido,
        "ciudad": ciudad,
        "personas": personas,
        "destino": destino
    }
    reservas.append(reserva)
    print("Reserva registrada con éxito")

# Aquí se muestra la lista de posibles destinos y el usuario elige uno
def elegir_destino():
    catalogo = ["torres del paine", "carretera austral", "chiloé"]
    print("Destinos disponibles: ", catalogo)
    destino = input("Ingrese el destino a escoger: ").lower()
    while destino not in catalogo:
        print("Destino no registrado. Intente nuevamente.")
        destino = input("Ingrese el destino a escoger: ").lower()
    print("Destino registrado con éxito")
    return destino

# Aquí se muestra la lista de reservas
def listar_reservas():
    print("Reservas registradas:")
    for reserva in reservas:
        print(f"Nombre: {reserva['nombre']}")
        print(f"Apellido: {reserva['apellido']}")
        print(f"Ciudad: {reserva['ciudad']}")
        print(f"Destino: {reserva['destino']}")
        print(f"Personas: {reserva['personas']}\n")

# Aquí se imprimen los detalles de las reservas en un archivo
def imprimir_detalle_reservas():
    try:
        with open("reservas.txt", "w") as archivo:
            for reserva in reservas:
                archivo.write(f"Nombre: {reserva['nombre']}\n")
                archivo.write(f"Apellido: {reserva['apellido']}\n")
                archivo.write(f"Ciudad: {reserva['ciudad']}\n")
                archivo.write(f"Destino: {reserva['destino']}\n")
                archivo.write(f"Personas: {reserva['personas']}\n\n")
        print("Detalles de reservas impresos en 'reservas.txt'")
    except Exception as e:
        print(f"No se pudo abrir el archivo: {e}")

# El menú definitivo está aquí
def menu():
    while True:
        mostrar_menu()
        opcion = input("Ingrese una opción: ")
        if opcion == "1":
            registrar_reserva()
        elif opcion == "2":
            listar_reservas()
        elif opcion == "3":
            imprimir_detalle_reservas()
        elif opcion == "4":
            print("Saliendo del programa")
            break
        else:
            print("Opción inválida, por favor intente nuevamente.")

menu()