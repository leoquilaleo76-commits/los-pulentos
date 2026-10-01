class Departamento:
    def __init__(self, id_departamento: int, nombre: str, piso: int):
        self.id_departamento = id_departamento
        self.nombre = nombre
        self.piso = piso

    def __str__(self):
        return (
            f"ID Departamento: {self.id_departamento}\n"
            f"Nombre: {self.nombre}\n"
            f"Piso: {self.piso}"
        )


# Lista para guardar departamentos
departamentos = []


def agregar_departamento():
    try:
        id_departamento = int(input("Ingrese ID del departamento: "))
        nombre = input("Ingrese nombre del departamento: ")
        piso = int(input("Ingrese piso del departamento: "))

        departamento = Departamento(
            id_departamento,
            nombre,
            piso
        )

        departamentos.append(departamento)

        print("\nDepartamento agregado correctamente.\n")

    except ValueError:
        print("\nError: ID y piso deben ser números.\n")


def mostrar_departamentos():
    if len(departamentos) == 0:
        print("\nNo existen departamentos registrados.\n")
    else:
        print("\n===== DEPARTAMENTOS =====")

        for departamento in departamentos:
            print("-------------------------")
            print(departamento)

        print("-------------------------\n")


def buscar_departamento():
    try:
        id_buscar = int(input("Ingrese ID del departamento: "))

        for departamento in departamentos:
            if departamento.id_departamento == id_buscar:
                print("\nDepartamento encontrado:")
                print(departamento)
                print()
                return

        print("\nDepartamento no encontrado.\n")

    except ValueError:
        print("\nError: debe ingresar un número.\n")


def eliminar_departamento():
    try:
        id_eliminar = int(input("Ingrese ID del departamento a eliminar: "))

        for departamento in departamentos:
            if departamento.id_departamento == id_eliminar:
                departamentos.remove(departamento)
                print("\nDepartamento eliminado correctamente.\n")
                return

        print("\nDepartamento no encontrado.\n")

    except ValueError:
        print("\nError: debe ingresar un número.\n")


def menu():
    while True:
        print("================================")
        print("      MENÚ DEPARTAMENTO")
        print("================================")
        print("1.- Agregar departamento")
        print("2.- Mostrar departamentos")
        print("3.- Buscar departamento")
        print("4.- Eliminar departamento")
        print("0.- Salir")
        print("================================")

        opcion = input("Ingrese una opción: ")

        if opcion == "1":
            agregar_departamento()

        elif opcion == "2":
            mostrar_departamentos()

        elif opcion == "3":
            buscar_departamento()

        elif opcion == "4":
            eliminar_departamento()

        elif opcion == "0":
            print("\nPrograma finalizado.")
            break

        else:
            print("\nOpción incorrecta. Intente nuevamente.\n")


menu()