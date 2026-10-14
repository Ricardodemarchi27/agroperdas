
import json
import os


def calcular_perdas(area, produtividade, percentual_perda, preco_tonelada):
    producao_total = area * produtividade
    toneladas_perdidas = producao_total * (percentual_perda / 100)
    prejuizo = toneladas_perdidas * preco_tonelada

    return producao_total, toneladas_perdidas, prejuizo


def salvar_historico(resultado):
    nome_arquivo = "historico_agroperdas.json"

    if os.path.exists(nome_arquivo):
        try:
            with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
                historico = json.load(arquivo)

            if not isinstance(historico, list):
                historico = []

        except (json.JSONDecodeError, OSError):
            historico = []
    else:
        historico = []

    historico.append(resultado)

    with open(nome_arquivo, "w", encoding="utf-8") as arquivo:
        json.dump(historico, arquivo, ensure_ascii=False, indent=4)


def main():
    tabela_memoria = []

    print("=" * 40)
    print("          SISTEMA AGROPERDAS")
    print("  Calculadora de perdas na colheita")
    print("=" * 40)

    try:
        area = float(input("Área plantada (hectares): ").replace(",", "."))
        produtividade = float(
            input("Produtividade (toneladas por hectare): ").replace(",", ".")
        )
        percentual_perda = float(
            input("Percentual de perdas (%): ").replace(",", ".")
        )
        preco_tonelada = float(
            input("Preço por tonelada (R$): ").replace(",", ".")
        )

        if not all(map(lambda x: x == x and abs(x) != float("inf"),
                       [area, produtividade, percentual_perda, preco_tonelada])):
            print("Erro: informe apenas números finitos.")
            return

        if area <= 0:
            print("Erro: a área deve ser maior que zero.")
            return

        if produtividade <= 0:
            print("Erro: a produtividade deve ser maior que zero.")
            return

        if not 0 <= percentual_perda <= 100:
            print("Erro: as perdas devem estar entre 0 e 100%.")
            return

        if preco_tonelada <= 0:
            print("Erro: o preço deve ser maior que zero.")
            return

        producao, perdas, prejuizo = calcular_perdas(
            area, produtividade, percentual_perda, preco_tonelada
        )

        faixas_perda = [5, 10, 15]

        if percentual_perda <= faixas_perda[0]:
            classificacao = "Baixa"
        elif percentual_perda <= faixas_perda[1]:
            classificacao = "Moderada"
        else:
            classificacao = "Alta"

        dados_resumidos = (area, produtividade, percentual_perda, prejuizo)

        resultado = {
            "area_hectares": area,
            "produtividade_toneladas_hectare": produtividade,
            "percentual_perda": percentual_perda,
            "preco_por_tonelada": preco_tonelada,
            "producao_total": producao,
            "toneladas_perdidas": perdas,
            "classificacao_perda": classificacao,
            "prejuizo_reais": prejuizo
        }

        tabela_memoria.append(resultado)

        salvar_historico(resultado)
        print("\nAnálise adicionada ao histórico!")

        with open("agroperdas.json", "w", encoding="utf-8") as arquivo:
            json.dump(resultado, arquivo, ensure_ascii=False, indent=4)

        print("Dados salvos no arquivo agroperdas.json!")

        with open("agroperdas.txt", "w", encoding="utf-8") as arquivo:
            arquivo.write("RELATORIO AGROPERDAS\n")
            arquivo.write("=" * 30 + "\n")

            for chave, valor in resultado.items():
                arquivo.write(f"{chave}: {valor}\n")

        print("Dados salvos no arquivo agroperdas.txt!")

        print("\n" + "=" * 40)
        print("           RESULTADO")
        print("=" * 40)
        print(f"Produção esperada: {producao:.2f} toneladas")
        print(f"Produção perdida:  {perdas:.2f} toneladas")
        print(f"Prejuízo estimado: R$ {prejuizo:,.2f}")
        print(f"Classificação das perdas: {classificacao}")
        print("=" * 40)

        print("\nDADOS REGISTRADOS")
        for chave, valor in resultado.items():
            print(f"{chave}: {valor}")

        print("\nTABELA DE MEMÓRIA")
        print("-" * 40)

        for indice, analise in enumerate(tabela_memoria, start=1):
            print(f"Análise {indice}:")
            print(f"Área: {analise['area_hectares']} hectares")
            print(f"Perda: {analise['toneladas_perdidas']} toneladas")
            print(f"Prejuízo: R$ {analise['prejuizo_reais']:.2f}")
            print("-" * 40)

        print(f"\nResumo em tupla: {dados_resumidos}")

    except ValueError:
        print("Erro: digite números válidos.")

    except OSError as erro:
        print(f"Erro ao acessar um arquivo: {erro}")


if __name__ == "__main__":
    main()
