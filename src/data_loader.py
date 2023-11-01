import pandas as pd


def ler_dados_climaticos(nome_arquivo):
    try:
        df = pd.read_csv(nome_arquivo)
        df['Data'] = pd.to_datetime(df['Data'])
        df['Temperatura'] = df['Temperatura'].astype(float)
        return df
    except FileNotFoundError:
        print(f"O arquivo '{nome_arquivo}' não foi encontrado.")
        return None
