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

# a = ControllerCategoria()
# a.cadastraCategoria('Frios')

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
