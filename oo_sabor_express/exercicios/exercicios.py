# print('1.Atribua o valor \'Italiana\' ao atributo categoria da instância restaurante_praca da classe Restaurante.')
# print('2.Acesse o valor do atributo nome da instância restaurante_praca da classe Restaurante.')

class Restaurante: 
    nome = ''
    categoria = ''
    ativo = False

restaurante_praca = Restaurante()
restaurante_pizza = Restaurante()

restaurantes = [restaurante_praca, restaurante_pizza]
restaurante_praca.nome = 'Praça'
restaurante_praca.categoria = 'Italiana'
print(vars(restaurante_praca))

# print('3.Verifique o valor inicial do atributo ativo para a instância restaurante_praca e exiba uma mensagem informando se o restaurante está ativo ou inativo.')
if restaurante_praca.ativo:
    print('O restaurante está ativo')
else:
    print('O restaurante está inativo')

# 4 - Acesse o valor do atributo de classe categoria diretamente da classe Restaurante e armazene em uma variável chamada categoria.
categoria = Restaurante.categoria

# 5 -Altere o valor do atributo nome para 'Bistrô'.
restaurante_praca.nome = 'Bistrô'

# 6 - Crie uma nova instância da classe Restaurante chamada restaurante_pizza com o nome 'Pizza Place' e categoria 'Fast Food'.
restaurante_pizza = Restaurante()

restaurante_pizza.nome = 'Pizza Place'
restaurante_pizza.categoria = 'Fast Food'

# 7 - Verifique se a categoria da instância restaurante_pizza é 'Fast Food'.
if restaurante_pizza.categoria == 'Fast Food':
    print('A categoria é Fast Food')
else:
    print('A categoria não é Fast Food')

# 8 - Mude o estado da instância restaurante_pizza para ativo.
restaurante_pizza.ativo = True

#  9 - Imprima no console o nome e a categoria da instância restaurante_praca.

print(f'Nome: {restaurante_praca.nome}, Categoria: {restaurante_praca.categoria}')

# 10 - Refaça essa classe Musica utilizando uma forma mais concisa e expressiva, aproveitando a sintaxe simplificada do Python.
'''class Musica:
    nome = ''
    artista = ''
    duracao = int'''
class Musica:
    def __init__(self, nome='', artista='', duracao=0):
        self.nome = nome
        self.artista = artista
        self.duracao = duracao

musica1 = Musica(nome='Under Pressure', artista='Queen & David Bowie', duracao=248)
musica2 = Musica(nome='The Trooper', artista='Iron Maiden', duracao=245)
musica3 = Musica(nome='Hotel California', artista='Eagles', duracao=390)

# 1 - Implemente uma classe chamada Carro com os atributos básicos, como modelo, cor e ano. Crie uma instância dessa classe e atribua valores aos seus atributos.
# 2 - Crie uma classe chamada Restaurante com os atributos nome, categoria, ativo e crie mais 2 atributos. Instancie um restaurante e atribua valores aos seus atributos.
# 3 - Modifique a classe Restaurante adicionando um construtor que aceita nome e categoria como parâmetros e inicia ativo como False por padrão. Crie uma instância utilizando o construtor.
# 4 - Adicione um método especial __str__ à classe Restaurante para que, ao imprimir uma instância, seja exibida uma mensagem formatada com o nome e a categoria. Exiba essa mensagem para uma instância de restaurante.
# 5 - Crie uma classe chamada Cliente e pense em 4 atributos. Em seguida, instancie 3 objetos desta classe e atribua valores aos seus atributos através de um método construtor.

# Respostas

# 1) Implemente uma classe chamada Carro com os atributos básicos, como modelo, cor e ano. Crie uma instância dessa classe e atribua valores aos seus atributos.

class Carro:
    def __init__(self, modelo, cor, ano):
        self.modelo = modelo
        self.cor = cor
        self.ano = ano

# Instanciando um carro e atribuindo valores aos seus atributos
meu_carro = Carro(modelo='Fusca', cor='Azul', ano=1970)

# 2) Crie uma classe chamada Restaurante com os atributos nome, categoria, ativo e crie mais 2 atributos. Instancie um restaurante e atribua valores aos seus atributos.

