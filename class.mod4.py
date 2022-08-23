class Clientes:
    total_clientes = 0

    def __init__(self, nome, idade ):
        self.nome = nome
        self.idade = idade
        Clientes.total_clientes = Clientes.total_clientes + 1

cliente_1 = Clientes("Carlos", "24")
cliente_2 = Clientes("Maria", "55")
cliente_3 = Clientes("João", "18")

print(cliente_1.total_clientes)
print(cliente_2.total_clientes)
print(cliente_3.total_clientes)
print(Clientes.total_clientes)




