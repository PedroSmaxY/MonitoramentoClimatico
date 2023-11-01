# Monitoramento Climático

Este programa detecta mudanças significativas na temperatura usando uma derivada da temperatura com média móvel de 3 dias.

## Instalação
Para instalar o programa, siga estas etapas:

- Clone o repositório do GitHub.
- Instale as dependências necessárias:
  `pip install matplotlib pandas`


## Uso

Para usar o programa, siga estas etapas:

1. Insira o caminho do arquivo CSV com os dados climáticos no argumento `nome_arquivo`.
2. Insira o limiar de mudança significativa no argumento `limiar`.

## Exemplo

python deteccao_mudancas_temperatura.py data/dados_climaticos.csv 2

Este exemplo irá detectar mudanças significativas na temperatura usando um limiar de 2 graus Celsius.

## Exemplo de Gráfico Gerado:

![image](https://github.com/PedroSmaxY/MonitoramentoClimatico/assets/127573080/276c5ec3-4341-4eec-9d23-3aa6db22a762)



## Resultados
O programa irá gerar um gráfico mostrando os dados climáticos e as mudanças detectadas. O gráfico terá as seguintes características:

- A linha azul representa a temperatura.
- A linha laranja representa a média dos dias.
- Os pontos vermelhos representam as mudanças significativas.
- Contribuições
- Contribuições são bem-vindas. Para contribuir com o programa, siga estas etapas:

Faça um fork do repositório do GitHub.
Faça suas alterações.
Crie um pull request.
