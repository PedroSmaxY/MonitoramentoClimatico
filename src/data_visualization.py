import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('TkAgg')


def visualizar_dados(df, mudancas):
    plt.figure(figsize=(12, 6))
    plt.plot(df['Data'], df['Temperatura'], label='Temperatura', color='blue')
    plt.xlabel('Data')
    plt.ylabel('Temperatura')

    try:
        df['Media'] = df['Temperatura'].rolling(7).mean()
        plt.plot(df['Data'], df['Media'], label='Média', color='orange')
    except KeyError:
        print("A coluna 'Media' não existe no DataFrame.")

    plt.scatter(mudancas['Data'], mudancas['Temperatura'],
                color='red', label='Mudanças significativas')
    plt.ylim(0, 50)
    plt.grid(True)
    plt.legend()
    plt.title('Detecção de Mudanças na Temperatura')
    plt.show()