class Restaurante:
    def __init__(self, nome, categoria, ativo=False, capacidade, nota_avaliacao):
        self.nome = nome
        self.categoria = categoria
        self.ativo = ativo
        self.capacidade = capacidade
        self.nota_avaliacao = nota_avaliacao

# Instanciando um restaurante e atribuindo valores aos seus atributos
restaurante_exemplo = Restaurante(nome='Comida Boa', categoria='Gourmet', ativo=True, capacidade=50, nota_avaliacao=4.5)

# 3) Modifique a classe Restaurante adicionando um construtor que aceita nome e categoria como parâmetros e inicia ativo como False por padrão. Crie uma instância utilizando o construtor.

class Restaurante:
    def __init__(self, nome, categoria, ativo=False, capacidade, nota_avaliacao):
        self.nome = nome
        self.categoria = categoria
        self.ativo = ativo
        self.capacidade = capacidade
        self.nota_avaliacao = nota_avaliacao

# Instanciando um restaurante utilizando o construtor
novo_restaurante = Restaurante(nome='Santa Marmita', categoria='Fast Food')

# 4) Adicione um método especial `__str__` à classe Restaurante para que, ao imprimir uma instância, seja exibida uma mensagem formatada com o nome e a categoria. Exiba essa mensagem para uma instância de restaurante.

class Restaurante:
    def __init__(self, nome, categoria, ativo=False, capacidade, nota_avaliacao):
        self.nome = nome
        self.categoria = categoria
        self.ativo = ativo
        self.capacidade = capacidade
        self.nota_avaliacao = nota_avaliacao

    def __str__(self):
        return f'{self.nome} | {self.categoria}'

# Exibindo uma instância do restaurante formatada
restaurante_formatado = Restaurante(nome='Bom Sabor', categoria='Tradicional')
print(restaurante_formatado)

# 5) Crie uma classe chamada `Cliente` e pense em 4 atributos. Em seguida, instancie 3 objetos desta classe e atribua valores aos seus atributos através de um método construtor.

class Cliente:
    def __init__(self, nome='', idade=0, email='', telefone=''):
        self.nome = nome
        self.idade = idade
        self.email = email
        self.telefone = telefone

# Instanciando três objetos da classe Cliente e atribuindo valores aos seus atributos através do construtor
cliente1 = Cliente(nome='Alice', idade=25, email='alice@gmail.com', telefone='123-456-7890')
cliente2 = Cliente(nome='Bob', idade=30, email='bob@gmail.com', telefone='987-654-3210')
cliente3 = Cliente(nome='Charlie', idade=22, email='charlie@gmail.com', telefone='555-123-4567')


'''Agora é sua vez! Crie uma nova classe chamada Pessoa com atributos como nome, idade e profissão. Adicione um método especial __str__ para imprimir uma representação em string da pessoa. Implemente também um método de instância chamado aniversario que aumenta a idade da pessoa em um ano. Por fim, adicione uma propriedade chamada saudacao que retorna uma mensagem de saudação personalizada com base na profissão da pessoa.'''
'''class Livro:
    def __init__(self, titulo='', autor='', paginas=0):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas

    def __str__(self):
        return f'{self.titulo} por {self.autor} - {self.paginas} páginas'

    @property
    def titulo_autor(self):
        return f'{self.titulo} por {self.autor}'

    def aumentar_paginas(self, quantidade):
        self.paginas += quantidade
'''
class Pessoa:
    def __init__(self, nome='', idade=0, profissao=''):
        self.nome = nome
        self.idade = idade
        self.profissao = profissao

    def __str__(self):
        return f'{self.nome}, {self.idade} anos, {self.profissao}'

    @property
    def saudacao(self):
        if self.profissao:
            return f'Olá, sou {self.nome}! Trabalho como {self.profissao}.'
        else:
            return f'Olá, sou {self.nome}!'

    def aniversario(self):
        self.idade += 1

