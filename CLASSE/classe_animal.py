class Animal():
    nome=str
    coracao:bool
    racional=bool
    cor= str
    raca= str
    idade= int
    def __init__(self,nome,coracao):
        self.nome = nome
        self.coracao = coracao
    
    def info(self):
        return{'nome': self.nome}
    
    def andar(self):
        print("-------------andando...")

class Humano(Animal):
    nome = str
    racional=True
    trabalho = str
    cpf = str
    altura = float
   

    def __init__(self,nome,racional,trabalho,cpf,altura):
        self.nome = nome
        self.racional = racional
        self.trabalho = trabalho
        self.cpf = cpf
        self.altura = altura

    def adicionar_humano(self, humano):
        self.humanos.append(humano)


class Cachorro(Animal):
    tamanho = 0
    raca=''
   
    
    def __init__(self,nome,tamanho,raca):
        self.nome = nome
        self.tamanho = tamanho
        self.raca = raca
        self.coracao=True
        self.racional=False


    def listar_caos(self): 
        for cao in self.caos:
            print(f'{cao.nome}')

    def buscar_cao(self, nome):
        for cao in self.caos:
            if cao.nome == nome:
                return cao
        return None

    def latir(self):
        print('------------ au-au-au!!')


