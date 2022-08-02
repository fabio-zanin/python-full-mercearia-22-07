from datetime import datetime

from DAO import *
from Model import *


class ControllerCategoria:
    def cadastraCategoria(self, novaCategoria):
        existe = False
        x = DaoCategoria.ler()
        for i in x:
            if i.categoria == novaCategoria:
                existe = True
        if not existe:
                DaoCategoria.salvar(novaCategoria)
                print('Categoria cadastrada com sucesso.')
        else:
                print('Categoria que deseja cadastrar já existe.')

    def removerCategoria(self, excluirCategoria):
        x = DaoCategoria.ler()
        cat = list(filter(lambda x: x.categoria == excluirCategoria, x))
        if len(cat) <= 0:
            print('A categoria que deseja remover não existe')
        else:
            for i in range(len(x)):
                if x[i].categoria == excluirCategoria:
                    del x[i]
                    break
            print('Categoria removiad com sucesso')

            with open('categoria.txt', 'w') as arq:
                for i in x:
                    arq.writelines(i.categoria)
                    arq.writelines('\n')

    def alterarCategoria(self, categoriaAlterar, categoriaAlterada):
        x = DaoCategoria.ler()
        cat = list(filter(lambda x : x.categoria == categoriaAlterar, x))
        if len(cat) > 0:
            cat1 = list(filter(lambda x : x.categoria == categoriaAlterada, x))
            if len(cat1) == 0:
                x = list(map(lambda x : Categoria(categoriaAlterada) if(x.categoria == categoriaAlterar) else(x), x))
                print('A alteração foi efetuada com sucesso.')
            else:
                print('A categoria para qual deseja alterar já existe')
        else:
            print('A categoria que deseja alterar não existe.')
        with open('categoria.txt', 'w') as arq:
            for i in x:
                arq.writelines(i.categoria)
                arq.writelines('\n')

# Cadastrar Categoria
# a = ControllerCategoria()
# a.cadastraCategoria('Frios')

# Remover Categoria
# a = ControllerCategoria()
# a.removerCategoria('Frios')

# Alterar Categoria
# a = ControllerCategoria()
# a.alterarCategoria('Carnes', 'Verduras')
