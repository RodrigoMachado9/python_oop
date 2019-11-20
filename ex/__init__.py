class Pessoa:

    def __init__(self):
        self.nome = None
        self.idade = None


if __name__ == "__main__":
    p = Pessoa()

    p.nome = input("digite o seu nome: ")
    p.idade = input("digite a sua idade: ")

    print(f"Nome: {p.nome} - Idade: {p.idade}")

