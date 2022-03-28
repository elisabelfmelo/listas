import tkinter as tk 

def adicionar_elemento(lista: list, elemento: str) -> bool:
    '''
    Verifica se o elemento começa com letra maiúscula
    Se ele passar na verificação, inserir na lista e retornar
    verdadeiro, caso contrário, retorne falso
    '''
    x = elemento[0]
    if (x == x.upper()):
        lista.append(elemento)
        return True
    else:
        return False
    

def buscar_elemento(lista: list, elemento: str) -> bool:
    '''
    Verifica se um elemento está contido na lista.
    Se estiver, retorne verdadeiro, caso contrário, retorne falso.
    '''
    x=(elemento)
    if x in lista:
     return True
    if x not in lista:
        return False


def remover_elemento(lista: list, elemento: str) -> bool:
    '''
    Verifica se a lista contém um elemento específico.
    Se ele estiver contido na lista, remover o elemento e
    retornar verdadeiro, caso contrário, retornar falso.
    '''
    for x in lista:
     if x  in lista:
      lista.remove(x)
      return lista
      return True
    else:
      return False



def limpar_lista(lista: list) -> None:
    '''
    Remove todos os elementos da lista.
    Função sem retorno.
    '''
    lista.clear()


def ordenar_lista(lista:list) -> None:
    '''
    Ordena todos os elementos da lista por ordem
    alfabética. A função não possui retorno
    '''
    for x in lista:
     lista.sort(reverse=False)


def pegar_quantidade(lista: list) -> int:
    '''
    Retorna a quantidade de elementos dentro
    da lista
    '''
    for x in lista:
     return len(lista)


def converter_maiusculo(lista: list) -> list:
    '''
    Converte todos os elementos da lista para letra
    maiúscula e os retorna em uma nova lista
    '''
    list2=[]
    for x in lista:
     if x in lista:
      a=x.upper()
     if x not in list2:
         list2.append(a)
    return list2

def eliminar_repetidos(lista: list) -> list:
    '''
    DESAFIO: 0.5 extra
    Remove todos os elementos repetidos na lista
    e retorna uma lista nova (não vale utilizar o set)
    '''
    list2=[]
    for x in lista:
     if x not in list2:
      list2.append(x)
      list2.sort()
    return list2
        
    
