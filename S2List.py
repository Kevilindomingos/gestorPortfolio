import json

# arquivo para armazenamento das listas
ARQUIVO_DADOS = "portfolio.json"

def carregar_dados():
    try:
        with open(ARQUIVO_DADOS, "r", encoding="utf-8") as f:   # encoding serve como tradutor de caracteres especiais
            return json.load(f)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        print("\nO arquivo de dados está corrompido. Iniciando uma lista vazia.")
        return []

def salvar_dados():
    with open(ARQUIVO_DADOS, "w", encoding="utf-8") as f:
        # indent = formata o JSON para ficar legivel e organizado
        # ensure_ascii = converte os caracteres corretamente e mantém letras com acentos.
        json.dump(projetos, f, indent=4, ensure_ascii=False)

def ver_estatisticas():
    print("\n--- STATUS GERAL ---")
    concluidos = sum(1 for p in projetos if p['finalizado'])
    pendentes = len(projetos) - concluidos

    print(f"Projetos prontos: {concluidos}")
    print(f"Projetos fazendo: {pendentes}")

    if len(projetos) > 0:
        media = concluidos / 4
        print(f"Média de finalizados (por mês): {media} por semana")

    ultimo = "Nenhum ainda"
    for p in projetos:
        if p['finalizado']:
            ultimo = p['nome']
    print(f"Último que você terminou: {ultimo}")

def buscar_por_termo():
    termo = input("Digite o que quer buscar: ").strip().lower()
    print(f"\nResultados para '{termo}':")
    achou = False
    for p in projetos:
        if termo in p['nome'].lower():
            status = "OK" if p['finalizado'] else "Pendente"
            print(f"- {p['nome']} [{status}]")
            achou = True
    if not achou:
        print("Não achei nada com esse nome.")

def adicionar_projeto():
    nome = input("Nome do projeto: ").strip()
    if not nome:
        print("Erro: O nome não pode ser vazio.")
        return
    novo = {
        "nome": nome,
        "finalizado": False,
        "observacoes": "Nenhuma",
        "historico": []
    }
    projetos.append(novo)
    print(f"Projeto '{nome}' adicionado.")

def listar_projetos():
    if not projetos:
        print("\n[!] Nenhum projeto cadastrado.")
        return
    print("\n--- LISTA DE PROJETOS ---")
    for i, p in enumerate(projetos, 1):
        status = "Finalizado" if p['finalizado'] else "Pendente"
        obs = p['observacoes']
        print(f"{i}. {p['nome']} \n | Observação: {obs} \n | Status: {status}")
        print("-" * 30)

def atualizar_projeto():
    nome_busca = input("Nome do projeto para atualizar: ")
    p = next((proj for proj in projetos if proj['nome'].lower() == nome_busca.lower()), None)

    if p is None:
        print("Erro: Projeto não encontrado.")
        return

    print(f"\nEditando: {p['nome']} (ENTER para manter)")
    novo_nome = input("Novo nome: ").strip()
    status_in = input(f"Finalizado? S/N (Atual: {'S' if p['finalizado'] else 'N'}): ").strip().lower()
    nova_obs = input("Nova observação: ").strip()

    if novo_nome: p['nome'] = novo_nome
    if status_in in ['s', 'sim']:
        p['finalizado'] = True
    elif status_in in ['n', 'nao', 'não']:
        p['finalizado'] = False
    if nova_obs: p['observacoes'] = nova_obs

    p['historico'].append((p['nome'], p['finalizado']))
    print("Projeto atualizado.")

def remover_projeto():
    nome_busca = input("Nome do projeto para remover: ")
    p = next((proj for proj in projetos if proj['nome'].lower() == nome_busca.lower()), None)
    if p:
        confirmar = input(f"Remover '{p['nome']}'? (S/N): ").strip().lower()
        if confirmar in ['s', 'sim']:
            projetos.remove(p)
            print("Removido.")
        else:
            print("Cancelado.")
    else:
        print("Erro: Não encontrado.")

projetos = carregar_dados()

# loop inicial
while True:
        print("\n=== GESTOR DE PORTFÓLIO PESSOAL ===")
        print("ADD    - Adicionar projeto")
        print("LIST   - Listar projetos")
        print("UPDATE - Atualizar projeto")
        print("DELETE - Remover projeto")
        print("STATS  - Estatísticas")
        print("SEARCH - Buscar termo")
        print("QUIT   - Sair")

        opcao = input("Escolha uma opção: ").upper().strip()

        if opcao    == "ADD": adicionar_projeto()
        elif opcao  == "LIST": listar_projetos()
        elif opcao  == "UPDATE": atualizar_projeto()
        elif opcao  == "DELETE": remover_projeto()
        elif opcao  == "STATS": ver_estatisticas()
        elif opcao  == "SEARCH": buscar_por_termo()
        elif opcao  == "QUIT":
            salvar_dados()
            print("Dados salvos. Até logo!")
            break
        else:
            print("Opção inválida.")
