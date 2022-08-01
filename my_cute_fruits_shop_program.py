###############################################################################
# Funcoes auxiliares
###############################################################################

def apresenta_menu_de_produtos(produtos):
    print('Escolha o que deseja comprar:')

    for produto in produtos:
        id_produto = produto['id']
        nome_produto = produto['nome']

        print(id_produto, ' - ', nome_produto)

def aguarda_selecao_de_produto(produtos_por_id):
    id_produto = int(
        input('Qual sua escolha?')
    )

    produto = produtos_por_id.get(id_produto)

    if not produto:
        print('Produto inexistente!')
        quit() # encerra o programa se o produto selecionado nao existe

    return produto

def aguarda_numero_de_unidades_a_serem_compradas():
    return int(
        input('Quantas unidades?')
    )

def calcula_total_carrinho_de_compra(produto, n_unidades):
    total_a_pagar = produto['preco_und'] * n_unidades
    return total_a_pagar

def apresenta_resumo_de_compra(produto, n_unidades):
    formato_msg_resumo_compra = 'Você comprou {} {}. Total á pagar: R$ {}'

    total_carrinho = calcula_total_carrinho_de_compra(
        produto, n_unidades
    )

    msg_resumo_compra = formato_msg_resumo_compra.format(
        n_unidades,
        produto['rotulo_resumo_de_compra'],
        total_carrinho,
    )

    print(msg_resumo_compra)

def cria_lista_de_produtos():
    produtos = [
        {
            'id': 1,
            'nome': 'Maçã',
            'preco_und': 2.3,
            'rotulo_resumo_de_compra': 'maça(s)',
        },
        {
            'id': 2,
            'nome': 'Laranja',
            'preco_und': 3.6,
            'rotulo_resumo_de_compra': 'laranja(s)',
        },
        {
            'id': 3,
            'nome': 'Banana',
            'preco_und': 1.85,
            'rotulo_resumo_de_compra': 'banana(s)',
        }
    ]

    return produtos

def cria_dicionario_de_produtos_por_id(produtos):
    produtos_por_id = {}

    for produto in produtos:
        id_produto = produto['id']
        produtos_por_id[id_produto] = produto

    return produtos_por_id


###############################################################################
# Funcao principal
###############################################################################
def my_cute_fruits_shop_program():
    produtos_disponiveis = cria_lista_de_produtos()
    produtos_disponiveis_indexados_por_id = cria_dicionario_de_produtos_por_id(
        produtos_disponiveis
    )

    apresenta_menu_de_produtos(
        produtos_disponiveis
    )

    produto = aguarda_selecao_de_produto(
        produtos_disponiveis_indexados_por_id
    )

    n_unidades = aguarda_numero_de_unidades_a_serem_compradas()

    apresenta_resumo_de_compra(produto, n_unidades)


###############################################################################
# Execucao do programa
###############################################################################
my_cute_fruits_shop_program()