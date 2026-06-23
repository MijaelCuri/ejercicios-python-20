promedio = float(input("Ingresa tu promedio final: "))
if promedio >= 18:
    print("Resultado: ¡Felicidades! Obtuviste una Beca completa.")
elif promedio >= 15:
    print("Resultado: Obtuviste una Media beca.")
elif promedio >= 11:
    print("Resultado: Regular (Estudios financiados de manera regular, Sin beca).")
else:
    print("Resultado: Desaprobado.")