'''Crie uma classe chamada ContaBancaria com um construtor que aceita os parâmetros titular e saldo. Inicie o atributo ativo como False por padrão.

Na classe ContaBancaria, adicione um método especial __str__ que retorna uma mensagem formatada com o titular e o saldo da conta. Crie duas instâncias da classe e imprima essas instâncias.

Adicione um método de classe chamado ativar_conta à classe ContaBancaria que define o atributo ativo como True. Crie uma instância da classe, chame o método de classe e imprima o valor de ativo.

Refatore a classe ContaBancaria para utilizar a abordagem "pythonica" na criação de atributos. Utilize propriedades, se necessário.

Crie uma instância da classe e imprima o valor da propriedade titular.

Crie uma classe chamada ClienteBanco com um construtor que aceita 5 atributos. Instancie 3 objetos desta classe e atribua valores aos seus atributos através do método construtor.

Crie um método de classe para a conta ClienteBanco.'''

# 1) Crie uma classe chamada `ContaBancaria` com um construtor que aceita os parâmetros titular e saldo. Inicie o atributo ativo como False por padrão.
class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo
        self._ativo = False  # Atributo protegido

# 2) Na classe ContaBancaria, adicione um método especial `__str__` que retorna uma mensagem formatada com o titular e o saldo da conta. Crie duas instâncias da classe e imprima essas instâncias.
    def __str__(self):
        return f"Conta de {self.titular} - Saldo: R${self.saldo}"

conta1 = ContaBancaria("João", 1000)
conta2 = ContaBancaria("Maria", 500)

print(conta1)
print(conta2)

# 3) Adicione um método de classe chamado `ativar_conta` à classe `ContaBancaria` que define o atributo ativo como `True`. Crie uma instância da classe, chame o método de classe e imprima o valor de ativo.
@classmethod
def ativar_conta(cls, conta):
    conta._ativo = True

conta3 = ContaBancaria("Carlos", 200)
print(f"Antes de ativar: Conta ativa? {conta3._ativo}")
ContaBancaria.ativar_conta(conta3)
print(f"Depois de ativar: Conta ativa? {conta3._ativo}")

# 4) Refatore a classe `ContaBancaria` para utilizar a abordagem "pythonica" na criação de atributos. Utilize propriedades, se necessário.
class ContaBancariaPythonica:
    def __init__(self, titular, saldo):
        self._titular = titular
        self._saldo = saldo
        self._ativo = False

    @property
    def titular(self):
        return self._titular

    @property
    def saldo(self):
        return self._saldo

    @property
    def ativo(self):
        return self._ativo

# 5) Crie uma instância da classe e imprima o valor da propriedade titular.
conta4 = ContaBancariaPythonica("Fernanda", 1500)
print(f"Titular da conta 4: {conta4.titular}")

# 6) Crie uma classe chamada `ClienteBanco` com um construtor que aceita 5 atributos. Instancie 3 objetos desta classe e atribua valores aos seus atributos através do método construtor.
class ClienteBanco:
    def __init__(self, nome, idade, endereco, cpf, profissao):
        self.nome = nome
        self.idade = idade
        self.endereco = endereco
        self.cpf = cpf
        self.profissao = profissao

cliente1 = ClienteBanco("Ana", 30, "Rua A", "123.456.789-01", "Backend")
cliente2 = ClienteBanco("Luiza", 25, "Rua B", "987.654.321-01", "Estudante")
cliente3 = ClienteBanco("Vinny Neves", 40, "Rua C", "111.222.333-44", "Frontend")

# 7) Crie um método de classe para a conta `ClienteBanco`.
class ClienteBanco:
    # ... (outros métodos e atributos)

    @classmethod
    def criar_conta(cls, titular, saldo_inicial):
        conta = ContaBancariaPythonica(titular, saldo_inicial)
        return conta

