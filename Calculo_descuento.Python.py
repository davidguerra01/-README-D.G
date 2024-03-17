# Calcular descuento en compras
def calcular_descuento(monto_total, porcentaje_descuento=0.20):
  """Calcula el descuento en función del monto total de la compra.

  Args:
    monto_total: El monto total de la compra.
    porcentaje_descuento: El porcentaje de descuento a aplicar (el 20%).

  Returns:
    El monto del descuento calculado.
  """

  descuento = monto_total * porcentaje_descuento
  return descuento


# Obtener el monto total de la compra
monto_total = float(input("Ingrese el monto total de la compra: "))

# Calcular el descuento
descuento = calcular_descuento(monto_total)

# Calcular el monto final a pagar
monto_final = monto_total - descuento

# Mostrar el monto final a pagar
print(f"El monto final a pagar es: {monto_final}")