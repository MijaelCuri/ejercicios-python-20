TIPO_DE_CAMBIO = 3.70
soles = float(input("Ingresa la cantidad en soles (S/): "))
dolares = soles / TIPO_DE_CAMBIO
print(f"S/. {soles:.2f} soles equivalen a $ {dolares:.2f} dólares.")