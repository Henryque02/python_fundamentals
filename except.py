print("Exemplo de captura de exceções")
while True:
    try:
        numero = int(input("Digite um número inteiro: "))
        resultado = 10/numero
    except Exception as e:
        print(f"Erro: {e}")
    except ValueError as e:
        print(f"Erro de value error: {e}")
        raise ValueError("Tipo de variaveis incompativeis")
    else:
        print(f"Resultado: {resultado}")
    """finally:
        print("Operação finalizada")"""