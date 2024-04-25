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

class Camera:
    def __init__(self, nome, filmando=False):
        self.nome = nome
        self.filmando = filmando
    def filmar(self):
        if self.filmando:
            print(f'{self.nome} Já está filmando...')
            return
        print(f'{self.nome} está filmando...')
        self.filmando = True
    def parar_filmar(self):
        if not self.filmando:
            print(f'{self.nome} Não está filmando...')
            return
        print(f'{self.nome} está parando de filmar...')
        self.filmando = False
    def fotografar(self):
        if self.filmando:
            print(f'{self.nome} Não pode fotografar filmando...')
            return
        print(f'{self.nome} está fotografando...')
 

c1 = Camera('Canon')
c2 = Camera('Sony')
c1.filmar()
c1.filmar()
c1.fotografar()
c1.parar_filmar()
c1.fotografar()
print()
c2.filmar()
c2.filmar()
c2.fotografar()
c2.parar_filmar()
c2.fotografar()
# print(c1.filmando, c2.filmando)