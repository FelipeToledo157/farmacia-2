import csv

ARQUIVO = "medicamentos.csv"

CAMPOS = ["nome", "categoria", "quantidade"]


def salvar_medicamentos(medicamentos):
    with open(ARQUIVO, "w", newline="", encoding="utf-8") as arquivo:
        escritor = csv.DictWriter(arquivo, fieldnames=CAMPOS)

        escritor.writeheader()

        for medicamento in medicamentos:
            escritor.writerow(medicamento)


def carregar_medicamentos():
    medicamentos = []

    if (ARQUIVO):
        with open(ARQUIVO, "r", encoding="utf-8") as arquivo:
            leitor = csv.DictReader(arquivo)

            for medicamento in leitor:
                medicamento["quantidade"] = int(medicamento["quantidade"])
                medicamentos.append(medicamento)

    return medicamentos


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

