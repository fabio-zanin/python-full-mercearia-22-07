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
            print('Categoria removida com sucesso')
        # TODO: Colacar sem categoria no estoque
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
        # TODO: Aleterar a categoria do estoque
            else:
                print('A categoria para qual deseja alterar já existe')
        else:
            print('A categoria que deseja alterar não existe.')
        with open('categoria.txt', 'w') as arq:
            for i in x:
                arq.writelines(i.categoria)
                arq.writelines('\n')

    def mostrarCategoria(self):
        categorias = DaoCategoria.ler()
        if len(categorias) == 0:
            print('Categoria vazia')
        else:
            for i in categorias:
                print(f'Categoria: {i.categoria}')

# Cadastrar Categoria
# a = ControllerCategoria()
# a.cadastraCategoria('Frutas')

# Remover Categoria
# a = ControllerCategoria()
# a.removerCategoria('Frios')

# Alterar Categoria
# a = ControllerCategoria()
# a.alterarCategoria('Carnes', 'Verduras')

# Maostrar Categoria
# a = ControllerCategoria()
# a.mostrarCategoria()


class ControllerEstoque:
    def cadastrarProduto(self, nome, preco, categoria, quantidade):
        x = DaoEstoque.ler()
        y = DaoCategoria.ler()
        h = list(filter(lambda x : x.categoria == categoria, y))
        est = list(filter(lambda x : x.produto.nome == nome, x))
        if len(h) > 0:
            if len(est) == 0:
                produto = Produtos(nome, preco, categoria)
                DaoEstoque.salvar(produto, quantidade)
                print('Produto cadastrado com sucesso.')
            else:
                print('Produto já exsite em estoque.')
        else:
            print('Categoria inexistente.')
    
    def removerProduto(self, nome):
        x = DaoEstoque.ler()
        est = list(filter(lambda x : x.produto.nome == nome, x))
        if len(est) > 0:
            for i in range(len(x)):
                if x[i].produto.nome == nome:
                    del x[i]
                    break
            print('Produto removido com sucesso.')
        else:
            print('O produto que deseja remover não existe.')
        with open('estoque.txt', 'w') as arq:
            for i in x:
                arq.writelines(i.produto.nome + "|" + i.produto.preco + "|" +
                            i.produto.categoria + "|" + str(i.quantidade))
                arq.writelines('\n')

    def alterarProduto(self, nomeAlterar, novoNome, novoPreco, novaCategoria, novaQuantidade):
        x = DaoEstoque.ler()
        y = DaoCategoria.ler()
        h = list(filter(lambda x : x.categoria == novaCategoria, y))
        if len(h) > 0:
            est = list(filter(lambda x : x.produto.nome == nomeAlterar, x))
            if len(est) > 0:
                est = list(filter(lambda x : x.produto.nome == novoNome, x))
                if len(est) == 0:
                    x = list(map(lambda x : Estoque(Produtos(novoNome, novoPreco, novaCategoria), novaQuantidade) if(x.produto.nome == nomeAlterar) else(x), x))
                    print('Produto alterado com sucesso.')
                else:
                    print('Produto já cadastrado.')
            else:
                print('O produto que deseja alterar não existe.')
        else:
            print('A categoria informada não existe.')
        with open('estoque.txt', 'w') as arq:
            for i in x:
                arq.writelines(i.produto.nome + "|" + i.produto.preco + "|" +
                            i.produto.categoria + "|" + str(i.quantidade))
                arq.writelines('\n')
    
    def mostrarProduto(self):
        estoque = DaoEstoque.ler()
        if len(estoque) == 0:
            print('Estoque vazio.')
        else:
            print('======Produtos======')
            for i in estoque:                
                print(f'Nome: {i.produto.nome}\n'
                      f'Preço: {i.produto.preco}\n'
                      f'Categoria: {i.produto.categoria}\n'
                      f'Qauntidade: {i.quantidade}'
                )
                print('--------------------')


# Cadastrar Produtos
# a = ControllerEstoque()
# a.cadastrarProduto('abacaxi', '2', 'Frutas', 20)

# Remover Produto
# a = ControllerEstoque()
# a.removerProduto('banana')

# Alterar Produto
# a = ControllerEstoque()
# a.alterarProduto('banana', 'maca', '5', 'Verduras', '20')

# Mostrar Produto
# a = ControllerEstoque()
# a.mostrarProduto()


class ControllerVenda:

    def cadastrarVenda(self, nomeProduto, vendedor, comprador, quantidadeVendida):
        x = DaoEstoque.ler()
        temp = []
        existe = False
        quantidade = False

        for i in x:
            if existe == False:
                if i.produto.nome == nomeProduto:
                    existe = True
                    if i.quantidade >= quantidadeVendida:
                        quantidade = True
                        i.quantidade = int(i.quantidade) - int(quantidadeVendida)
                        vendido = Venda(Produtos(i.produto.nome, i.produto.preco, i.produto.categoria), vendedor, comprador, quantidadeVendida)
                        valorCompra = int(quantidadeVendida) * int(i.produto.preco)
                        DaoVenda.salvar(vendido)
            temp.append(Estoque(Produtos(i.produto.nome, i.produto.preco, i.produto.categoria), i.quantidade))
        arq = open('estoque.txt', 'w')
        arq.write('')

        for i in temp:
            with open('estoque.txt', 'a') as arq:                
                arq.writelines(i.produto.nome + "|" + i.produto.preco + "|" + i.produto.categoria + "|" + str(i.quantidade))
                arq.writelines('\n')
        if existe == False:
            print('O produto não existe.')
            return None
        elif not quantidade:
            print('A quantidade vendida não contem em estoque.')
            return None
        else:
            print('Venda realizada com sucesso.')
            return valorCompra
        
    def relatorioProdutos(self):
        vendas = DaoVenda.ler()
        produtos = []
        for i in vendas:
            nome = i.itensVendido.nome
            quantidade = i.quantidadeVendida
            tamanho = list(filter(lambda x: x['produto'] == nome, produtos))            
            if len(tamanho) > 0:
                produtos = list(map(lambda x: {'produto': nome, 'quantidade': int(x['quantidade']) + int(quantidade)}
                if (x['produto'] == nome) else (x), produtos))                
            else:
                produtos.append({'produto': nome, 'quantidade': int(quantidade)})

        ordenado = sorted(produtos, key=lambda k : k['quantidade'], reverse=True)
        print('Esses saos os produtos mais vendidos')
        a = 1
        for i in ordenado:
            print(f'==========Produto [{a}]==========')
            print(f"Produto: {i['produto']}\n"
                    f"Quantidade: {i['quantidade']}\n")
            a += 1

            

# Cadastrar Venda
# a = ControllerVenda()
# a.cadastrarVenda('abacaxi', 'joão', 'caio', 1)
# a.cadastrarVenda('laranja', 'joão', 'caio', 200)
# a.cadastrarVenda('maca', 'joão', 'caio', 2)

# Relatorio
a = ControllerVenda()
a.relatorioProdutos()
