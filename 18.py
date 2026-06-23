num1 = float(input("Ingresa el primer número: "))
num2 = float(input("Ingresa el segundo número: "))
operacion = input("Ingresa la operación (+, -, *, /): ")
if operacion == "+":
    resultado = num1 + num2
    print(f"Resultado: {num1} + {num2} = {resultado}")
    
elif operacion == "-":
    resultado = num1 - num2
    print(f"Resultado: {num1} - {num2} = {resultado}")
    
elif operacion == "*":
    resultado = num1 * num2
    print(f"Resultado: {num1} * {num2} = {resultado}")
    
elif operacion == "/":
    if num2 != 0:
        resultado = num1 / num2
        print(f"Resultado: {num1} / {num2} = {resultado}")
    else:
        print("Error: No se puede dividir entre cero.")
        
else:
    print("Operación no válida. Por favor, usa +, -, * o /.")