# Exemplo de uso do método de classe
conta_cliente1 = ClienteBanco.criar_conta("Ana", 2000)
print(f"Conta de {conta_cliente1.titular} criada com saldo inicial de R${conta_cliente1.saldo}")
'''
Crie uma classe chamada Livro com um construtor que aceita os parâmetros titulo, autor e ano_publicacao. Inicie um atributo chamado disponivel como True por padrão.

Na classe Livro, adicione um método especial str que retorna uma mensagem formatada com o título, autor e ano de publicação do livro. Crie duas instâncias da classe Livro e imprima essas instâncias.

Adicione um método de instância chamado emprestar à classe Livro que define o atributo disponivel como False. Crie uma instância da classe, chame o método emprestar e imprima se o livro está disponível ou não.

Adicione um método estático chamado verificar_disponibilidade à classe Livro que recebe um ano como parâmetro e retorna uma lista dos livros disponíveis publicados nesse ano.

Crie um arquivo chamado biblioteca.py e importe a classe Livro neste arquivo.

No arquivo biblioteca.py, empreste o livro chamando o método emprestar e imprima se o livro está disponível ou não após o empréstimo.

No arquivo biblioteca.py, utilize o método estático verificar_disponibilidade para obter a lista de livros disponíveis publicados em um ano específico.

Crie um arquivo chamado main.py, importe a classe Livro e, no arquivo main.py, instancie dois objetos da classe Livro e exiba a mensagem formatada utilizando o método str.
'''

# 1) Crie uma classe chamada Livro com um construtor que aceita os parâmetros titulo, autor e ano_publicacao. Inicie um atributo chamado disponivel como True por padrão.
class Livro:
    def __init__(self, titulo, autor, ano_publicacao):
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacao = ano_publicacao
        self.disponivel = True

# 2) Na classe Livro, adicione um método especial __str__ que retorna uma mensagem formatada com o título, autor e ano de publicação do livro. Crie duas instâncias da classe Livro e imprima essas instâncias.
    def __str__(self):
        return f"Livro: {self.titulo} | Autor: {self.autor} | Ano de Publicação: {self.ano_publicacao}"

livro1 = Livro("Aprendendo Python", "John Doe", 2022)
livro2 = Livro("Data Science Fundamentals", "Jane Smith", 2020)

print(livro1)
print(livro2)

# 3) Adicione um método de instância chamado emprestar à classe Livro que define o atributo disponivel como False. Crie uma instância da classe, chame o método emprestar e imprima se o livro está disponível ou não.
    def emprestar(self):
        self.disponivel = False

livro3 = Livro("Python Cookbook", "Samuel Developer", 2019)
print(f"Antes de emprestar: Livro disponível? {livro3.disponivel}")
livro3.emprestar()
print(f"Depois de emprestar: Livro disponível? {livro3.disponivel}")

# 4) Adicione um método estático chamado verificar_disponibilidade à classe Livro que recebe um ano como parâmetro e retorna uma lista dos livros disponíveis publicados nesse ano.
    @staticmethod
    def verificar_disponibilidade(ano):
        livros_disponiveis = [livro for livro in Livro.livros if livro.ano_publicacao == ano and livro.disponivel]
        return livros_disponiveis

Livro.livros = [livro1, livro2, livro3]  # Adicionando os livros à lista de livros

# 5) Crie um arquivo chamado biblioteca.py e importe a classe Livro neste arquivo.

# 6) No arquivo biblioteca.py, empreste o livro chamando o método emprestar e imprima se o livro está disponível ou não após o empréstimo.
livro_biblioteca = Livro("Python in Practice", "Emily Coder", 2021)
print(f"Antes de emprestar (biblioteca): Livro disponível? {livro_biblioteca.disponivel}")
livro_biblioteca.emprestar()
print(f"Depois de emprestar (biblioteca): Livro disponível? {livro_biblioteca.disponivel}")

# 7) No arquivo biblioteca.py, utilize o método estático verificar_disponibilidade para obter a lista de livros disponíveis publicados em um ano específico.
ano_especifico = 2020
livros_disponiveis_ano = Livro.verificar_disponibilidade(ano_especifico)
print(f"Livros disponíveis em {ano_especifico}: {livros_disponiveis_ano}")

# 8) Crie um arquivo chamado main.py, importe a classe Livro e, no arquivo main.py, instancie dois objetos da classe Livro e exiba a mensagem formatada utilizando o método __str__.
from minha_classe import Livro  # Certifique-se de corrigir o nome do arquivo para o correto

livro_main1 = Livro("Python para Iniciantes", "Carlos Coder", 2021)
livro_main2 = Livro("Web Development Essentials", "Laura Developer", 2023)

print(livro_main1)
print(livro_main2)
