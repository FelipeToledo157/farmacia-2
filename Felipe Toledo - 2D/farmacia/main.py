import csv
import os


def carregar_medicamentos():
    medicamentos = []

    caminho_csv = os.path.join(
        os.path.dirname(__file__),
        "medicamentos.csv"
    )

    with open(caminho_csv, "r", encoding="utf-8") as arquivo:
        leitor = csv.DictReader(arquivo)

        for medicamento in leitor:
            medicamento["quantidade"] = int(medicamento["quantidade"])
            medicamentos.append(medicamento)

    return medicamentos


def salvar_medicamentos(medicamentos):
    caminho_csv = os.path.join(
        os.path.dirname(__file__),
        "medicamentos.csv"
    )

    with open(caminho_csv, "w", newline="", encoding="utf-8") as arquivo:
        campos = ["nome", "categoria", "quantidade"]

        escritor = csv.DictWriter(
            arquivo,
            fieldnames=campos
        )

        escritor.writeheader()
        escritor.writerows(medicamentos)


def cadastrar_medicamento(medicamentos):
    print("\n--- CADASTRAR MEDICAMENTO ---")

    nome = input("Nome: ").strip()
    categoria = input("Categoria: ").strip()
    quantidade = input("Quantidade em estoque: ").strip()

    if not quantidade.isdigit():
        print("Digite uma quantidade válida.")
        return

    medicamento = {
        "nome": nome,
        "categoria": categoria,
        "quantidade": int(quantidade)
    }

    medicamentos.append(medicamento)

    salvar_medicamentos(medicamentos)

    print("Medicamento cadastrado com sucesso!")


def listar_medicamentos(medicamentos):
    print("\n--- MEDICAMENTOS CADASTRADOS ---")

    if not medicamentos:
        print("Nenhum medicamento cadastrado.")
        return

    for medicamento in medicamentos:
        print("Nome:", medicamento["nome"])
        print("Categoria:", medicamento["categoria"])
        print("Quantidade:", medicamento["quantidade"])
        print("------------------------")


def buscar_medicamento(medicamentos):
    print("\n--- BUSCAR MEDICAMENTO ---")

    nome = input("Digite o nome do medicamento: ").strip().lower()

    for medicamento in medicamentos:
        if medicamento["nome"].lower() == nome:
            print("\nMedicamento encontrado!")
            print("Nome:", medicamento["nome"])
            print("Categoria:", medicamento["categoria"])
            print("Quantidade:", medicamento["quantidade"])
            return

    print("Medicamento não encontrado.")


def main():
    medicamentos = carregar_medicamentos()

    while True:
        print("\n==============================")
        print("          FARMÁCIA")
        print("==============================")
        print("1 - Cadastrar medicamento")
        print("2 - Listar medicamentos")
        print("3 - Buscar medicamento")
        print("4 - Sair")
        print("==============================")

        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            cadastrar_medicamento(medicamentos)

        elif opcao == "2":
            listar_medicamentos(medicamentos)

        elif opcao == "3":
            buscar_medicamento(medicamentos)

        elif opcao == "4":
            print("Programa encerrado.")
            break

        else:
            print("Opção inválida.")


main()
