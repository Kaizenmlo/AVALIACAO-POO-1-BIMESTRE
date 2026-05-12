🏗️ Arquitetura em Camadas
O sistema é dividido em 4 camadas que se comunicam em sequência:

UI  →  View  →  DAO  →  Model
(tela)  (regras)  (dados)  (entidades)
Cada camada só conversa com a camada imediatamente abaixo. A UI nunca acessa o DAO diretamente, por exemplo. Isso é o conceito de programação em camadas.

📄 model.py — Camada Model (Entidades)
São as classes que representam os objetos do mundo real do sistema. Não têm lógica de negócio, só guardam dados.

class Cliente
def __init__(self, id, nome, email, fone, senha):
Representa um cliente do sistema. Guarda id, nome, email, telefone e senha.

class Categoria
def __init__(self, id, descricao):
Representa uma categoria de produto. Ex: "Eletrônicos", "Roupas".

class Produto
def __init__(self, id, descricao, preco, estoque, id_categoria):
Representa um produto à venda. Tem preço, estoque e pertence a uma categoria.

class VendaItem
@property
def total(self):
    return self.preco_unitario * self.quantidade
Representa um item dentro de uma venda (um produto + quantidade comprada). O @property faz o total ser calculado automaticamente sempre que acessado, sem precisar chamar como método.

class Venda
self.itens = []  # lista de VendaItem
@property
def total(self):
    return sum(item.total for item in self.itens)
Representa uma compra finalizada. Contém vários VendaItem e calcula o total somando todos os itens.

class Avaliacao (Tarefa 10 — Nova funcionalidade)
def __init__(self, id, id_produto, id_cliente, nota, comentario):
Nova entidade criada para a Tarefa 10. Permite que clientes avaliem produtos com nota (1 a 5) e comentário.

📄 dao.py — Camada DAO (Data Access Object)
Responsável por armazenar e recuperar dados. Em um sistema real usaria banco de dados. Aqui usa listas em memória (os dados somem quando o programa fecha).

Cada DAO tem atributos de classe estáticos (_clientes = []) — isso significa que a lista é compartilhada por toda a aplicação, não por instância.

ClienteDAO
_clientes = []      # lista que armazena todos os clientes
_proximo_id = 1     # controla o ID automático
listar() → retorna todos os clientes
inserir(...) → cria um objeto Cliente e adiciona na lista
buscar_por_id(id) → percorre a lista e retorna o cliente com aquele id
buscar_por_email(email) → busca por email (usado no login)
atualizar(...) → encontra o cliente e modifica seus atributos
excluir(id) → recria a lista sem o cliente de aquele id (list comprehension)
CategoriaDAO e ProdutoDAO
Mesma estrutura do ClienteDAO. O ProdutoDAO tem um método extra:

def reajustar(percentual):
    for p in ProdutoDAO._produtos:
        p.preco = p.preco * (1 + percentual / 100)
Percorre todos os produtos e aumenta o preço pelo percentual informado.

VendaDAO
def listar_por_cliente(id_cliente):
    return [v for v in VendaDAO._vendas if v.id_cliente == id_cliente]
Filtra as vendas pelo id do cliente — usado em "Listar minhas compras".

VendaItemDAO
def inserir(venda, id_produto, ...):
    item = VendaItem(...)
    venda.itens.append(item)  # adiciona o item dentro da venda
Cria um VendaItem e anexa diretamente dentro do objeto Venda.

AvaliacaoDAO (Tarefa 10)
Armazena avaliações e permite buscar por produto.

📄 view.py — Camada View (Regras de Negócio)
É o cérebro do sistema. Valida dados, aplica regras e orquestra as operações entre DAO e UI. A UI nunca chama o DAO diretamente — sempre passa pela View.

Login
def Login(email, senha, admin_senha):
    if email == "admin@sistema.com" and senha == admin_senha:
        return "admin", None
    cliente = ClienteDAO.buscar_por_email(email)
    if cliente and cliente.senha == senha:
        return "cliente", cliente
    raise ValueError("Email ou senha inválidos.")
Verifica se é admin (email+senha fixos) ou cliente (busca no DAO). Se não encontrar, lança exceção.

Carrinho_Inserir
# Se produto já está no carrinho, SOMA a quantidade
for item in carrinho:
    if item["id_produto"] == id_produto:
        item["quantidade"] += quantidade
        return
# Senão, adiciona novo item
carrinho.append({...})
Implementa a regra da Tarefa 5: não duplica o produto no carrinho, soma as quantidades.

Carrinho_Comprar
def Carrinho_Comprar(carrinho, id_cliente):
    venda = VendaDAO.inserir(id_cliente, data)       # cria a venda
    for item in carrinho:
        produto.estoque -= item["quantidade"]         # desconta estoque
        VendaItemDAO.inserir(venda, ...)              # registra os itens
    carrinho.clear()                                  # limpa o carrinho
Cria a venda, desconta o estoque de cada produto e limpa o carrinho no final.

Validações (exemplos)
if ClienteDAO.buscar_por_email(email):
    raise ValueError("Email já cadastrado.")  # impede email duplicado

if quantidade > produto.estoque:
    raise ValueError("Estoque insuficiente.") # impede compra sem estoque
Todas as validações lançam ValueError com mensagem, que a UI captura e exibe.

📄 ui.py — Camada UI (Interface do Usuário)
É o que o usuário vê e interage. Mostra menus, lê entradas do teclado, chama a View e exibe resultados. Não tem regra de negócio — só apresentação.

Fluxo principal
Main() → Menu() → Abrir_Conta() ou Entrar_Sistema()
                         ↓
              Menu_Admin() ou Menu_Cliente()
Menu_Admin() — opções do administrador
Manter Categorias (listar/inserir/atualizar/excluir)
Manter Produtos (listar/inserir/atualizar/excluir)
Manter Clientes
Reajustar preços
Listar todas as vendas
Menu_Cliente() — opções do cliente
Listar produtos disponíveis
Inserir produto no carrinho
Visualizar carrinho
Comprar carrinho
Listar minhas compras
Avaliar produto (Tarefa 10)
Tratamento de erros
try:
    View.Cliente_Inserir(nome, email, fone, senha)
    print("Conta criada com sucesso!")
except ValueError as e:
    print(f"Erro: {e}")
Todo bloco que chama a View usa try/except para capturar os erros da View e mostrar a mensagem amigável ao usuário.

📄 main.py — Ponto de Entrada
if __name__ == "__main__":
    UI.Main()
Só inicia o programa chamando UI.Main(). O if __name__ == "__main__" garante que o código só roda quando o arquivo é executado diretamente.

🔑 Conceitos importantes para o professor perguntar
Pergunta provável	Resposta
Por que usar camadas?	Separação de responsabilidades — cada camada tem uma função clara, facilitando manutenção
O que é DAO?	Camada que abstrai o acesso aos dados, isolando a lógica de armazenamento
Por que usar @staticmethod?	Não precisa de instância (self), pois os dados são compartilhados (atributos de classe)
Por que usar @property?	Para calcular total automaticamente sem armazenar um valor que pode ficar desatualizado
O que é raise ValueError?	Lança uma exceção quando uma regra de negócio é violada, que a UI captura com try/except
Qual a nova funcionalidade?	Avaliação de produtos: clientes dão nota (1-5) e comentário após comprar
Como o admin é criado?	Automaticamente pelo sistema com email e senha fixos (admin@sistema.com / admin123)
Como o carrinho evita duplicatas?	A View percorre o carrinho; se o produto já existe, soma a quantidade em vez de inserir novo item