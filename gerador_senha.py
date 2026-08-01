import secrets
import string

def gerar_senha(tamanho=16, usar_simbolos=True):
    """
    Gera uma senha segura usando o módulo 'secrets'.

    tamanho: quantidade de caracteres da senha
    usar_simbolos: se True, inclui caracteres especiais (!@#$...)
    """
    letras_minusculas = string.ascii_lowercase
    letras_maiusculas = string.ascii_uppercase
    numeros = string.digits
    simbolos = string.punctuation

    # Monta o "Alfabeto" disponível para sorteio
    alfabeto = letras_minusculas + letras_maiusculas + numeros
    if usar_simbolos:
        alfabeto += simbolos

    while True:
        senha = ''.join(secrets.choice(alfabeto) for _ in range(tamanho))

        # Garante que a senha tenha pelo menos um cada tipo
        if (any(c.islower() for c in senha)
            and any(c.isupper() for c in senha)
            and any(c.isdigit() for c in senha)
            and(not usar_simbolos or any(c in simbolos for c in senha ))):
            return senha

if __name__ == "__main__":
    senha = gerar_senha(tamanho=16)
    print(f"Senha gerada: {senha}")