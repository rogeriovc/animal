from classe_animal import * 
from views import *

def criar_cao():
    nome = input("nome do cachorro:---- ")
    tamanho = int(input("tamanho do cachorro em CM:---- "))
    raca = input("raça do cachorro:---- ")
    cao = Cachorro(nome,tamanho,raca)
    lista_cao.append(cao)


def criar_humano():
    nome = input("nome do humano:---- ")
    racional = input("esse humano é racional:---- ")
    trabalho = input("Qual é o seu trabalho:---- ")
    cpf = str(input("qual é seu cpf:---- "))
    altura = float(input("qual é a altura desse humano:---- "))
    humano = Humano(nome,racional,trabalho,cpf,altura)
    lista_humano.append(humano)

def informacoes_cao(cao):
    print(cao.nome)
    print(cao.tamanho)
    print(cao.raca)

def info_humano(humano):
    print(humano.nome)
    print(humano.racional)
    print(humano.trabalho)
    print(humano.cpf)
    print(humano.altura)

   

def  listar(lista:list): 
        if len(lista) > 0:
            for objeto in lista:
                print(objeto.info())
        else:
            print("lista vazia")

def enumerar_cao():
    for index in range(0,len(lista_cao)):
        print(index)
           

lista_cao = []
lista_humano = []

while True:
    menu_inicial()
    op = int(input("digite a opção do menu principal: "))
    if op == 1:
        criar_cao()        
         
    if op == 2:
        criar_humano()
        
    if op == 3:
        enumerar_cao()
        listar(lista_cao)
        
    if op == 4:
        listar(lista_humano)

    if op == 5:
        print("saiu")
        break


    sub_menu()
    op1 =  int(input("digite a opção do sub menu:"))
    if op1 == 1:
        humano = lista_humano[0]
        humano.andar()

    if op1 == 2:
        cao = lista_cao[0]
        cao.latir()
    
    if op1 == 3:
         for cao in lista_cao:
            print(informacoes_cao(cao))

    if op1 == 4:
        for humano in lista_humano:
            print(info_humano(humano))

    if op1 == 5:
        menu_inicial()
    
    if op1 == 6:
        print("saiu")
        break



    
    

           