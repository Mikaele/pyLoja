#coding: utf-8

from loja.estoque import Estoque
import sys
''' Lê do terminal'''
argumentos = sys.argv[1:]
estoque = Estoque()

comandos = {
    '-add': estoque.adicionar,
     '-readcsv': estoque.ler
}

if argumentos[0] not in comandos:
    raise KeyError("Comando não reconhecido")
elif argumentos[0] in comandos:
    comandos[argumentos[0]](*argumentos[1:])


#for argumento in argumentos:
 #   print argumento

