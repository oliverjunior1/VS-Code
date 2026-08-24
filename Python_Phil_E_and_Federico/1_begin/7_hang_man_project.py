import random

def jogo_da_forca():
    # Lista de palavras possíveis
    palavras = ["python", "programacao", "computador", "inteligencia", "algoritmo", "dados"]

    # Escolhe uma palavra aleatória
    palavra = random.choice(palavras)
    letras_descobertas = ["_" for _ in palavra]
    letras_erradas = []
    vidas = 6

    print("Bem-vindo ao jogo da forca!")
    print(" ".join(letras_descobertas))

    # Loop principal do jogo
    while vidas > 0 and "_" in letras_descobertas:
        letra = input("Digite uma letra: ").lower()

        # Verifica se a entrada é válida
        if len(letra) != 1 or not letra.isalpha():
            print("Entrada inválida. Digite apenas uma letra.")
            continue

        # Verifica se a letra está na palavra
        if letra in palavra:
            for i, l in enumerate(palavra):
                if l == letra:
                    letras_descobertas[i] = letra
            print("Boa! Você acertou uma letra.")
        else:
            if letra not in letras_erradas:
                letras_erradas.append(letra)
                vidas -= 1
                print(f"Letra errada! Você perdeu uma vida. Vidas restantes: {vidas}")
            else:
                print("Você já tentou essa letra antes.")

        # Mostra o progresso
        print("Palavra: ", " ".join(letras_descobertas))
        print("Letras erradas: ", ", ".join(letras_erradas))

    # Verifica resultado final
    if "_" not in letras_descobertas:
        print("Parabéns! Você completou a palavra:", palavra)
    else:
        print("Game Over! A palavra era:", palavra)

# Executa o jogo
if __name__ == "__main__":
    jogo_da_forca()
