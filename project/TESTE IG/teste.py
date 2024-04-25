# class pessoas:
#     def __init__(self, nome, sobrenome):
#         self.nome = nome
#         self.sobrenome = sobrenome

# p1 = pessoas('Geovani', 'Cordeiro')
# # p1.name = 'Geovani'
# # p1.sobrenome = 'Cordeiro'
# p2 = pessoas('Michael', 'Jackson')
# # p2.name = 'Michael'
# # p2.sobrenome = 'Jackson'

# print (p1.nome, p1.sobrenome, p2.nome, p2.sobrenome)

# Método em instância de classes Python
# Classe - Molde (geralmente sem dados)
# Instância da class (objeto) - Tem os dados
# Uma classe pode gerar várias instâncias
# Na classe o self é a prória instẫncias

# class Carro:
#     def __init__(self, nome):
#         self.nome = nome
#     def acelerar(self):
#         print(f'{self.nome} está acelerando...')

# fusca = Carro('Fusca')
# print(fusca.nome)
# fusca.acelerar()
# celta = Carro('Celta')
# print(celta.nome)
# celta.acelerar()

# class Camera:
#     def __init__(self, nome, filmando=False):
#         self.nome = nome
#         self.filmando = filmando
#     def filmar(self):
#         if self.filmando:
#             print(f'{self.nome} Já está filmando...')
#             return
#         print(f'{self.nome} está filmando...')
#         self.filmando = True
#     def parar_filmar(self):
#         if not self.filmando:
#             print(f'{self.nome} Não está filmando...')
#             return
#         print(f'{self.nome} está parando de filmar...')
#         self.filmando = False
#     def fotografar(self):
#         if self.filmando:
#             print(f'{self.nome} Não pode fotografar filmando...')
#             return
#         print(f'{self.nome} está fotografando...')
 

# c1 = Camera('Canon')
# c2 = Camera('Sony')
# c1.filmar()
# c1.filmar()
# c1.fotografar()
# c1.parar_filmar()
# c1.fotografar()
# print()
# c2.filmar()
# c2.filmar()
# c2.fotografar()
# c2.parar_filmar()
# c2.fotografar()

# Atributos de classe
# class Pessoa:
#     ano_atual = 2024
#     def __init__(self, nome, idade):
#         self.nome = nome
#         self.idade = idade
#     def get_ano_nacimento(self):
#         return Pessoa.ano_atual - self.idade

# p1 = Pessoa('João', 35)
# p2 = Pessoa('Helena', 12)
# print(Pessoa.ano_atual)
# print(p1.get_ano_nacimento())
# print(p2.get_ano_nacimento())

# # __dict__ e vars para atributos de instância
# class Pessoa:
#     ano_atual = 2024
#     def __init__(self, nome, idade):
#         self.nome = nome
#         self.idade = idade
#     def get_ano_nacimento(self):
#         return Pessoa.ano_atual - self.idade

# dados = {'nome': 'Geovani', 'idade': 28}    
# p1 = Pessoa(**dados)
# print(vars(p1))
# print(p1.nome)

# Aula 127_A
# Exercício - Salve sua classe em JSON
# Salve os dados da sua classe em JSON
# e depois crie novamente as instâncias
# da classe com os dados salvos
# Faça em arquivos separados.

# #import json
# CAMINHO_ARQUIVO = 'aula127.json'

# class Pessoa:
#     def __init__(self, nome, idade):
#         self.nome = nome
#         self.idade = idade
# p1 = Pessoa('Geovani', 28)
# p2 = Pessoa('Elias', 28)
# p3 = Pessoa('Yago', 22)
# bd = [vars(p1), p2.__dict__, vars(p3)]
# # with open(CAMINHO_ARQUIVO, 'w') as arquivo:
# #     Json.dump(db, arquivo, ensure_ascii=False, indent=2)