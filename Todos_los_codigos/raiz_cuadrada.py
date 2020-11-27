import math
def raiz(dato,error_permitido, valor_inicial):
    resultado=((1/2)*(valor_inicial + (dato/valor_inicial)))
    if abs(valor_inicial-resultado) < error_permitido:
        return resultado
    return raiz(dato, error_permitido,resultado)

    



# def raiz(dato,error_permitido, valor_inicial):
#     resultado= ((1/2)*(valor_inicial + (dato/valor_inicial)))

#     while abs(valor_inicial-resultado)>error_permitido:
#         valor_inicial=resultado
#         resultado = ((1/2)*(valor_inicial + (dato/valor_inicial)))
#     return resultado

print(raiz(math.pi, 1e-10, -50) )