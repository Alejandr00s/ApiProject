from API.API import get_database


def user_interface():
    department_name = input("Ingrese el nombre del departamento: ").upper()
    record_number = int(input("Ingrese el límite de registros, máximo 20: "))
    if record_number > 20:
        print("El número de registros debe ser 20 o menos. Estableciendo el límite a 20")
        record_number = 20
    return department_name, record_number
