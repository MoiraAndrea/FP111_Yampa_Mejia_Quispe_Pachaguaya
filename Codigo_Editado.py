print("----- REGISTRO DE USUARIO -----")

nombre = input("Ingrese su nombre: ")
edad = int(input("Ingrese su edad: "))
nota = float(input("Ingrese su nota: "))

print("\nMENÚ")
print("1. Mostrar información")
print("2. Modificar información")
print("3. Eliminar información")

opcion = int(input("Seleccione una opción: "))

if edad >= 18:
    print(f"{nombre} es mayor de edad.")
else:
    print(f"{nombre} es menor de edad.")

print(f"Nota registrada: {nota}")

if opcion == 1:
    print("Mostrar información")
elif opcion == 2:
    print("Modificar información")
elif opcion == 3:
    print("Eliminar información")
else:
    print("Opción no válida")

print("Proceso finalizado.")