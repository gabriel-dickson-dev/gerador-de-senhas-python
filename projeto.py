import random
import string


def gerar_senha():
  print("=" * 40)
  print("        GERADOR DE SENHAS SEGURAS        ")
  print("=" * 40)

  try:
    tamanho = int(
        input("Digite o tamanho desejado para a senha (mínimo 4): ")
    )

    if tamanho < 4:
      print("\n[Erro] A senha precisa ter pelo menos 4 caracteres.")
      return

    caracteres = (
        string.ascii_letters + string.digits + string.punctuation
    )

   
    senha = "".join(random.choice(caracteres) for _ in range(tamanho))

    print("\n" + "-" * 40)
    print(f" Senha gerada com sucesso:\n\n{senha}")
    print("-" * 40)

  except ValueError:
    print(
        "\n[Erro] Entrada inválida! Por favor, digite apenas números inteiros"
        " válidos."
    )


if __name__ == "__main__":
  gerar_senha()
