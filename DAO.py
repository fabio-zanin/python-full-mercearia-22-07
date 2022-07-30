from Model import *


class DaoCategoria:
    @classmethod
    def salvar(cls, categoria):
        with open('categoria.txt', 'a') as arq:
            arq.writelines(categoria)
            arq.writelines('\n')
    
    @classmethod
    def ler(cls):
        with open('categoria.txt', 'r') as arq:
            cls.categoria = arq.readlines()
        cls.categoria = list(map(lambda x: x.replace('\n', ''), cls.categoria))
        cat = []
        for i in cls.categoria:
            cat.append(Categoria(i))
        return cat
#         print(cls.categoria)
# DaoCategoria.salvar('Frutas')
# DaoCategoria.salvar('Verduras')
# DaoCategoria.salvar('Legumes')
# DaoCategoria.ler()


class DaoVenda:
    @classmethod
    def salvar(cls, venda:Venda):
        with open('vendas.txt', 'a') as arq:
            arq.writelines(venda.itensVendido.nome + "|" + venda.itensVendido.preco + "|" + 
                            venda.itensVendido.categoria + "|" + venda.vendedor + "|" + 
                            venda.comprador + "|" + str(venda.quantidadeVendida) + "|" + venda.data)
            arq.writelines('\n')
    
    @classmethod
    def ler(cls):
        with open('vendas.txt', 'r') as arq:
            cls.venda = arq.readlines()
        cls.venda = list(map(lambda x: x.replace('\n', ''), cls.venda))
        cls.venda = list(map(lambda x: x.split('|'), cls.venda))
        vend = []
        for i in cls.venda:
            vend.append(Venda(Produtos(i[0], i[1], i[2]), i[3], i[4], i[5], i[6]))
        return vend

        # print(cls.venda)
# x = Produtos('banana', '5', 'frutas')
# y = Venda(x, 'caio', 'marcos', '3')
# DaoVenda.salvar(y)
# DaoVenda.ler()
x = DaoVenda.ler()
# print(x)
print(x[0].comprador)
print(x[1].itensVendido.nome)

