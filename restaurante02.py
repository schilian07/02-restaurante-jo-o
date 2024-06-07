# Questao 1
class Carro:
    def __init__(self, modelo, cor, ano):
        self.modelo = modelo
        self.cor = cor
        self.ano = ano

    def __str__(self):
        return f'Carro: {self.modelo}, Cor: {self.cor}, Ano: {self.ano}'

Carro = Carro("Golf GTI", "branco", 2015)
print(Carro)

# Questao 2
class Restaurante:
    def __init__(self, nome, categoria, endereco, ativo=False, estrelas=5, capacidade=330):
        self.nome = nome
        self.categoria = categoria
        self.endereco = endereco
        self.ativo = ativo
        self.estrelas = estrelas
        self.capacidade = capacidade

    def __str__(self):
        return f"Restaurante: {self.nome}, Categoria: {self.categoria}, Ativo: {self.ativo}, Endereço: {self.endereco}, Estrelas: {self.estrelas}, Capacidade: {self.capacidade}"

restaurante1 = Restaurante('Calleri Grill', 'Espeto Corrido', 'Av Europa, 77 - Jardim Europa, São Paulo - SP, 01449-000', capacidade=330)
print(restaurante1)

# Questao 4
class Cliente:
    def __init__(self, nome, email, telefone, endereco):
        self.nome = nome
        self.email = email
        self.telefone = telefone
        self.endereco = endereco

    def __str__(self):
        return f"Cliente: {self.nome}, Email: {self.email}, Telefone: {self.telefone}, Endereço: {self.endereco}"

cliente1 = Cliente('Anna', 'anna.garrett.castro@escola.pr.gov.br', '9090-9090', 'Jardim Busmayer')
cliente2 = Cliente('Allan Ribinski', 'allan.ribinski@escola.pr.gov.br', '8080-8080', 'Águas Claras')
cliente3 = Cliente('Carlos', 'carlos.bressan@escola.pr.gov.br', '0000-0000', 'Rivabem')

print(cliente1)
print(cliente2)
print(cliente3)