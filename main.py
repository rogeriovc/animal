from classe_animal import * 
from views import *

def criar_cao():
    nome = input("nome do cachorro: ")
    tamanho = int(input("tamanho do cachorro em CM: "))
    raca = input("raça do cachorro: ")
    cao = Cachorro(nome,tamanho,raca)
    lista_cao.append(cao)


def criar_humano():
    nome = input("nome do humano: ")
    racional = input("esse humano é racional: ")
    trabalho = input("Qual é o seu trabalho: ")
    cpf = str(input("qual é seu cpf: "))
    altura = float(input("qual é a altura desse humano: "))
    humano = Humano(nome,racional,trabalho,cpf,altura)
    lista_humano.append(humano)

def  listar(lista): 
        for objeto in lista:
            print(objeto.info())
    

lista_cao = []
lista_humano = []

while True:
    menu_inicial()
    op = int(input("digite a opção do menu: "))
    if op == 1:
        criar_cao()         
         
    if op == 2:
        criar_humano()
        
    if op == 3:
        listar(lista_cao)

    if op == 4:
        listar(lista_humano)
           