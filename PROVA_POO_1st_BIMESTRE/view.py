from datetime import datetime
from dao import ClienteDAO, CategoriaDAO, ProdutoDAO, VendaDAO, VendaItemDAO, AvaliacaoDAO


class View:

    @staticmethod
    def Cliente_Listar():
        return ClienteDAO.listar()

    @staticmethod
    def Cliente_Inserir(nome, email, fone, senha):
        if ClienteDAO.buscar_por_email(email):
            raise ValueError("Email já cadastrado.")
        ClienteDAO.inserir(nome, email, fone, senha)

    @staticmethod
    def Cliente_Atualizar(id, nome, email, fone, senha):
        if not ClienteDAO.buscar_por_id(id):
            raise ValueError("Cliente não encontrado.")
        ClienteDAO.atualizar(id, nome, email, fone, senha)

    @staticmethod
    def Cliente_Excluir(id):
        if not ClienteDAO.buscar_por_id(id):
            raise ValueError("Cliente não encontrado.")
        ClienteDAO.excluir(id)

    @staticmethod
    def Categoria_Listar():
        return CategoriaDAO.listar()

    @staticmethod
    def Categoria_Inserir(descricao):
        if not descricao.strip():
            raise ValueError("Descrição não pode ser vazia.")
        CategoriaDAO.inserir(descricao)

    @staticmethod
    def Categoria_Atualizar(id, descricao):
        if not CategoriaDAO.buscar_por_id(id):
            raise ValueError("Categoria não encontrada.")
        CategoriaDAO.atualizar(id, descricao)

    @staticmethod
    def Categoria_Excluir(id):
        if not CategoriaDAO.buscar_por_id(id):
            raise ValueError("Categoria não encontrada.")
        CategoriaDAO.excluir(id)

    @staticmethod
    def Produto_Listar():
        return ProdutoDAO.listar()

    @staticmethod
    def Produto_Inserir(descricao, preco, estoque, id_categoria):
        if not CategoriaDAO.buscar_por_id(id_categoria):
            raise ValueError("Categoria não encontrada.")
        if preco < 0 or estoque < 0:
            raise ValueError("Preço e estoque devem ser não negativos.")
        ProdutoDAO.inserir(descricao, preco, estoque, id_categoria)

    @staticmethod
    def Produto_Atualizar(id, descricao, preco, estoque, id_categoria):
        if not ProdutoDAO.buscar_por_id(id):
            raise ValueError("Produto não encontrado.")
        ProdutoDAO.atualizar(id, descricao, preco, estoque, id_categoria)

    @staticmethod
    def Produto_Excluir(id):
        if not ProdutoDAO.buscar_por_id(id):
            raise ValueError("Produto não encontrado.")
        ProdutoDAO.excluir(id)

    @staticmethod
    def Produto_Reajustar(percentual):
        ProdutoDAO.reajustar(percentual)

    @staticmethod
    def Carrinho_Inserir(carrinho, id_produto, quantidade):
        produto = ProdutoDAO.buscar_por_id(id_produto)
        if not produto:
            raise ValueError("Produto não encontrado.")
        if quantidade <= 0:
            raise ValueError("Quantidade deve ser maior que zero.")
        if quantidade > produto.estoque:
            raise ValueError(f"Estoque insuficiente. Disponível: {produto.estoque}")

        for item in carrinho:
            if item["id_produto"] == id_produto:
                nova_qtd = item["quantidade"] + quantidade
                if nova_qtd > produto.estoque:
                    raise ValueError(f"Estoque insuficiente. Disponível: {produto.estoque}")
                item["quantidade"] = nova_qtd
                return

        carrinho.append({
            "id_produto": produto.id,
            "descricao": produto.descricao,
            "preco": produto.preco,
            "quantidade": quantidade
        })

    @staticmethod
    def Carrinho_Visualizar(carrinho):
        return carrinho

    @staticmethod
    def Carrinho_Comprar(carrinho, id_cliente):
        if not carrinho:
            raise ValueError("Carrinho está vazio.")

        data = datetime.now().strftime("%d/%m/%Y %H:%M")
        venda = VendaDAO.inserir(id_cliente, data)

        for item in carrinho:
            produto = ProdutoDAO.buscar_por_id(item["id_produto"])
            if produto.estoque < item["quantidade"]:
                raise ValueError(f"Estoque insuficiente para '{produto.descricao}'.")
            produto.estoque -= item["quantidade"]
            VendaItemDAO.inserir(venda, produto.id, produto.descricao, item["preco"], item["quantidade"])

        carrinho.clear()
        return venda

    @staticmethod
    def Vendas_ListarPorCliente(id_cliente):
        return VendaDAO.listar_por_cliente(id_cliente)

    @staticmethod
    def Vendas_ListarTodas():
        return VendaDAO.listar()


    @staticmethod
    def Login(email, senha, admin_senha):
        if email == "admin@sistema.com" and senha == admin_senha:
            return "admin", None

        cliente = ClienteDAO.buscar_por_email(email)
        if cliente and cliente.senha == senha:
            return "cliente", cliente

        raise ValueError("Email ou senha inválidos.")


    @staticmethod
    def Avaliacao_Inserir(id_produto, id_cliente, nota, comentario):
        if not ProdutoDAO.buscar_por_id(id_produto):
            raise ValueError("Produto não encontrado.")
        if nota < 1 or nota > 5:
            raise ValueError("Nota deve ser entre 1 e 5.")
        AvaliacaoDAO.inserir(id_produto, id_cliente, nota, comentario)

    @staticmethod
    def Avaliacao_ListarPorProduto(id_produto):
        return AvaliacaoDAO.listar_por_produto(id_produto)