temperatura = float(input("Ingresa la temperatura en °C: "))
if temperatura < 10:
    print("El clima está: Frío")
elif temperatura >= 10 and temperatura <= 25:
    print("El clima está: Templado")
else:
    print("El clima está: Caluroso")