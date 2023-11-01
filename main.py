import matplotlib.pyplot as plt
import pandas as pd


# Função para ler os dados climáticos de um arquivo CSV
def ler_dados_climaticos(nome_arquivo):
    try:
        df = pd.read_csv(nome_arquivo)
        df['Data'] = pd.to_datetime(df['Data'])
        df['Temperatura'] = df['Temperatura'].astype(float)
        return df
    except FileNotFoundError:
        print(f"O arquivo '{nome_arquivo}' não foi encontrado.")
        return None


# Função para calcular a derivada da temperatura com média móvel de 3 dias
def calcular_derivada_temperatura(df):
    # Calcular a média móvel de 3 dias
    df['Media'] = df['Temperatura'].rolling(2).mean()

    # Calcular a derivada da temperatura
    df['Derivada'] = df['Media'].diff()

    return df


# Função para detectar mudanças significativas na temperatura
def detectar_mudancas_significativas(df, limiar):
    # Filtra os dados antes de calcular a derivada
    df = filtrar_dados(df)

    # Calcula a derivada da temperatura
    df = calcular_derivada_temperatura(df)

    # Detecta mudanças significativas
    mudancas = df[df['Derivada'] > limiar]
    return mudancas


# Função para filtrar dados discrepantes
def filtrar_dados(df):
    # Remove valores fora de um intervalo especificado
    df = df[df['Temperatura'] >= 0]
    df = df[df['Temperatura'] <= 50]
    return df


# Função para visualizar os dados e as mudanças detectadas
def visualizar_dados(df, mudancas):
    # Visualização dos dados
    plt.figure(figsize=(12, 6))
    plt.plot(df['Data'], df['Temperatura'], label='Temperatura', color='blue')
    plt.xlabel('Data')
    plt.ylabel('Temperatura')

    # Visualização da média dos dias
    try:
        df['Media'] = df['Temperatura'].rolling(7).mean()
        plt.plot(df['Data'], df['Media'], label='Média', color='orange')
    except KeyError:
        print("A coluna 'Media' não existe no DataFrame.")

    # Visualização das mudanças detectadas
    plt.scatter(mudancas['Data'], mudancas['Temperatura'], color='red', label='Mudanças significativas')

    # Escala do eixo y
    plt.ylim(0, 50)

    plt.grid(True)

    plt.legend()

    plt.title('Detecção de Mudanças na Temperatura')
    plt.show()


# Função principal
def main():
    nome_arquivo = "data/dados_climaticos.csv"

    df = ler_dados_climaticos(nome_arquivo)

    if df is None:
        return

    limiar = 2
    mudancas = detectar_mudancas_significativas(df, limiar)

    visualizar_dados(df, mudancas)


if __name__ == "__main__":
    main()
