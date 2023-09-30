empresas = [7,4,8,5,6,8,200,1000]

def facturacion_media(empresas):
    total = sum(empresas)
    media = total / len(empresas)
    return media

resultado = facturacion_media(empresas)

print("La facturacon media es de: ", resultado)
