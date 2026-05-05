nombre=input(str("Ingrese su nombre: "))
edad=int(input("Ingrese su edad: "))
print("Su edad es: ", edad)
print("Su nombre es:", nombre)
if edad < 18:
    print("Acceso denegado")
elif edad >= 18:
    print("Acceso básico")
elif edad >= 26:
    print("Acceso intermedo")
elif edad >= 40:
    print("Acceso avanzado")
elif edad <= 0:
    print("La edad ingresada no es válida")