from model import Cliente, Categoria, Produto, Venda, VendaItem, Avaliacao


class ClienteDAO:
    _clientes = []
    _proximo_id = 1

    @staticmethod
    def listar():
        return ClienteDAO._clientes

    @staticmethod
    def inserir(nome, email, fone, senha):  
        cliente = Cliente(ClienteDAO._proximo_id, nome, email, fone, senha)
        ClienteDAO._clientes.append(cliente)
        ClienteDAO._proximo_id += 1
        return cliente

    @staticmethod
    def buscar_por_id(id):
        for c in ClienteDAO._clientes:
            if c.id == id:
                return c
        return None

    @staticmethod
    def buscar_por_email(email):
        for c in ClienteDAO._clientes:
            if c.email == email:
                return c
        return None

    @staticmethod
    def atualizar(id, nome, email, fone, senha):
        c = ClienteDAO.buscar_por_id(id)
        if c:
            c.nome = nome
            c.email = email
            c.fone = fone
            c.senha = senha

    @staticmethod
    def excluir(id):
        ClienteDAO._clientes = [c for c in ClienteDAO._clientes if c.id != id]


class CategoriaDAO:
    _categorias = []
    _proximo_id = 1

    @staticmethod
    def listar():
        return CategoriaDAO._categorias

    @staticmethod
    def inserir(descricao):
        cat = Categoria(CategoriaDAO._proximo_id, descricao)
        CategoriaDAO._categorias.append(cat)
        CategoriaDAO._proximo_id += 1
        return cat

    @staticmethod
    def buscar_por_id(id):
        for c in CategoriaDAO._categorias:
            if c.id == id:
                return c
        return None

    @staticmethod
    def atualizar(id, descricao):
        c = CategoriaDAO.buscar_por_id(id)
        if c:
            c.descricao = descricao

    @staticmethod
    def excluir(id):
        CategoriaDAO._categorias = [c for c in CategoriaDAO._categorias if c.id != id]


class ProdutoDAO:
    _produtos = []
    _proximo_id = 1

    @staticmethod
    def listar():
        return ProdutoDAO._produtos

    @staticmethod
    def inserir(descricao, preco, estoque, id_categoria):
        p = Produto(ProdutoDAO._proximo_id, descricao, preco, estoque, id_categoria)
        ProdutoDAO._produtos.append(p)
        ProdutoDAO._proximo_id += 1
        return p

    @staticmethod
    def buscar_por_id(id):
        for p in ProdutoDAO._produtos:
            if p.id == id:
                return p
        return None

    @staticmethod
    def atualizar(id, descricao, preco, estoque, id_categoria):
        p = ProdutoDAO.buscar_por_id(id)
        if p:
            p.descricao = descricao
            p.preco = preco
            p.estoque = estoque
            p.id_categoria = id_categoria

    @staticmethod
    def reajustar(percentual):
        for p in ProdutoDAO._produtos:
            p.preco = p.preco * (1 + percentual / 100)

    @staticmethod
    def excluir(id):
        ProdutoDAO._produtos = [p for p in ProdutoDAO._produtos if p.id != id]


class VendaDAO:
    _vendas = []
    _proximo_id = 1

    @staticmethod
    def listar():
        return VendaDAO._vendas

    @staticmethod
    def listar_por_cliente(id_cliente):
        return [v for v in VendaDAO._vendas if v.id_cliente == id_cliente]

    @staticmethod
    def inserir(id_cliente, data):
        v = Venda(VendaDAO._proximo_id, id_cliente, data)
        VendaDAO._vendas.append(v)
        VendaDAO._proximo_id += 1
        return v

    @staticmethod
    def buscar_por_id(id):
        for v in VendaDAO._vendas:
            if v.id == id:
                return v
        return None


class VendaItemDAO:
    @staticmethod
    def inserir(venda, id_produto, descricao_produto, preco_unitario, quantidade):
        item = VendaItem(id_produto, descricao_produto, preco_unitario, quantidade)
        venda.itens.append(item)
        return item


class AvaliacaoDAO:
    """Nova funcionalidade - Tarefa 10"""
    _avaliacoes = []
    _proximo_id = 1

    @staticmethod
    def listar():
        return AvaliacaoDAO._avaliacoes

    @staticmethod
    def listar_por_produto(id_produto):
        return [a for a in AvaliacaoDAO._avaliacoes if a.id_produto == id_produto]

    @staticmethod
    def inserir(id_produto, id_cliente, nota, comentario):
        av = Avaliacao(AvaliacaoDAO._proximo_id, id_produto, id_cliente, nota, comentario)
        AvaliacaoDAO._avaliacoes.append(av)
        AvaliacaoDAO._proximo_id += 1
        return av