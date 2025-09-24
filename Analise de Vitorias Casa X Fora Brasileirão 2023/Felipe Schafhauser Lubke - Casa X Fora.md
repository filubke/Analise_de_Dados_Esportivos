#  Analise da performance de jogos em Casa vs Fora


                                                    Felipe Schafhauser Lubke
                                                   
                                                    03-Dez-2023 · Curitiba/PR/Brasil



<!-- TOC -->

* [Analise da performance de jogos em Casa vs Fora](#analise-da-performance-de-jogos-em-casa-vs-fora)\
      * [Introdução](#introdução)\
      * [Os dados](#os-dados)\
      * [Metodologia](#metodologia)\
      * [Análise Exploratória](#análise-exploratória)\
      * [Teste A/B](#teste-ab)\
      * [Conclusões](#conclusões)\
      * [Recomendações e próximos passos](#recomendações-e-próximos-passos)\
      * [Tabelas](#tabelas)\
      * [Glossário](#glossário)
 
<!-- TOC -->


#### Introdução
O futebol é um esporte dinâmico, com vários fatores afetando o jogo de diversas formas e uma das que mais se fala é em relação ao fator "casa", mas será mesmo que temos uma grande predominância no aspecto casa, ou isso se aplica apenas para alguns times ou momentos?


#### Os dados
Foi selecionado o site https://fbref.com/, para ser feito o web scraping, o motivo de sua seleção foi a variedade de dados contidos e não ser um site fechado para a captura dos dados, inicialmente foi selecionado a tabela de dados gerais, como vitórias, empates, gols a favor e contra, além de algumas outras métricas já fornecidas pelo site, outra tabela selecionado foi a diferença entre os jogos em casa e fora, que também incluem os mesmos dados citados anteriormente. 
Os dados foram coletados no incio da 37 rodada de 2023, faltando 2 rodadas para finalizar o campeonato e pode ser refeito assim que o campeonato acabar.

#### Metodologia 
O ambiente utilizado para trabalhar com o Python foi o PyCharm C.E., com os pacotes, "requests", "BeautifulSoup", "statistics", "numpy", "scipy", "pandas" e "seaborn".
Com os dados já coletados, foi iniciado um processo de pré-visualização e higienização desses dados, esse processo se deu para poder eliminar colunas que não seriam utilizados e corrigir possíveis problemas identificados.
Esse processo foi realizado para nas duas extrações realizadas, a primeira extração com os dados de classificação dos times sem levar em conta nenhuma segmentação, a segunda extração contendo os mesmos dados sendo segmentados por jogos em casa e fora. Os dados contidos nas tabelas podem ser conferidos no Glossário.
Todas as colunas retiradas e ajustes realizados podem ser acompanhados no decorrer do código.


#### Análise Exploratória
Após o processo de scpraing e higienização do data-frame, pode-se verificar alguns insights para progredir com a análise. 
Inicialmente o principal foco do estudo é a diferença entre a quantidade vitórias comparando com a posição do time, foi tomado esse ponto de partida para entender se temos nos times mais bem posicionados um valor maior nesse indicador. 
Com uma comparação descritiva entre vitórias, temos que a variação de vitórias em casa é a menor, outra questão é a média de vitórias, temos 9 times acima da média para vitórias em casa e fora de casa. 
Enquanto fora de casa se tem 5 vitórias em média no campeonato, em casa temos 8 vitórias, 3 vitórias a menos, e ao relacionar com a colocação do time percebemos que, os 11 primeiros times mais bem posicionados estão acima da média de vitórias em casa, mas em relação a vitórias fora temos um comportamento diferente, times em diferentes posições estão acima da média.

**Posição X Vitórias**\
<img src="D:\Estatistica\Python para Dados\Trabalho de Análise de Dados\Imagens\Posição X Vitórias.png" title="Posição X Vitórias"/>\
A vitórias em caem após a 11° posição, enquanto as fora de casa variam mais.

Aplicamos uma regressão de ordem 2 para entender melhor o comportamento dos dados, e percebemos de forma visual que as vitórias em casa realmente têm uma declividade bem mais acentuada que em relação a vitórias fora.
Com as vitórias de casa tendo um desvio de 4 temos uma variabilidade bem maior já que as vitórias fora de casa têm desvio de 2, assim fica mais claro que vencer em casa acaba sendo um diferencial.
Outro ponto analisado para colaborar com a importância de vencer em casa é a correlação de -0,84 com a posição, a correlação das vitórias fora com a posição é de -0,57.

**Posição X Vitórias com Regressão**\
<img src="D:\Estatistica\Python para Dados\Trabalho de Análise de Dados\Imagens\Posição X Vitórias (regressão).png" title="Posição X Vitórias"/>\
Com maior variabilidade a regressão de vitórias em casa tem uma declividade bem mais acentuada.


Fizemos as mesmas analises considerando a pontuação, afim de verificar se temos o empate com um fator decisivo ou que possa alterar a dinâmica já observada.
De início o que já chama atenção é que a variação, quando olhamos apenas em casa, a pontuação tem 8,7 enquanto vitórias tem 8,3. Ao olhar fora de casa, a variação muda mais, pontuação tem 6,5 e vitórias tem 5.
Outro padrão também já identificado é que os 11 primeiros times mais bem posicionados estão acima da média de pontos em casa, e em relação a pontos fora temos o mesmo comportamento de diferentes posições estarem acima da média.

**Posição X Pontos**\
<img src="D:\Estatistica\Python para Dados\Trabalho de Análise de Dados\Imagens\Posição X Pontos.png" title="Posição X Pontos"/>\
Da mesma forma que o gráfico anterior, temos o mesmo comportamento que as vitórias, demonstrando que empates não são um bom resultado.

Trazendo o time de forma individual, mas ainda categorizado por sua classificação, vemos o quão predominante é a pontuação em casa para os primeiros colocados, de forma que alguns times como o Fluminense e o São Paulo são 2 dos 3 priores times fora de casa e são o melhor e 4° melhor, respectivamente, pontuando em casa, por conta disso conseguiram ainda ficar na metade de cima da tabela.

**Pontos por Time**\
<img src="D:\Estatistica\Python para Dados\Trabalho de Análise de Dados\Imagens\Pontos por time.png" title="Pontos por Time"/>\
Da metade para baixo do gráfico não temos times com mais de 30 pontos conquistados em casa, mas da metade para cima temos alguns times com menos de 20 pontos conquistados fora de casa.

#### Teste A/B
Vamos utilizar o teste A/B para confirmar a hipótese de que os jogos em casa geram mais pontos, para isso vamos ter a versão A sendo pontos em casa e a versão B sendo pontos fora de casa. 
Com isso temos o valor de p em 0, indicando que foi observado diferenças estatísticas entre as duas versões testadas, pontos em casa e pontos fora.
O valor positivo de t, indica que a versão A (pontos em casa) é estatisticamente superior a versão B (pontos fora de casa), como o valor de t ficou em 3,9, temos que é provável que seja estatisticamente significativo.

**Teste A/B**\
<img src="D:\Estatistica\Python para Dados\Trabalho de Análise de Dados\Imagens\Teste AB.png" title="Teste A/B"/>\


##### Conclusões
O time precisa corresponder em casa para evitar posições muito inferiores na tabela, ao menos ficar próximo da média da pontuação e para isso ocorrer é necessário que os jogos sejam ganhos, o empate em si não traz tantos benefícios para compor a pontuação, mas é claro que acaba colaborando como um todo no resultado final mas nunca deve ser o objetivo.
Fora de casa é um desafio para todos os times, mas fica claro que para disputar as primeiras colocações é necessário ter uma excelente performance. 


##### Recomendações e próximos passos
* Analisar os times de forma individual; 
* Analisar a capacidade do estádio;
* Analisar média de público;
* Correlacionar a média de público com a performance do adversário;
* Analisar distância viajada para jogar;
* Analisar distância a data da viagem para jogar;

<details>

<summary>Tabelas</summary>

### Tabelas    

**Dados Gerais**

| rank | team            |  games |  wins  |  ties |  losses  |  goals_for  |  goals_against  |  goal_diff  |  points  |  points_avg  |  xg_for  |   xg_against |   xg_diff |   xg_diff_per90 |   attendance_per_g |
|:-----|:----------------|:------:|:------:|:-----:|:--------:|:-----------:|:---------------:|:-----------:|:--------:|:------------:|:--------:|-------------:|----------:|----------------:|-------------------:|
|      1 | Palmeiras        |      36 |     19 |      9 |        8 |          62 |              32 |          30 |       66 |         1.83 |     53.8 |         37.4 |      16.4 |            0.45 |             22.044 |
|      2 | Atlético Mineiro |      37 |     19 |      9 |        9 |          51 |              28 |          23 |       66 |         1.78 |     45.5 |         39.4 |       6.2 |            0.17 |             15.02  |
|      3 | Botafogo (RJ)    |      36 |     18 |      9 |        9 |          57 |              34 |          23 |       63 |         1.75 |     48.8 |         46.7 |       2.1 |            0.06 |             23.354 |
|      4 | Flamengo         |      36 |     18 |      9 |        9 |          54 |              40 |          14 |       63 |         1.75 |     47.9 |         43.7 |       4.1 |            0.11 |             36.569 |
|      5 | Grêmio           |      36 |     19 |      5 |       12 |          59 |              54 |           5 |       62 |         1.72 |     46.8 |         52.1 |      -5.3 |           -0.15 |             21.667 |
|      6 | Bragantino       |      36 |     16 |     11 |        9 |          47 |              33 |          14 |       59 |         1.64 |     54.9 |         40.7 |      14.2 |            0.39 |              3.283 |
|      7 | Fluminense       |      36 |     16 |      8 |       12 |          49 |              43 |           6 |       56 |         1.56 |     47.6 |         43.9 |       3.7 |            0.1  |             22.297 |
|      8 | Ath Paranaense   |      36 |     13 |     14 |        9 |          48 |              40 |           8 |       53 |         1.47 |     49.2 |         43.4 |       5.8 |            0.16 |             14.091 |
|      9 | Internacional    |      37 |     14 |     10 |       13 |          43 |              44 |          -1 |       52 |         1.41 |     41   |         46.7 |      -5.8 |           -0.16 |             10.628 |
|     10 | São Paulo        |      37 |     13 |     11 |       13 |          39 |              38 |           1 |       50 |         1.35 |     48.5 |         36.2 |      12.3 |            0.33 |             24.678 |
|     11 | Fortaleza        |      36 |     13 |      9 |       14 |          42 |              43 |          -1 |       48 |         1.33 |     49.1 |         42.4 |       6.7 |            0.19 |             22.869 |
|     12 | Cuiabá           |      36 |     13 |      9 |       14 |          36 |              37 |          -1 |       48 |         1.33 |     35.4 |         39.7 |      -4.4 |           -0.12 |              8.109 |
|     13 | Corinthians      |      37 |     11 |     14 |       12 |          45 |              48 |          -3 |       47 |         1.27 |     39.5 |         48.8 |      -9.2 |           -0.25 |             24.253 |
|     14 | Cruzeiro         |      36 |     11 |     12 |       13 |          34 |              31 |           3 |       45 |         1.25 |     45.4 |         39.4 |       6   |            0.17 |             15.14  |
|     15 | Santos           |      36 |     11 |     10 |       15 |          38 |              59 |         -21 |       43 |         1.19 |     40.6 |         48.9 |      -8.3 |           -0.23 |              5.688 |
|     16 | Vasco da Gama    |      36 |     11 |      9 |       16 |          39 |              49 |         -10 |       42 |         1.17 |     45.2 |         44.7 |       0.6 |            0.02 |             15.319 |
|     17 | Bahia            |      36 |     11 |      8 |       17 |          44 |              49 |          -5 |       41 |         1.14 |     45.4 |         49   |      -3.6 |           -0.1  |             26.643 |
|     18 | Goiás            |      36 |      8 |     11 |       17 |          35 |              52 |         -17 |       35 |         0.97 |     35.3 |         43.9 |      -8.6 |           -0.24 |              6.695 |
|     19 | Coritiba         |      36 |      8 |      6 |       22 |          41 |              70 |         -29 |       30 |         0.83 |     38.3 |         57.9 |     -19.5 |           -0.54 |             10.428 |
|     20 | América (MG)     |      36 |      4 |      9 |       23 |          39 |              78 |         -39 |       21 |         0.58 |     44.8 |         58.2 |     -13.3 |           -0.37 |              2.375 |

**Dados Casa**

| rank   | team             |  home_games  |  home_wins  |  home_ties  |  home_losses  |  home_goals_for  |  home_goals_against  |  home_goal_diff  |  home_points  |  home_points_avg  |  home_xg_for  |  home_xg_against  |  home_xg_diff  |  home_xg_diff_per90  |
|:-------|:-----------------|:------------:|:-----------:|:-----------:|:-------------:|:----------------:|:--------------------:|:----------------:|:-------------:|:-----------------:|:-------------:|:-----------------:|:--------------:|:--------------------:|
|      1 | Palmeiras        |           18 |          13 |           2 |             3 |               34 |                   12 |               22 |            41 |              2.28 |          33.6 |              11.5 |           22.2 |                 1.23 |
|      2 | Atlético Mineiro |           19 |          11 |           3 |             5 |               28 |                   16 |               12 |            36 |              1.89 |          25.1 |              18   |            7.1 |                 0.37 |
|      3 | Botafogo (RJ)    |           18 |          11 |           3 |             4 |               36 |                   17 |               19 |            36 |              2    |          32.3 |              18.6 |           13.7 |                 0.76 |
|      4 | Flamengo         |           18 |           9 |           5 |             4 |               24 |                   15 |                9 |            32 |              1.78 |          25.5 |              20.8 |            4.7 |                 0.26 |
|      5 | Grêmio           |           18 |          13 |           2 |             3 |               33 |                   16 |               17 |            41 |              2.28 |          25.2 |              17.9 |            7.3 |                 0.4  |
|      6 | Bragantino       |           18 |          10 |           5 |             3 |               27 |                   14 |               13 |            35 |              1.94 |          32.8 |              17   |           15.9 |                 0.88 |
|      7 | Fluminense       |           18 |          13 |           4 |             1 |               31 |                   15 |               16 |            43 |              2.39 |          26.2 |              15.5 |           10.7 |                 0.59 |
|      8 | Ath Paranaense   |           18 |           9 |           8 |             1 |               30 |                   19 |               11 |            35 |              1.94 |          31.5 |              18.3 |           13.2 |                 0.74 |
|      9 | Internacional    |           18 |           8 |           5 |             5 |               27 |                   20 |                7 |            29 |              1.61 |          23.8 |              20.2 |            3.6 |                 0.2  |
|     10 | São Paulo        |           18 |          12 |           3 |             3 |               28 |                   13 |               15 |            39 |              2.17 |          29.5 |              13.6 |           15.8 |                 0.88 |
|     11 | Fortaleza        |           18 |           8 |           6 |             4 |               27 |                   20 |                7 |            30 |              1.67 |          31.3 |              17.2 |           14.2 |                 0.79 |
|     12 | Cuiabá           |           18 |           5 |           6 |             7 |               20 |                   22 |               -2 |            21 |              1.17 |          20.3 |              19.2 |            1.1 |                 0.06 |
|     13 | Corinthians      |           19 |           6 |          10 |             3 |               26 |                   23 |                3 |            28 |              1.47 |          24.5 |              20.4 |            4.1 |                 0.21 |
|     14 | Cruzeiro         |           18 |           4 |           7 |             7 |               13 |                   16 |               -3 |            19 |              1.06 |          25.1 |              16.8 |            8.3 |                 0.46 |
|     15 | Santos           |           18 |           6 |           7 |             5 |               25 |                   26 |               -1 |            25 |              1.39 |          24.2 |              19.7 |            4.5 |                 0.25 |
|     16 | Vasco da Gama    |           18 |           8 |           2 |             8 |               22 |                   22 |                0 |            26 |              1.44 |          27.9 |              19.1 |            8.8 |                 0.49 |
|     17 | Bahia            |           18 |           7 |           5 |             6 |               25 |                   20 |                5 |            26 |              1.44 |          25.7 |              20.2 |            5.5 |                 0.31 |
|     18 | Goiás            |           18 |           4 |           7 |             7 |               18 |                   25 |               -7 |            19 |              1.06 |          20.3 |              19   |            1.4 |                 0.08 |
|     19 | Coritiba         |           18 |           4 |           4 |            10 |               17 |                   26 |               -9 |            16 |              0.89 |          22.1 |              24.2 |           -2   |                -0.11 |
|     20 | América (MG)     |           18 |           4 |           2 |            12 |               18 |                   36 |              -18 |            14 |              0.78 |          24.6 |              24.3 |            0.3 |                 0.02 |


**Dados Visitantes**

|   rank | team             |   away_games |   away_wins |   away_ties |   away_losses |   away_goals_for |   away_goals_against |   away_goal_diff |   away_points |   away_points_avg |   away_xg_for |   away_xg_against |   away_xg_diff |   away_xg_diff_per90 |
|-------:|:-----------------|-------------:|------------:|------------:|--------------:|-----------------:|---------------------:|-----------------:|--------------:|------------------:|--------------:|------------------:|---------------:|---------------------:|
|      1 | Palmeiras        |           18 |           6 |           7 |             5 |               28 |                   20 |                8 |            25 |              1.39 |          20.2 |              26   |           -5.8 |                -0.32 |
|      2 | Atlético Mineiro |           18 |           8 |           6 |             4 |               23 |                   12 |               11 |            30 |              1.67 |          20.5 |              21.4 |           -0.9 |                -0.05 |
|      3 | Botafogo (RJ)    |           18 |           7 |           6 |             5 |               21 |                   17 |                4 |            27 |              1.5  |          16.5 |              28.1 |          -11.6 |                -0.64 |
|      4 | Flamengo         |           18 |           9 |           4 |             5 |               30 |                   25 |                5 |            31 |              1.72 |          22.4 |              22.9 |           -0.6 |                -0.03 |
|      5 | Grêmio           |           18 |           6 |           3 |             9 |               26 |                   38 |              -12 |            21 |              1.17 |          21.6 |              34.2 |          -12.6 |                -0.7  |
|      6 | Bragantino       |           18 |           6 |           6 |             6 |               20 |                   19 |                1 |            24 |              1.33 |          22.1 |              23.7 |           -1.7 |                -0.09 |
|      7 | Fluminense       |           18 |           3 |           4 |            11 |               18 |                   28 |              -10 |            13 |              0.72 |          21.4 |              28.4 |           -7   |                -0.39 |
|      8 | Ath Paranaense   |           18 |           4 |           6 |             8 |               18 |                   21 |               -3 |            18 |              1    |          17.6 |              25.1 |           -7.5 |                -0.41 |
|      9 | Internacional    |           19 |           6 |           5 |             8 |               16 |                   24 |               -8 |            23 |              1.21 |          17.1 |              26.5 |           -9.3 |                -0.49 |
|     10 | São Paulo        |           19 |           1 |           8 |            10 |               11 |                   25 |              -14 |            11 |              0.58 |          19   |              22.6 |           -3.6 |                -0.19 |
|     11 | Fortaleza        |           18 |           5 |           3 |            10 |               15 |                   23 |               -8 |            18 |              1    |          17.8 |              25.2 |           -7.5 |                -0.41 |
|     12 | Cuiabá           |           18 |           8 |           3 |             7 |               16 |                   15 |                1 |            27 |              1.5  |          15.1 |              20.6 |           -5.5 |                -0.3  |
|     13 | Corinthians      |           18 |           5 |           4 |             9 |               19 |                   25 |               -6 |            19 |              1.06 |          15.1 |              28.4 |          -13.3 |                -0.74 |
|     14 | Cruzeiro         |           18 |           7 |           5 |             6 |               21 |                   15 |                6 |            26 |              1.44 |          20.3 |              22.6 |           -2.3 |                -0.13 |
|     15 | Santos           |           18 |           5 |           3 |            10 |               13 |                   33 |              -20 |            18 |              1    |          16.4 |              29.2 |          -12.8 |                -0.71 |
|     16 | Vasco da Gama    |           18 |           3 |           7 |             8 |               17 |                   27 |              -10 |            16 |              0.89 |          17.3 |              25.5 |           -8.2 |                -0.46 |
|     17 | Bahia            |           18 |           4 |           3 |            11 |               19 |                   29 |              -10 |            15 |              0.83 |          19.7 |              28.8 |           -9.1 |                -0.51 |
|     18 | Goiás            |           18 |           4 |           4 |            10 |               17 |                   27 |              -10 |            16 |              0.89 |          15   |              24.9 |          -10   |                -0.55 |
|     19 | Coritiba         |           18 |           4 |           2 |            12 |               24 |                   44 |              -20 |            14 |              0.78 |          16.2 |              33.7 |          -17.5 |                -0.97 |
|     20 | América (MG)     |           18 |           0 |           7 |            11 |               21 |                   42 |              -21 |             7 |              0.39 |          20.3 |              33.9 |          -13.6 |                -0.76 |

**Comparativo de vitórias em casa e fora e sua pontuação**

| rank   | team             |  home_points  |  home_wins  |  away_points  |  away_wins  |
|:-------|:-----------------|:-------------:|:-----------:|:-------------:|:-----------:|
|      1 | Palmeiras        |            41 |          13 |            25 |           6 |
|      2 | Atlético Mineiro |            36 |          11 |            30 |           8 |
|      3 | Botafogo (RJ)    |            36 |          11 |            27 |           7 |
|      4 | Flamengo         |            32 |           9 |            31 |           9 |
|      5 | Grêmio           |            41 |          13 |            21 |           6 |
|      6 | Bragantino       |            35 |          10 |            24 |           6 |
|      7 | Fluminense       |            43 |          13 |            13 |           3 |
|      8 | Ath Paranaense   |            35 |           9 |            18 |           4 |
|      9 | Internacional    |            29 |           8 |            23 |           6 |
|     10 | São Paulo        |            39 |          12 |            11 |           1 |
|     11 | Fortaleza        |            30 |           8 |            18 |           5 |
|     12 | Cuiabá           |            21 |           5 |            27 |           8 |
|     13 | Corinthians      |            28 |           6 |            19 |           5 |
|     14 | Cruzeiro         |            19 |           4 |            26 |           7 |
|     15 | Santos           |            25 |           6 |            18 |           5 |
|     16 | Vasco da Gama    |            26 |           8 |            16 |           3 |
|     17 | Bahia            |            26 |           7 |            15 |           4 |
|     18 | Goiás            |            19 |           4 |            16 |           4 |
|     19 | Coritiba         |            16 |           4 |            14 |           4 |
|     20 | América (MG)     |            14 |           4 |             7 |           0 |




</details>


<details>
<summary>Glossário</summary>

### Glossário    

#### rank: ```Posição da equipe no campeonato```
##### team:```Nome do time``` 
##### games: ```Número de jogos feitos```
##### wins: ```Jogos ganhos```
##### ties: ```Jogos empatados```
##### losses: ```Jogos perdidos```
##### goals_for: ```Gols feitos```
##### goals_against: ```Gols sofridos```
##### goal_diff: ```Saldos de gols```
##### points: ```Número de pontos```
##### points_avg: ```Média de pontos por partida```
##### xg_for: ```Esperança do número de gols feitos```
##### xg_against: ```Esperança do número de gols sofridos``` 
##### xg_diff: ```Esperança do saldo de gols```
##### xg_diff_per90: ```Esperança do saldo de gols por 90'``` 
##### attendance_per_g: ```Média de público por partida```
##### home_games: ```Número de jogos em casa```
##### home_wins: ```Jogos ganhos em casa```
##### home_ties: ```Jogos empratados em casa```
##### home_losses: ```Jogos perdidos em casa```
##### home_goals_for: ```Gols feitos em casa```
##### home_goals_against: ```Gols sofridos em casa```
##### home_goal_diff: ```Saldo de gols em casa```
##### home_points: ```Número de pontos em casa```
##### home_points_avg: ```Média de pontos por partida em casa```
##### home_xg_for: ```Esperança do número de gols feitos em casa```
##### home_xg_against: ```Esperança do número de gols sofridos em casa```
##### home_xg_diff: ```Esperança do saldo de gols em casa```
##### home_xg_diff_per90 ```Esperança do saldo de gols de gols por  90' em casa```
##### away_games: ```Número de jogos fora```
##### away_wins: ```Jogos ganhos fora```
##### away_ties: ```Jogos empatados fora```
##### away_losses: ```Jogos perdidos fora```
##### away_goals_for: ```Gols feitos fora```
##### away_goals_against: ```Gols sofridos fora```
##### away_goal_diff: ```Saldo de gols fora```
##### away_points: ```Número de pontos fora```
##### away_points_avg: ```Média de pontos por partida fora```
##### away_xg_for: ```Esperança do número de gols feitos fora```
##### away_xg_against: ```Esperança do número de gols sofridos fora```
##### away_xg_diff: ```Esperança do saldo de gols fora```
##### away_xg_diff_per90: ```Esperança do saldo de gols de gols por 90' fora```

</details>

Referência bibliográfica

FBREF. **Série A estatísticas**. Disponível em: <https://fbref.com/pt/comps/24/Serie-A-Estatisticas>. Acesso em: 03 de Dez. de 2023 as 22:30.



