# ==========================================
# CLASE PACIENTE
# ==========================================

class Paciente:
    def __init__(self, rut: str, nombre: str, edad: int, prevision: str):
        self.rut = rut
        self.nombre = nombre
        self.edad = edad
        self.prevision = prevision

    def __str__(self):
        return (
            f"RUT: {self.rut}\n"
            f"Nombre: {self.nombre}\n"
            f"Edad: {self.edad}\n"
            f"Previsión: {self.prevision}"
        )


# ==========================================
# LISTA DE PACIENTES
# ==========================================

pacientes: list[Paciente] = [
    Paciente("11.111.111-1", "Juan Perez", 30, "Fonasa"),
    Paciente("22.222.222-2", "Maria Gonzalez", 25, "Isapre")
]


# ==========================================
# LEER NÚMERO
# ==========================================

def leer_numero(mensaje: str) -> int:
    while True:
        try:
            numero = int(input(mensaje))
            return numero
        except ValueError:
            print("Error: Debe ingresar un número entero.")


# ==========================================
# MENÚ PRINCIPAL
# ==========================================

def menu() -> int:
    print("\n" + "=" * 30)
    print("MENÚ CLÍNICA")
    print("=" * 30)
    print("1.- Agregar paciente")
    print("2.- Editar paciente")
    print("3.- Eliminar paciente")
    print("4.- Mostrar un paciente")
    print("5.- Mostrar todos los pacientes")
    print("0.- Salir")
    print("=" * 30)

    opcion = leer_numero("Ingrese una opción: ")

    return opcion


# ==========================================
# AGREGAR PACIENTE
# ==========================================

def agregar_paciente() -> None:
    print("\nAGREGAR PACIENTE")
    print("-" * 30)

    rut = input("Ingrese RUT del paciente: ")
    nombre = input("Ingrese nombre del paciente: ")
    edad = leer_numero("Ingrese edad del paciente: ")

    print("\nTipo de previsión:")
    print("1.- Fonasa")
    print("2.- Isapre")
    print("3.- Particular")
    print("4.- Otro")

    opcion = leer_numero("Seleccione una previsión: ")

    if opcion == 1:
        prevision = "Fonasa"

    elif opcion == 2:
        prevision = "Isapre"

    elif opcion == 3:
        prevision = "Particular"

    elif opcion == 4:
        prevision = "Otro"

    else:
        print("Opción de previsión inválida.")
        return

    nuevo_paciente = Paciente(
        rut,
        nombre,
        edad,
        prevision
    )

    pacientes.append(nuevo_paciente)

    print("\nPaciente agregado exitosamente.")
    print(f"Total de pacientes: {len(pacientes)}")


# ==========================================
# BUSCAR PACIENTE
# ==========================================

def buscar_paciente():
    rut = input("Ingrese RUT del paciente: ")

    for paciente in pacientes:
        if paciente.rut == rut:
            return paciente

    return None


# ==========================================
# MOSTRAR UN PACIENTE
# ==========================================

def imprimir_paciente() -> None:
    paciente = buscar_paciente()

    if paciente is not None:
        print("\nPACIENTE ENCONTRADO")
        print("-" * 30)
        print(paciente)

    else:
        print("No se encontró el paciente.")


# ==========================================
# MOSTRAR TODOS LOS PACIENTES
# ==========================================

def imprimir_pacientes() -> None:

    if len(pacientes) == 0:
        print("No hay pacientes registrados.")

    else:
        print("\nLISTA DE PACIENTES")
        print("=" * 30)

        for paciente in pacientes:
            print(paciente)
            print("-" * 30)


# ==========================================
# ELIMINAR PACIENTE
# ==========================================

def eliminar_paciente() -> None:
    paciente = buscar_paciente()

    if paciente is not None:
        pacientes.remove(paciente)
        print("Paciente eliminado exitosamente.")

    else:
        print("No se encontró el paciente.")


# ==========================================
# EDITAR PACIENTE
# ==========================================

def editar_paciente() -> None:
    paciente = buscar_paciente()

    if paciente is None:
        print("No se encontró el paciente.")
        return

    print("\nPACIENTE ENCONTRADO")
    print("-" * 30)
    print(paciente)

    print("\nMENÚ DE EDICIÓN")
    print("1.- Editar nombre")
    print("2.- Editar edad")
    print("3.- Editar previsión")
    print("0.- Volver")

    opcion = leer_numero("Ingrese una opción: ")

    if opcion == 1:
        nuevo_nombre = input("Ingrese nuevo nombre: ")
        paciente.nombre = nuevo_nombre

        print("Nombre actualizado correctamente.")

    elif opcion == 2:
        nueva_edad = leer_numero("Ingrese nueva edad: ")
        paciente.edad = nueva_edad

        print("Edad actualizada correctamente.")

    elif opcion == 3:
        print("\nTIPO DE PREVISIÓN")
        print("1.- Fonasa")
        print("2.- Isapre")
        print("3.- Particular")
        print("4.- Otro")

        opcion_prevision = leer_numero(
            "Seleccione una previsión: "
        )

        if opcion_prevision == 1:
            paciente.prevision = "Fonasa"

        elif opcion_prevision == 2:
            paciente.prevision = "Isapre"

        elif opcion_prevision == 3:
            paciente.prevision = "Particular"

        elif opcion_prevision == 4:
            paciente.prevision = "Otro"

        else:
            print("Opción inválida.")
            return

        print("Previsión actualizada correctamente.")

    elif opcion == 0:
        print("Volviendo al menú principal...")

    else:
        print("Opción inválida.")


# ==========================================
# PROGRAMA PRINCIPAL
# ==========================================

def main() -> None:

    while True:

        opcion = menu()

        if opcion == 1:
            agregar_paciente()

        elif opcion == 2:
            editar_paciente()

        elif opcion == 3:
            eliminar_paciente()

        elif opcion == 4:
            imprimir_paciente()

        elif opcion == 5:
            imprimir_pacientes()

        elif opcion == 0:
            print("Saliendo del programa...")
            break

        else:
            print("Opción inválida. Intente nuevamente.")


# ==========================================
# EJECUTAR PROGRAMA
# ==========================================

if __name__ == "__main__":
    main()