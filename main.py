from src import data_loader
from src import data_processing
from src import data_visualization


def main():
    nome_arquivo = "../data/climate_data.csv"
    df = data_loader.ler_dados_climaticos(nome_arquivo)

    if df is None:
        return

    limiar = 2
    mudancas = data_processing.detectar_mudancas_significativas(df, limiar)

    data_visualization.visualizar_dados(df, mudancas)


if __name__ == "__main__":
    main()
