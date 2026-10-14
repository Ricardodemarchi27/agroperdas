AgroPerdas — Calculadora de Perdas na Colheita

1. Sobre o projeto

O AgroPerdas é um sistema desenvolvido em Python para estimar as perdas financeiras causadas por perdas na colheita de cana-de-açúcar.

O agronegócio possui grande importância econômica, e a redução de desperdícios pode contribuir para melhorar a eficiência das operações agrícolas. O sistema busca ajudar o usuário a compreender o impacto das perdas na produção e no resultado financeiro.

2. Problema identificado

Durante a colheita mecanizada da cana-de-açúcar, parte da matéria-prima pode ser perdida. Essas perdas representam redução na quantidade de produto aproveitável e podem causar prejuízos financeiros.

O desafio é calcular a quantidade estimada de cana perdida e o valor financeiro correspondente, utilizando informações básicas da operação.

3. Solução proposta

O AgroPerdas recebe quatro informações:

Área plantada, em hectares;

Produtividade estimada, em toneladas por hectare;

Percentual de perdas;

Preço estimado por tonelada.

Com esses dados, o sistema calcula a produção esperada, as toneladas perdidas e o prejuízo financeiro estimado. Também classifica as perdas como baixas, moderadas ou altas, conforme as faixas definidas no código.

4. Funcionalidades

Cálculo da produção esperada;

Cálculo das toneladas perdidas;

Estimativa do prejuízo financeiro;

Classificação do percentual de perdas;

Validação dos dados informados;

Exibição dos resultados no terminal;

Registro dos resultados em arquivos JSON e TXT;

Uso de estruturas de dados em Python.

5. Tecnologias utilizadas

Python;

PyCharm;

Arquivos TXT;

Arquivos JSON;

GitHub para versionamento e entrega do código.

6. Como executar

Instale o Python no computador.

Baixe ou clone este repositório.

Abra a pasta do projeto no PyCharm.

Execute o arquivo main.py.

Siga as instruções exibidas no terminal.

Os arquivos de histórico e relatório são utilizados para registrar os resultados gerados pelo programa.

7. Exemplo de utilização

Dados informados:

Área plantada: 100 hectares;

Produtividade: 150 toneladas por hectare;

Percentual de perdas: 12%;

Preço por tonelada: R$ 11,00.

Resultado esperado:

Produção esperada: 15.000 toneladas;

Produção perdida: 1.800 toneladas;

Prejuízo estimado: R$ 19.800,00;

Classificação das perdas: Alta.

8. Limitações e melhorias futuras

O sistema utiliza valores informados pelo usuário e produz estimativas. Os resultados dependem da qualidade dos dados inseridos.

Como melhorias futuras, podem ser incluídos gráficos, comparação entre diferentes períodos, recomendações de redução de perdas e integração com banco de dados Oracle.

9. Autor

Projeto acadêmico desenvolvido individualmente para atividade da FIAP.
