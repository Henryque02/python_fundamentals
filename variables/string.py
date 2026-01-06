nome_completo = "Gabriel Casemiro"

nome_completo_aspas = """Gabriel
Casemiro"""

nome_completo_quebra = "Gabriel"\
    "Casemiro"

nome = "Gabriel"
sobrenome = "Casemiro"

# Formatação

print("Nome completo (1a forma):", nome_completo) # Tem um espaço depois dos :
print("Nome completo (2a forma):" + nome_completo) # Não tem espaço depois :
print("Nome completo (3a forma): %s %s" % (nome,sobrenome))
print(f"Nome completo (4a forma):{nome} {sobrenome}")
print("Nome completo (5a forma): {} {}".format(nome, sobrenome))