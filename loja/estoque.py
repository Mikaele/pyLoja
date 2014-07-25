#coding: utf-8


class Estoque():
    def __int__(self):
        pass

    def adicionar(self, nome, quant, preco):
        self.gravar_em_csv(nome.lower().capitalize(), self.check_type(int, quant), self.check_type(float, preco))
    #     with open("estoque.csv", "a") as estoque:
    #        estoque.write(', '.join([str(item) for item in [nome, quant, preco]]) + '\n')
    #        print "Produto armazenado com sucesso"

    def ler(self):
        with open("estoque.csv", "r") as estoque:
            for item in enumerate(estoque):
                print item
#            print estoque.read()


    def gravar_em_csv(self, nome, quant, preco):
        with open("estoque.csv", "a") as estoque:
            estoque.write(', '.join([str(item) for item in [nome, quant, preco]]) + '\n')
            print "Produto armazenado com sucesso"

    def check_type(self, tipo, valor):
        try:
            return tipo(valor)
        except:
            print "Tipo  %s não permitido" % valor
            return 0
#
#    def ler_de_csv(self):
#         with open("estoque.csv", "r") as estoque:
#            print enumerate(estoque)