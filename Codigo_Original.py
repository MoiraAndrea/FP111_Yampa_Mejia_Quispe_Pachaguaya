print("----- REGISTRO DE USUARIO -----")

nombre = input("Ingrese su nombre: ")
edad = int(input("Ingrese su edad: "))
nota = float(input("Ingrese su nota: "))
opcion = int(input("Ingrese una opción: "))

if edad >= 18:
    print(nombre, "es mayor de edad.")
else:
    print(nombre, "es menor de edad.")

print("Nota registrada:", nota)

if opcion == 1:
    print("Mostrar información")
elif opcion == 2:
    print("Modificar información")
elif opcion == 3:
    print("Eliminar información")
else:
    print("Opción no válida")

print("Proceso finalizado.")