precio = float(input("Ingresa un precio: "))
descuento = 0.15

precio_desc = precio * (1 - descuento)
print(f"\nPrecio original:     {precio:,.2f} €")
print(f"Descuento aplicado:  {descuento:.0%}")
print(f"Precio final:        {precio_desc:,.2f} €")