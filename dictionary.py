pessoa = {"nome": 'João', "idade": 30, "cidade": "São Paulo"}
print("Meu dicionário de exemplo:", pessoa)

print("Nome:{}\nIdade:{}\nCidade:{}".format(pessoa['nome'],pessoa["idade"],pessoa["cidade"]))

pessoa["sobrenome"] = "Affiune"
print("Sobrenome:{}".format(pessoa["sobrenome"]))

del pessoa["sobrenome"] # Exclue o par chave-valor
print(pessoa)

chaves = list(pessoa.keys())
print("Chaves do meu dicionário:", chaves)
print("Primeira chave:", chaves[0]) # Para acessar assim precisa do cast list em cima

valores = list(pessoa.values())
print("Valores do dicionário:", valores)
print("Primeiro valor do dicionário:", valores[0])

itens = list(pessoa.items())
print("Pares chave-valor do dicionário:", itens)
print("Primeiro valor:", itens[0][0])

for chave, valor in pessoa.items():
    print(f"{chave}:{valor}")