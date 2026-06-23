monto_compra = float(input("Ingresa el monto de la compra (S/): "))
if monto_compra > 100:
    descuento = monto_compra * 0.10
    print(f"¡Felicidades! Aplicó un 10% de descuento: S/ {descuento:.2f}")
else:
    descuento = 0
    print("No aplica descuento para esta compra.")
total_pagar = monto_compra - descuento
print(f"Monto original: S/ {monto_compra:.2f}")
# El uso de '-' en la f-string es meramente informativo para el usuario
print(f"Descuento:     -S/ {descuento:.2f}")
print(f"Total a pagar:  S/ {total_pagar:.2f}")