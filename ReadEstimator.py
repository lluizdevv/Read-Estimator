import json
import os

CAMINHO_ARQUIVO = "usuarios.json"

#UTILIDADES
def carregar_usuarios():
    if not os.path.exists(CAMINHO_ARQUIVO):
        return []
    with open(CAMINHO_ARQUIVO, "r", encoding="utf-8") as f:
        return json.load(f)

def salvar_usuarios(usuarios):
    with open(CAMINHO_ARQUIVO, "w", encoding="utf-8") as f:
        json.dump(usuarios, f, indent=4, ensure_ascii=False)

#CADASTRO E LOGIN
def cadastrar_usuario():
    print("\n=== Cadastro ===")
    nome = input("Nome: ")
    idade = int(input("Idade: "))
    cidade = input("Cidade: ")
    estado = input("Estado: ")
    email = input("Email: ")
    senha = input("Senha: ")
    livros_digitais = int(input("Livros digitais lidos no último ano: "))
    livros_fisicos = int(input("Livros físicos lidos no último ano: "))
    preferencia = input("Preferência de leitura (Digital ou Físico): ")
    horas_estudo = float(input("Horas semanais de estudo com livros: "))
    horas_lazer = float(input("Horas semanais de leitura por entretenimento: "))
    objetivo = input("Objetivo principal com a leitura (Estudo, Lazer, Profissional, Outro): ")

    usuarios = carregar_usuarios()
    if any(u['email'] == email for u in usuarios):
        print("\n❌ Email já cadastrado.")
        return

    novo_usuario = {
        "nome": nome,
        "idade": idade,
        "cidade": cidade,
        "estado": estado,
        "email": email,
        "senha": senha,
        "livros_digitais": livros_digitais,
        "livros_fisicos": livros_fisicos,
        "preferencia": preferencia,
        "horas_estudo": horas_estudo,
        "horas_lazer": horas_lazer,
        "objetivo": objetivo
    }
    usuarios.append(novo_usuario)
    salvar_usuarios(usuarios)
    print("\n✅ Cadastro realizado com sucesso! Faça login para continuar.")

def fazer_login():
    print("\n=== Login ===")
    email = input("Email: ")
    senha = input("Senha: ")
    usuarios = carregar_usuarios()
    for u in usuarios:
        if u["email"] == email and u["senha"] == senha:
            print(f"\n✅ Bem-vindo, {u['nome']}!")
            executar_estatisticas(u)
            return
    print("❌ Email ou senha incorretos.")

#ESTATÍSTICAS
def executar_estatisticas(u):
    print("\n📊 Estatísticas de Leitura:")

    # 1. Mensagem personalizada
    print(f"Olá, {u['nome']} de {u['cidade']}, {u['estado']}! Com {u['idade']} anos, é ótimo ver seu interesse pela leitura!")

    # 2. Estimativa de leitura para os próximos 5 anos
    total_livros = u['livros_digitais'] + u['livros_fisicos']
    estimativa = total_livros * 5
    if total_livros >= 30:
        feedback = "📚 Você é um leitor assíduo!"
    elif total_livros >= 10:
        feedback = "📘 Boa frequência de leitura."
    else:
        feedback = "📖 Que tal tentar ler mais nos próximos anos?"
    print(f"Você leu {total_livros} livros no último ano. Em 5 anos manterá cerca de {estimativa} livros. {feedback}")

    # 3. Cálculo de horas de estudo por ano
    estudo_ano = u['horas_estudo'] * 52
    print(f"Horas de estudo com livros por ano: {estudo_ano:.1f}h")

    # 4. Cálculo de horas de lazer por ano
    lazer_ano = u['horas_lazer'] * 52
    print(f"Horas de leitura por lazer por ano: {lazer_ano:.1f}h")

    # 5. Tendência: perfil de leitor
    if u['livros_digitais'] > u['livros_fisicos']:
        perfil = "Leitor digital"
    elif u['livros_digitais'] < u['livros_fisicos']:
        perfil = "Leitor físico"
    else:
        perfil = "Leitor híbrido"
    print(f"Seu perfil de leitura: {perfil}")

    # 6. Tendência: tempo médio por livro
    horas_total = estudo_ano + lazer_ano
    tempo_medio = horas_total / total_livros if total_livros else 0
    print(f"Tempo médio gasto por livro (estudo+lazer): {tempo_medio:.1f}h")

#MENU INICIAL
def menu():
    while True:
        print("\n==== Menu Inicial ====")
        print("1 - Cadastrar")
        print("2 - Fazer Login")
        print("3 - Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_usuario()
        elif opcao == "2":
            fazer_login()
        elif opcao == "3":
            print("Encerrando...")
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    menu()

