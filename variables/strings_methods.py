# Strings em python são imutáveis

nome = "Henryque Affiune"
print(nome.upper())
print(nome.lower())
print(nome[0])
print(nome.count("e"))
print(nome.find("e")) #primeira ocorrência
print(nome.encode())
print(nome.encode().decode())
print(nome.replace("e","x"))
print("-".join(nome))
print(nome.split(" "))
nome2 = "XHenryque AffiuneX"
print(nome2.strip("X")) #lstrip rstrip
print(nome.startswith("Hen"))
print("ryq" in nome)
print("ryq" not in nome)