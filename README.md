# Monitoramento Climático

Este programa detecta mudanças significativas na temperatura usando uma derivada da temperatura com média móvel de 2 dias.

## Instalação
Para instalar o programa, siga estas etapas:

- Clone o repositório do GitHub.
- Instale as dependências necessárias:
  `pip install matplotlib pandas`


## Uso

Para usar o programa, siga estas etapas:

1. Insira o caminho do arquivo CSV com os dados climáticos no argumento `nome_arquivo` no arquivo main.py.
2. Insira o limiar de mudança significativa no argumento `limiar` no arquivo main.py.
3. Execute o arquivo main.py para gerar o gráfico dos dados fornecidos.

## Exemplo

### python climate_data.csv está dentro do repositório como um exemplo de dados

### Este exemplo irá detectar mudanças significativas na temperatura usando um limiar de 2 graus Celsius.

## Exemplo de Gráfico Gerado

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
