def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "Error: no se puede dividir entre cero."
    return a / b

def mostrar_menu():
    print("\n--- Calculadora ---")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")

def calculadora():
    while True:
        mostrar_menu()
        opcion = input("Elige una opción (1-5): ")

        if opcion == '5':
            print("¡Hasta luego!")
            break

        if opcion in ['1', '2', '3', '4']:
            try:
                num1 = float(input("Ingresa el primer número: "))
                num2 = float(input("Ingresa el segundo número: "))
            except ValueError:
                print("Por favor, ingresa números válidos.")
                continue

            if opcion == '1':
                resultado = sumar(num1, num2)
            elif opcion == '2':
                resultado = restar(num1, num2)
            elif opcion == '3':
                resultado = multiplicar(num1, num2)
            elif opcion == '4':
                resultado = dividir(num1, num2)

            print(f"Resultado: {resultado}")
        else:
            print("Opción no válida. Intenta de nuevo.")

# Ejecutar la calculadora
calculadora()

#Usa funciones para cada operación.

# comentario:Muestra un menú interactivo, permite salir del programa, maneja errores básicos como división por cero y entradas no numéricas.