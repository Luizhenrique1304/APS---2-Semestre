def criptografar(texto, chave):
    # Função para criptografar um texto usando a cifra de César
    resultado = ""
    for char in texto:
        if char.isupper():
            # Desloca letras maiúsculas
            resultado += chr((ord(char) - ord('A') + chave) % 26 + ord('A'))
        elif char.islower():
            # Desloca letras minúsculas
            resultado += chr((ord(char) - ord('a') + chave) % 26 + ord('a'))
        else:
            # Mantém caracteres não alfabéticos
            resultado += char
    return resultado

def descriptografar(texto, chave):
    # Função para descriptografar um texto usando a cifra de César
    resultado = ""
    for char in texto:
        if char.isupper():
            # Desloca letras maiúsculas
            resultado += chr((ord(char) - ord('A') - chave) % 26 + ord('A'))
        elif char.islower():
            # Desloca letras minúsculas
            resultado += chr((ord(char) - ord('a') - chave) % 26 + ord('a'))
        else:
            # Mantém caracteres não alfabéticos
            resultado += char
    return resultado

def menu():

    # Função para exibir o menu e interagir com o usuário

    while True:
        # Exibe o menu
        print("\n======== Menu de Criptografia ========")
        print("[1] Criptografar")
        print("[2] Descriptografar")
        print("[3] Sair")
        escolha = input("Escolha uma opção(1-3): ")

        # Processa a escolha do usuário
        if escolha == '1':
            # Solicita o texto e a chave para criptografia
            texto = input("Digite o texto a ser criptografado: ")
            try:
                chave = int(input("Digite a chave de criptografia (número inteiro): "))
                print("Texto Criptografado:", criptografar(texto, chave))
            except ValueError:
                print("Chave inválida! Por favor, insira um número inteiro. ")

        elif escolha == '2':
            # Solicita o texto e a chave para descriptografia
            texto = input("Digite o texto a ser descriptografado: ")
            try:
                chave = int(input("Digite a chave de descriptografia (número inteiro): "))
                print("Texto Descriptografado:", descriptografar(texto, chave))
            except ValueError:
                print("Chave inválida! Por favor, insira um número inteiro. ")

        elif escolha == '3':
            # Sai do programa
            print("Saindo do programa...Até logo!")
            break
        else:
            # Opção inválida
            print("Opção inválida! Por favor, escolha uma opção válida.")

if __name__ == "__main__":
    menu()