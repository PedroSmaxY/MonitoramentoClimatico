def filtrar_dados(df):
    df = df[df['Temperatura'] >= 0]
    df = df[df['Temperatura'] <= 50]
    return df
