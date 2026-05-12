from view import View

ADMIN_SENHA = "admin123"


class UI:

    @staticmethod
    def Main():
        # Cadastro automático do admin já está definido por ADMIN_SENHA
        print("=" * 50)
        print("   SISTEMA DE COMÉRCIO ELETRÔNICO")
        print("=" * 50)

        while True:
            UI.Menu()

    @staticmethod
    def Menu():
        print("\n--- MENU INICIAL ---")
        print("1. Abrir conta")
        print("2. Entrar no sistema")
        print("0. Sair do programa")
        opcao = input("Escolha: ").strip()

        if opcao == "1":
            UI.Abrir_Conta()
        elif opcao == "2":
            UI.Entrar_Sistema()
        elif opcao == "0":
            print("Encerrando o programa. Até logo!")
            exit()
        else:
            print("Opção inválida.")

    # ===================== VISITANTE =====================

    @staticmethod
    def Abrir_Conta():
        print("\n--- ABRIR CONTA ---")
        nome = input("Nome: ").strip()
        email = input("Email: ").strip()
        fone = input("Fone: ").strip()
        senha = input("Senha: ").strip()
        try:
            View.Cliente_Inserir(nome, email, fone, senha)
            print("Conta criada com sucesso!")
        except ValueError as e:
            print(f"Erro: {e}")

    @staticmethod
    def Entrar_Sistema():
        print("\n--- ENTRAR NO SISTEMA ---")
        email = input("Email: ").strip()
        senha = input("Senha: ").strip()
        try:
            perfil, cliente = View.Login(email, senha, ADMIN_SENHA)
            if perfil == "admin":
                print("Bem-vindo, Admin!")
                UI.Menu_Admin()
            else:
                print(f"Bem-vindo, {cliente.nome}!")
                UI.Menu_Cliente(cliente)
        except ValueError as e:
            print(f"Erro: {e}")

    # ===================== MENU ADMIN =====================

    @staticmethod
    def Menu_Admin():
        while True:
            print("\n--- MENU ADMIN ---")
            print("1. Manter Categorias")
            print("2. Manter Produtos")
            print("3. Manter Clientes")
            print("4. Reajustar preços")
            print("5. Listar todas as vendas")
            print("0. Sair do sistema")
            opcao = input("Escolha: ").strip()

            if opcao == "1":
                UI.Menu_Categoria()
            elif opcao == "2":
                UI.Menu_Produto()
            elif opcao == "3":
                UI.Menu_Cliente_Admin()
            elif opcao == "4":
                UI.Produto_Reajustar()
            elif opcao == "5":
                UI.Listar_Vendas()
            elif opcao == "0":
                print("Saindo do sistema...")
                break
            else:
                print("Opção inválida.")

    # ===================== MENU CLIENTE =====================

    @staticmethod
    def Menu_Cliente(cliente):
        carrinho = []
        while True:
            print(f"\n--- MENU CLIENTE ({cliente.nome}) ---")
            print("1. Listar produtos")
            print("2. Inserir produto no carrinho")
            print("3. Visualizar carrinho")
            print("4. Comprar carrinho")
            print("5. Listar minhas compras")
            print("6. Avaliar produto")
            print("7. Ver avaliações de um produto")
            print("0. Sair do sistema")
            opcao = input("Escolha: ").strip()

            if opcao == "1":
                UI.Produto_Listar()
            elif opcao == "2":
                UI.Carrinho_Inserir(carrinho)
            elif opcao == "3":
                UI.Carrinho_Visualizar(carrinho)
            elif opcao == "4":
                UI.Carrinho_Comprar(carrinho, cliente.id)
            elif opcao == "5":
                UI.Listar_Minhas_Compras(cliente.id)
            elif opcao == "6":
                UI.Avaliacao_Inserir(cliente.id)
            elif opcao == "7":
                UI.Avaliacao_Listar()
            elif opcao == "0":
                print("Saindo do sistema...")
                break
            else:
                print("Opção inválida.")

    # ===================== CATEGORIAS =====================

    @staticmethod
    def Menu_Categoria():
        while True:
            print("\n--- CATEGORIAS ---")
            print("1. Listar")
            print("2. Inserir")
            print("3. Atualizar")
            print("4. Excluir")
            print("0. Voltar")
            opcao = input("Escolha: ").strip()

            if opcao == "1":
                UI.Categoria_Listar()
            elif opcao == "2":
                UI.Categoria_Inserir()
            elif opcao == "3":
                UI.Categoria_Atualizar()
            elif opcao == "4":
                UI.Categoria_Excluir()
            elif opcao == "0":
                break
            else:
                print("Opção inválida.")

    @staticmethod
    def Categoria_Listar():
        cats = View.Categoria_Listar()
        if not cats:
            print("Nenhuma categoria cadastrada.")
        else:
            print("\n--- LISTA DE CATEGORIAS ---")
            for c in cats:
                print(c)

    @staticmethod
    def Categoria_Inserir():
        desc = input("Descrição: ").strip()
        try:
            View.Categoria_Inserir(desc)
            print("Categoria inserida com sucesso!")
        except ValueError as e:
            print(f"Erro: {e}")

    @staticmethod
    def Categoria_Atualizar():
        UI.Categoria_Listar()
        try:
            id = int(input("ID da categoria: "))
            desc = input("Nova descrição: ").strip()
            View.Categoria_Atualizar(id, desc)
            print("Categoria atualizada com sucesso!")
        except ValueError as e:
            print(f"Erro: {e}")

    @staticmethod
    def Categoria_Excluir():
        UI.Categoria_Listar()
        try:
            id = int(input("ID da categoria a excluir: "))
            View.Categoria_Excluir(id)
            print("Categoria excluída com sucesso!")
        except ValueError as e:
            print(f"Erro: {e}")

    # ===================== PRODUTOS =====================

    @staticmethod
    def Menu_Produto():
        while True:
            print("\n--- PRODUTOS ---")
            print("1. Listar")
            print("2. Inserir")
            print("3. Atualizar")
            print("4. Excluir")
            print("0. Voltar")
            opcao = input("Escolha: ").strip()

            if opcao == "1":
                UI.Produto_Listar()
            elif opcao == "2":
                UI.Produto_Inserir()
            elif opcao == "3":
                UI.Produto_Atualizar()
            elif opcao == "4":
                UI.Produto_Excluir()
            elif opcao == "0":
                break
            else:
                print("Opção inválida.")

    @staticmethod
    def Produto_Listar():
        prods = View.Produto_Listar()
        if not prods:
            print("Nenhum produto cadastrado.")
        else:
            print("\n--- LISTA DE PRODUTOS ---")
            for p in prods:
                cat = next((c for c in View.Categoria_Listar() if c.id == p.id_categoria), None)
                cat_desc = cat.descricao if cat else "N/A"
                print(f"[{p.id}] {p.descricao} | R$ {p.preco:.2f} | Estoque: {p.estoque} | Categoria: {cat_desc}")

    @staticmethod
    def Produto_Inserir():
        UI.Categoria_Listar()
        try:
            desc = input("Descrição: ").strip()
            preco = float(input("Preço: "))
            estoque = int(input("Estoque: "))
            id_cat = int(input("ID da Categoria: "))
            View.Produto_Inserir(desc, preco, estoque, id_cat)
            print("Produto inserido com sucesso!")
        except ValueError as e:
            print(f"Erro: {e}")

    @staticmethod
    def Produto_Atualizar():
        UI.Produto_Listar()
        try:
            id = int(input("ID do produto: "))
            desc = input("Nova descrição: ").strip()
            preco = float(input("Novo preço: "))
            estoque = int(input("Novo estoque: "))
            id_cat = int(input("Nova ID de categoria: "))
            View.Produto_Atualizar(id, desc, preco, estoque, id_cat)
            print("Produto atualizado com sucesso!")
        except ValueError as e:
            print(f"Erro: {e}")

    @staticmethod
    def Produto_Excluir():
        UI.Produto_Listar()
        try:
            id = int(input("ID do produto a excluir: "))
            View.Produto_Excluir(id)
            print("Produto excluído com sucesso!")
        except ValueError as e:
            print(f"Erro: {e}")

    @staticmethod
    def Produto_Reajustar():
        try:
            percentual = float(input("Percentual de reajuste (%): "))
            View.Produto_Reajustar(percentual)
            print(f"Preços reajustados em {percentual}% com sucesso!")
        except ValueError as e:
            print(f"Erro: {e}")

    # ===================== CLIENTES (ADMIN) =====================

    @staticmethod
    def Menu_Cliente_Admin():
        while True:
            print("\n--- CLIENTES ---")
            print("1. Listar")
            print("2. Atualizar")
            print("3. Excluir")
            print("0. Voltar")
            opcao = input("Escolha: ").strip()

            if opcao == "1":
                UI.Cliente_Listar()
            elif opcao == "2":
                UI.Cliente_Atualizar()
            elif opcao == "3":
                UI.Cliente_Excluir()
            elif opcao == "0":
                break
            else:
                print("Opção inválida.")

    @staticmethod
    def Cliente_Listar():
        clientes = View.Cliente_Listar()
        if not clientes:
            print("Nenhum cliente cadastrado.")
        else:
            print("\n--- LISTA DE CLIENTES ---")
            for c in clientes:
                print(c)

    @staticmethod
    def Cliente_Atualizar():
        UI.Cliente_Listar()
        try:
            id = int(input("ID do cliente: "))
            nome = input("Novo nome: ").strip()
            email = input("Novo email: ").strip()
            fone = input("Novo fone: ").strip()
            senha = input("Nova senha: ").strip()
            View.Cliente_Atualizar(id, nome, email, fone, senha)
            print("Cliente atualizado com sucesso!")
        except ValueError as e:
            print(f"Erro: {e}")

    @staticmethod
    def Cliente_Excluir():
        UI.Cliente_Listar()
        try:
            id = int(input("ID do cliente a excluir: "))
            View.Cliente_Excluir(id)
            print("Cliente excluído com sucesso!")
        except ValueError as e:
            print(f"Erro: {e}")

    # ===================== CARRINHO =====================

    @staticmethod
    def Carrinho_Inserir(carrinho):
        UI.Produto_Listar()
        try:
            id_prod = int(input("ID do produto: "))
            qtd = int(input("Quantidade: "))
            View.Carrinho_Inserir(carrinho, id_prod, qtd)
            print("Produto adicionado ao carrinho!")
        except ValueError as e:
            print(f"Erro: {e}")

    @staticmethod
    def Carrinho_Visualizar(carrinho):
        itens = View.Carrinho_Visualizar(carrinho)
        if not itens:
            print("Carrinho vazio.")
            return
        print("\n--- CARRINHO ---")
        total = 0
        for item in itens:
            subtotal = item["preco"] * item["quantidade"]
            total += subtotal
            print(f"  {item['descricao']} | Unit: R$ {item['preco']:.2f} | Qtd: {item['quantidade']} | Total: R$ {subtotal:.2f}")
        print(f"TOTAL DO CARRINHO: R$ {total:.2f}")

    @staticmethod
    def Carrinho_Comprar(carrinho, id_cliente):
        UI.Carrinho_Visualizar(carrinho)
        if not carrinho:
            return
        confirma = input("Confirmar compra? (s/n): ").strip().lower()
        if confirma == "s":
            try:
                venda = View.Carrinho_Comprar(carrinho, id_cliente)
                print(f"Compra realizada com sucesso! Venda #{venda.id} | Total: R$ {venda.total:.2f}")
            except ValueError as e:
                print(f"Erro: {e}")

    # ===================== VENDAS =====================

    @staticmethod
    def Listar_Minhas_Compras(id_cliente):
        vendas = View.Vendas_ListarPorCliente(id_cliente)
        if not vendas:
            print("Nenhuma compra realizada.")
            return
        print("\n--- MINHAS COMPRAS ---")
        for v in vendas:
            print(v)
            for item in v.itens:
                print(item)

    @staticmethod
    def Listar_Vendas():
        vendas = View.Vendas_ListarTodas()
        if not vendas:
            print("Nenhuma venda realizada.")
            return
        print("\n--- TODAS AS VENDAS ---")
        for v in vendas:
            cliente = next((c for c in View.Cliente_Listar() if c.id == v.id_cliente), None)
            nome_cliente = cliente.nome if cliente else "N/A"
            print(f"Venda #{v.id} | Cliente: {nome_cliente} | Data: {v.data} | Total: R$ {v.total:.2f}")
            for item in v.itens:
                print(item)

    # ===================== AVALIAÇÕES (Tarefa 10) =====================

    @staticmethod
    def Avaliacao_Inserir(id_cliente):
        UI.Produto_Listar()
        try:
            id_prod = int(input("ID do produto a avaliar: "))
            nota = int(input("Nota (1 a 5): "))
            comentario = input("Comentário: ").strip()
            View.Avaliacao_Inserir(id_prod, id_cliente, nota, comentario)
            print("Avaliação registrada com sucesso!")
        except ValueError as e:
            print(f"Erro: {e}")

    @staticmethod
    def Avaliacao_Listar():
        UI.Produto_Listar()
        try:
            id_prod = int(input("ID do produto: "))
            avals = View.Avaliacao_ListarPorProduto(id_prod)
            if not avals:
                print("Nenhuma avaliação para este produto.")
            else:
                print(f"\n--- AVALIAÇÕES DO PRODUTO {id_prod} ---")
                for a in avals:
                    print(a)
        except ValueError as e:
            print(f"Erro: {e}")