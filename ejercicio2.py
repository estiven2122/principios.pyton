#Ejercicio cálculo de precio total de una compra

#Supongamos que esta trabajando en una pequeña empresa que vende productos y necesitas crear un programa que calcule el total de una compra. incluyendo el impuesto de las ventas.
#El prigrama debera solicitar al usuario el nombre del producto, la cantidad comptada y el precio unitario del producto
#luego calculara el precio total y mostrará un resumen de la compra.

def calcular_precio_total(cantidad, precio_unitario):
    #calcular el precio total de la compra
    precio_total = cantidad * precio_unitario
    return precio_total

def main():
    print("Bienvenido a tu tienda")
    nombre_producto = input("Ingresa el nombre del producto")
    cantidad = int(input("Ingresa la cantidad comprada: "))
    precio_unitario = float(input("Ingresa el precio unitario: "))

    if cantidad <- 0 or precio_unitario <- 0:
        print("Debe de introtroducir un numero correcto")
    else:
        precio_total = calcular_precio_total(cantidad,precio_unitario)
        impuesto_ventas = precio_total * 0.21
        precio_total_impuestos = precio_total - impuesto_ventas

    #Mostrar resumen de la compra
    print("Resumen de compra: ")
    print(f"Cantidad: {nombre_producto}")
    print(f"cantidad: {cantidad}")
    print(f"precio unitario: {precio_unitario:.2f}")
    print(f"precio total: {precio_total:.2f}")
    print(f"IVA (21%): {impuesto_ventas:.2f}")
    print(f"Total con impuestos: {precio_total_impuestos:.2f}")

main()
