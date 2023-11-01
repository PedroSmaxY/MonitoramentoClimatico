import data_filter


def calcular_derivada_temperatura(df):
    df['Media'] = df['Temperatura'].rolling(2).mean()
    df['Derivada'] = df['Media'].diff()
    return df


def detectar_mudancas_significativas(df, limiar):
    df = data_filter.filtrar_dados(df)
    df = calcular_derivada_temperatura(df)
    mudancas = df[df['Derivada'] > limiar]
    return mudancas
