class Cliente:
    def __init__(self, id, nome, email, fone, senha):
        self.id = id
        self.nome = nome
        self.email = email
        self.fone = fone
        self.senha = senha

    def __str__(self):
        return f"[{self.id}] {self.nome} | {self.email} | {self.fone}"


class Categoria:
    def __init__(self, id, descricao):
        self.id = id
        self.descricao = descricao

    def __str__(self):
        return f"[{self.id}] {self.descricao}"


class Produto:
    def __init__(self, id, descricao, preco, estoque, id_categoria):
        self.id = id
        self.descricao = descricao
        self.preco = preco
        self.estoque = estoque
        self.id_categoria = id_categoria

    def __str__(self):
        return f"[{self.id}] {self.descricao} | R$ {self.preco:.2f} | Estoque: {self.estoque} | Cat: {self.id_categoria}"


class VendaItem:
    def __init__(self, id_produto, descricao_produto, preco_unitario, quantidade):
        self.id_produto = id_produto
        self.descricao_produto = descricao_produto
        self.preco_unitario = preco_unitario
        self.quantidade = quantidade

    @property
    def total(self):
        return self.preco_unitario * self.quantidade

    def __str__(self):
        return (f"  Produto: {self.descricao_produto} | "
                f"Qtd: {self.quantidade} | "
                f"Unit: R$ {self.preco_unitario:.2f} | "
                f"Total: R$ {self.total:.2f}")


class Venda:
    def __init__(self, id, id_cliente, data, status="concluida"):
        self.id = id
        self.id_cliente = id_cliente
        self.data = data
        self.status = status
        self.itens = []

    @property
    def total(self):
        return sum(item.total for item in self.itens)

    def __str__(self):
        return (f"Venda #{self.id} | Cliente ID: {self.id_cliente} | "
                f"Data: {self.data} | Total: R$ {self.total:.2f}")


class Avaliacao:
    """Nova funcionalidade - Tarefa 10: Avaliação de produto"""
    def __init__(self, id, id_produto, id_cliente, nota, comentario):
        self.id = id
        self.id_produto = id_produto
        self.id_cliente = id_cliente
        self.nota = nota          # 1 a 5
        self.comentario = comentario

    def __str__(self):
        return (f"  Avaliação #{self.id} | Produto ID: {self.id_produto} | "
                f"Cliente ID: {self.id_cliente} | Nota: {self.nota}/5 | "
                f"Comentário: {self.comentario}")