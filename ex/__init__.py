class Pessoa:

    def __init__(self):
        self.nome = None
        self.idade = None


if __name__ == "__main__":
    p = Pessoa()

    p.nome = input("type your name: ")
    p.idade = input("type your age: ")

    print(f"Nome: {p.nome} - Idade: {p.idade}")

