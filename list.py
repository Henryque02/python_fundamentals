minha_lista = [1,2,3,4,5,"rocketseat", True, False]

print("Minha lista de exemplo", minha_lista)

print("minha_lista[0]:", minha_lista[0])
print("minha_lista[5]:", minha_lista[5])
print("minha_lista[1:7]:", minha_lista[1:7])
print("minha_lista[:6]:", minha_lista[:6]) # Vai até o 5
print("minha_lista[2:]:", minha_lista[2:])

minha_lista.append(6)
print(minha_lista)
indice = minha_lista.index(6)
print(indice)

minha_lista.insert(2, 10) # (indice, elemento)
print(minha_lista)

elemento_removido = minha_lista.pop(3)
print(elemento_removido)
print(minha_lista)

minha_lista.remove(True) # Removeu 1 etendendo que era true
print(minha_lista)

lista_num = [7,13,22,19,72,1,3,7.5,19]
lista_num.sort()
print(lista_num)