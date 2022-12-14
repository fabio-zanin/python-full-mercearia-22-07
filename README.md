# Mercearia ![Badge em Desenvolvimento](http://img.shields.io/static/v1?label=STATUS&message=EM%20DESENVOLVIMENTO&color=GREEN&style=for-the-badge)

![GitHub Workflow Status](https://img.shields.io/github/workflow/status/dwyl/auth_plug/Elixir%20CI?label=build&style=flat-square)

## Sobre 

Projeto para gerenciamento de mercearia baseado em Python 3.

Projeto desenvolvido com a realização do curso Python Full, em Python 3.8.10 no Linux Mint XFCE 20.3 Una na IDE Visual Studio Code 1.69.2.

## Implementações

- Cadastro de Categoria, Produtos, Estoque, Venda, Fonercedor, Pessoa, e Funcionario em arquivos de texto, utilizando arquitetura MVC.

## Tecnologias utilizadas

- [Python](https://www.python.org/downloads/) - Versão 3.8+

## Autor
- Fabio Zanin
- e-mail: [f481011@gmail.com](f481011@gmail.com)

## Ajuda

Para relatar bugs ou fazer perguntas utilize o [Issues](https://github.com/fabio-zanin/python-full-mercearia-22-07/issues) ou via e-mail [f481011@gmail.com](f481011@gmail.com)


## Aulas

### Projeto prático 1 | Software para gerenciamento de mercearia

<table border="1" class="dataframe">
  <tbody>
    <tr>
    <th>00</th>
    <td>
        <p align="top"><b>Demonstração do projeto | AO VIVO</b></p>
    </td> 
    </tr>
    <tr>
    <th>01</th>
    <td>
        <p align="top"><b>Aula: Criação da Model</b></p>
        <p align="justify">Criação da Model.py e das classes:</p>
        <ul>
            <li>class Categoria</li>
            <li>class Produtos</li>
            <li>class Estoque</li>
            <li>class Venda</li>
            <li>class Fonercedor</li>
            <li>class Pessoa</li>
            <li>class Funcionario</li>
        </ul>
    </td> 
    </tr>
    <tr>
    <th>02</th>
    <td>
        <p align="top"><b>Aula: Criação da DAO #1</b></p>
        <p align="justify">Criação da DAO.py </p>
        <ul>
            <li>DaoCategoria e DaoVenda</li>
            <li>métodos: salvar e ler</li>
        </ul>
    </td> 
    </tr>
        </tr>
    <tr>
    <th>03</th>
    <td>
        <p align="top"><b>Aula: DAO #2</b></p>
        <p align="justify">Atualização da DAO.py </p>
        <ul>
            <li>DaoEstoque, DaoFornecedor, DaoPessoa, e DaoFuncionario</li>
            <li>métodos: salvar e ler</li>
        </ul>
    </td> 
    </tr>
    <tr>
    <th>04</th>
    <td>
        <p align="top"><b>Aula: Controller categoria #1 | Cadastrar categoria</b></p>
        <p align="justify">Criação Controller.py </p>
        <ul>
            <li>Função cadastrar categoria.</li>
        </ul>
    </td> 
    </tr>
    <tr>
    <th>05</th>
    <td>
        <p align="top"><b>Aula: Controller categoria #2 | Remover categoria</b></p>
        <p align="justify">Atualização Controller.py </p>
        <ul>
            <li>Função remover categoria.</li>
        </ul>
    </td> 
    </tr>
    </tr>
    <tr>
    <th>06</th>
    <td>
        <p align="top"><b>Aula: Controller categoria #3 | Alterar categoria</b></p>
        <p align="justify">Atualização Controller.py </p>
        <ul>
            <li>Função alterar categoria.</li>
        </ul>
    </td> 
    </tr>
    <tr>
    <th>07</th>
    <td>
        <p align="top"><b>Aula: Controller categoria #4 | Mostrar categoria</b></p>
        <p align="justify">Atualização Controller.py </p>
        <ul>
            <li>Função mostrar categoria.</li>
        </ul>
    </td> 
    </tr>
    </tr>
    <tr>
    <th>08</th>
    <td>
        <p align="top"><b>Aula: Controller estoque #1 | Cadastro de produto</b></p>
        <p align="justify">Atualização Controller.py </p>
        <ul>
            <li>Função cadastro de produtos.</li>
        </ul>
    </td> 
    </tr>
    <tr>
    <th>09</th>
    <td>
        <p align="top"><b>Aula: Controller estoque #2 | Remover produto</b></p>
        <p align="justify">Atualização Controller.py </p>
        <ul>
            <li>Função remover produto.</li>
        </ul>
    </td> 
    </tr>
    <tr>
    <th>10</th>
    <td>
        <p align="top"><b>Aula: Controller estoque #3 | Alterar produto</b></p>
        <p align="justify">Atualização Controller.py </p>
        <ul>
            <li>Função alterar produto.</li>
        </ul>
    </td> 
    </tr>
    <tr>
    <th>11</th>
    <td>
        <p align="top"><b>Aula: Controller estoque #4 | Mostrar estoque</b></p>
        <p align="justify">Atualização Controller.py </p>
        <ul>
            <li>Função mostrar produto.</li>
        </ul>
    </td> 
    </tr>
    <tr>
    <th>12</th>
    <td>
        <p align="top"><b>Aula: Controller venda #1 | Efetuar venda</b></p>
        <p align="justify">Atualização Controller.py </p>
        <ul>
            <li>Função efetuar venda.</li>
        </ul>
    </td> 
    </tr>
    <tr>
    <th>13</th>
    <td>
        <p align="top"><b>Aula: Controller venda #2 | Relatórios de produtos</b></p>
        <p align="justify">Atualização Controller.py </p>
        <ul>
            <li>Função relatórios de produtos.</li>
        </ul>
    </td> 
    </tr>
    <tr>
    <th>12</th>
    <td>
        <p align="top"><b>Aula: Controller venda #1 | Efetuar venda</b></p>
        <p align="justify">Atualização Controller.py </p>
        <ul>
            <li>Função efetuar venda.</li>
        </ul>
    </td> 
    </tr>
    <tr>
    <th>14</th>
    <td>
        <p align="top"><b>Aula: Controller Venda #4 | mostrar vendas</b></p>
        <p align="justify">Atualização Controller.py </p>
        <ul>
            <li>Função mostrar vendas.</li>
        </ul>
    </td> 
    </tr>
    <tr>
    <tr>
    <th>15 - 17</th>
    <td>
        <p align="top"><b>Aula: Controller gerais</b></p>
        <p align="justify">Atualização Controller.py</p>
        <ul>
            <li>funções fornecedor</li>
            <li>funções cliente</li>
            <li>funções funcionario</li>
        </ul>
    </td> 
    </tr>
    <tr>
    <tr>
    <th>15</th>
    <td>
        <p align="top"><b>funções fornecedor</b></p>
        <p align="justify">Atualização Controller.py</p>
        <ul>
            <li>Função cadastrar fornecedor</li>
            <li>Função remover fornecedor</li>
            <li>Função lterar fornecedor</li>
            <li>Função mostrar fornecedor</li>
        </ul>
    </td> 
    </tr>
    <th>16</th>
    <td>
        <p align="top"><b>funções cliente</b></p>
        <p align="justify">Atualização Controller.py</p>
        <ul>
            <li>Função cadastrar cliente</li>
            <li>Função remover cliente</li>
            <li>Função lterar cliente</li>
            <li>Função mostrar cliente</li>
        </ul>
    </td> 
    </tr>
        <tr>
    <th>17</th>
    <td>
        <p align="top"><b>funções funcionario</b></p>
        <p align="justify">Atualização Controller.py</p>
        <ul>
            <li>Função cadastrar funcionário</li>
            <li>Função remover funcionário</li>
            <li>Função lterar funcionário</li>
            <li>Função mostrar funcionário</li>
        </ul>
    </td> 
    </tr>
    <tr>
    <th>18</th>
    <td>
        <p align="top"><b>Controller categoria #5 | Terminando TODO</b></p>
        <p align="top"><b>Controller categoria #6 | Terminando TODO</b></p>
        <p align="justify">Atualização Controller.py</p>
        <ul>
            <li>Função colacar sem categoria no estoque</li>
            <li>Função aleterar a categoria do estoque</li>
        </ul>
    </td> 
    </tr>
</tbody>
</table>