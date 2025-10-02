#                                   Atividade Avaliativa de Web Scraping
#
#                                               Felipe Schafhauser Lubke
#                                                           GRR 20233918
#                                       2023-Set-30 · Curitiba/PR/Brasil
# -----------------------------------------------------------------------

#-----------------------------------------------------------------------
#########################################################
#mportar pacotes utilizados e definições iniciais
#########################################################

#Importa os pacotes que vão ser utilizados

import requests
from bs4 import BeautifulSoup
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import statistics
from scipy.stats import ttest_ind




#Define uma url para ser acessada
url = 'https://fbref.com/pt/comps/24/Serie-A-Estatisticas'
#Cabeçalhos HTTP para simular um navegador
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36'}
#Faz o requerimento da url
r=requests.get(url, headers=headers)
#Printa o código obtido após acessar a página
print("Código de acesso para a página:", r.status_code)
#Cria um objeto BeautifulSoup a partir do requerimento
soup = BeautifulSoup(r.text, 'html.parser')

#########################################################
#Scraping da primeira tabela com resultados gerais
#########################################################

#Encontrar a tabela no HTML usando o ID e procurar o seu "corpo"
soup_tabela = soup.find('table', id="results2023241_overall").find_all('tbody')
#cria uma lista para receber as equipes
lista_equipes = []
#Iteração sobre as linhas da tabela localizada anteriormente procurando os elementos "tr"
for equipe in soup_tabela[0].find_all('tr'):
    #Cria um dicionario para receber as equipes e seus dados
    dict_equipe = {}
    #Obtem os valores que contem "th" e seja um "data-stat" e adicionan ao dicionario criado anteriormente
    dict_equipe[equipe.find('th').get('data-stat')] = equipe.find('th').getText()
    #Iteração sobre as colunas de informações que cotem "td"
    for info in equipe.find_all('td'):
        #Obtem o nome da coluna a partir do atributo "data-stat" e seu valor correspondente
        dict_equipe[info.get('data-stat')] = info.getText()
    #Adcionando as informações de nome de coluna a lista
    lista_equipes.append(dict_equipe)
#Cria um Data Fram a partir da lista usando pandas
df_total = pd.DataFrame(lista_equipes)
print("Tabela Geral bruta:\n", df_total)
#retira as colunas que não seram nescessarias
df_total = df_total.drop(["last_5", "top_team_scorers", "top_keeper", "notes"], axis=1)
#Troca virugla por ponto, mantendo apenas um padrão na tabela
df_total = df_total.replace({',': '.'}, regex=True)
print("Tabela de posições Geral:\n", df_total)
#Altera a tabela para numerico, exceto onde tem a colocação e os nomes
for col in df_total.columns[2:len(df_total.columns)]:
    df_total[col] = pd.to_numeric(df_total[col], errors="coerce")
#Verifica se esta faltando valores na tabela
missing_total = df_total.isnull().sum()
print("Verificando dados faltando:\n", missing_total)
#Descrição das variaveis
describe_total = df_total.describe()
print("Dados descritivos:\n", describe_total)
#Retorna as médias das colunas
mean_hgf=df_total["goals_for"].mean()
print("média de gols é:", mean_hgf)
print(df_total.to_markdown(index=False)) #aqui precisa ter o pacote "tabulate" instalado


#########################################################
#Scraping da segunda tabela com resultados Casa X Visitantes
#########################################################

#Encontrar a tabela no HTML usando o ID e procurar o seu "corpo"
soup_tabela = soup.find('table', id="results2023241_home_away").find_all('tbody')
#cria uma lista para receber as equipes
lista_equipes = []
#Iteração sobre as linhas da tabela localizada anteriormente procurando os elementos "tr"
for equipe in soup_tabela[0].find_all('tr'):
    #Cria um dicionario para receber as equipes e seus dados
    dict_equipe = {}
    #Obtem os valores que contem "th" e seja um "data-stat" e adicionan ao dicionario criado anteriormente
    dict_equipe[equipe.find('th').get('data-stat')] = equipe.find('th').getText()
    #Iteração sobre as colunas de informações que cotem "td"
    for info in equipe.find_all('td'):
        #Obtem o nome da coluna a partir do atributo "data-stat" e seu valor correspondente
        dict_equipe[info.get('data-stat')] = info.getText()
    #Adcionando as informações de nome de coluna a lista
    lista_equipes.append(dict_equipe)
#Cria um Data Fram a partir da lista usando pandas
df_ha = pd.DataFrame(lista_equipes)
print("Tabela Fora vs Casa bruta:\n", df_ha)
#Troca virugla por ponto, mantendo apenas um padrão na tabela
df_ha = df_ha.replace({',': '.'}, regex=True)
#Altera a tabela para numerico, exceto onde tem a colocação e os nomes
for col in df_ha.columns[2:len(df_ha.columns)]:
    df_ha[col] = pd.to_numeric(df_ha[col], errors="coerce")
missing_ha = df_ha.isnull().sum()
print("Verificando dados faltando:\n", missing_ha)
#Descrição das variaveis
describe_ha = df_ha.describe()
print("Dados descritivos fora vs casa:\n", describe_ha)
print(df_ha.to_markdown(index=False))


#########################################################
#Juntando as tabelas
#########################################################
#junta os dois data frames em um só
df=df_total.merge(df_ha)
missing = df.isnull().sum()
print("Verificando dados faltando:\n", missing)
#Descrição das variaveis
describe = df.describe()
print("Dados descritivos:\n", describe)
print(df.to_markdown(index=False))

#########################################################
#Outros Ajustes
#########################################################

# Define o "rank" como numerico para poder gerar analises
df[["rank"]] = df[["rank"]].apply(pd.to_numeric)
# altera a base para uma base empilhada com os valores de vitórias em casa e fora
# dfm_ha = df.melt('team', value_vars=["home_points","home_wins",'away_points','away_wins'], var_name='cols', value_name='vals')


#########################################################
#Análise Exploratória
#########################################################

mean_vf=df["away_wins"].mean()
mean_vc=df["home_wins"].mean()
mean_v=df["wins"].mean()
print("média de vitorias fora é:",mean_vf)
print("média de vitorias em casa é:",mean_vc)
print("média de vitorias é:",mean_v)
mean_ec=df["home_ties"].mean()
mean_ef=df["away_ties"].mean()
mean_e=df["ties"].mean()
print("média de empates fora é:",mean_ef)
print("média de empates em casa é:",mean_ec)
print("média de empates é:",mean_e)
mean_pc=df["home_points"].mean()
mean_pf=df["away_points"].mean()
mean_p=df["points"].mean()
print("média de pontos fora é:",mean_pf)
print("média de pontos em casa é:",mean_pc)
print("média de pontos é:",mean_p)

df[["wins","home_wins","away_wins"]].describe()
df[["wins","home_wins","away_wins"]].mode()

np.corrcoef(df["rank"],df["home_wins"])
np.corrcoef(df["rank"],df["away_wins"])

#verifica a quantidade de times acima da média
print("Acima da média Vitórias:",sum(i > mean_v for i in df["wins"]))
print("Acima da média Vitórias em Casa:",sum(i > mean_vc for i in df["home_wins"]))
print("Acima da média Vitórias Fora:",sum(i > mean_vf for i in df["away_wins"]))



#verificando quais são os times com mais vitorias fora e em casa

df_vf=df.groupby("team")["away_wins"].mean().sort_values(ascending = False)
df_vc=df.groupby("team")["home_wins"].mean().sort_values(ascending = False)
df[["rank","team","home_wins","away_wins"]]

#verificando quais são os times com mais pontos fora e em casa

df_pf=df.groupby("team")["away_points"].mean().sort_values(ascending = False)
df_pc=df.groupby("team")["home_points"].mean().sort_values(ascending = False)
df[["rank","team","home_points","away_points"]]



#plotar
# Define o tema para os gráficos
sns.set_theme(style="darkgrid")
# df.plot(xlabel="Posição",ylabel="Pontos",x="rank",y=["home_points","away_points"],title="Posição X Pontos")

plt.rcParams["figure.figsize"] = (8, 8)
df.plot(xlabel="Posição",ylabel="Vitórias",x="rank",y=["home_wins","away_wins"],title="Posição X Vitórias")
sns.regplot(data=df, x="rank",y="wins",scatter=False, order=2,ci=None, color="black")
sns.regplot(data=df, x="rank",y="home_wins",scatter=False, order=2,ci=None, color="blue")
sns.regplot(data=df, x="rank",y="away_wins",scatter=False, order=2,ci=None, color="orange")
plt.hlines(y=mean_v, xmin=0, xmax=20, color='black', alpha=1, linewidth=1, linestyles='dotted')
plt.hlines(y=mean_vc, xmin=0, xmax=20, color='blue', alpha=1, linewidth=1, linestyles='dotted')
plt.hlines(y=mean_vf, xmin=0, xmax=20, color='orange', alpha=1, linewidth=1, linestyles='dotted')
plt.legend(loc='upper right', labels=['Vitórias Casa',"Vitórias Fora","Regressão Casa","Regressão Fora","Média de vitórias em casa"])
plt.title('Posição X Vitórias', loc='center')
plt.xlabel('Posição')
plt.ylabel("Número de Vitórias")

plt.rcParams["figure.figsize"] = (8, 8)
sns.lineplot(data=df, x="rank",y="home_points", color="blue",ci=None)
sns.lineplot(data=df, x="rank",y="away_points", color="orange",ci=None)
plt.hlines(y=mean_pc, xmin=0, xmax=20, color='blue', alpha=1, linewidth=1, linestyles='dotted')
plt.hlines(y=mean_pf, xmin=0, xmax=20, color='orange', alpha=1, linewidth=1, linestyles='dotted')
plt.legend(loc='upper right', labels=['Pontos Casa',"Pontos Fora","Média de Pontos"])
plt.title('Posição X Vitórias', loc='center')
plt.xlabel('Posição')
plt.ylabel("Número de Pontos")


## Gráfico comparando a pontuação

# Cria listas para receber os valores
position = list(range(1, 21))
hpoints = []
apoints = []
tpoints = []

# Calcula a média de pontos de cada time
for i in range(20):
    tpoints.append(statistics.mean(df['points'][i::20]))
    hpoints.append(statistics.mean(df['home_points'][i::20]))
    apoints.append(statistics.mean(df['away_points'][i::20]))

# Cria um dataframe das listas
frame = {'Rank': position, 'home_points': hpoints, 'away_points': apoints, 'points': tpoints}
df_avg = pd.DataFrame(frame)

## Cria o gráfico com disperção de pontuação para a média de pontos do campeonato

plt.rcParams["figure.figsize"] = (11, 8)
df_avg = df_avg.sort_values(by='points')
my_range=range(1,len(df_avg.index)+1)
plt.hlines(y=my_range, xmin=df_avg['home_points'], xmax=df_avg['away_points'], color='grey', alpha=0.4)
plt.scatter(df_avg['away_points'], my_range, color='navy', alpha=1, label='Pontos Fora')
plt.scatter(df_avg['home_points'], my_range, color='gold', alpha=0.8, label='Pontos em Casa')
plt.legend()

# Cria as linhas verticais
plt.vlines(x=0, ymin=0, ymax=26, color='black', alpha=1, linewidth=1, linestyles='dotted')
plt.vlines(x=10, ymin=0, ymax=26, color='black', alpha=1, linewidth=1, linestyles='dotted')
plt.vlines(x=20, ymin=0, ymax=26, color='black', alpha=1, linewidth=1, linestyles='dotted')
plt.vlines(x=30, ymin=0, ymax=26, color='black', alpha=1, linewidth=1, linestyles='dotted')
plt.vlines(x=40, ymin=0, ymax=26, color='black', alpha=1, linewidth=1, linestyles='dotted')
plt.vlines(x=50, ymin=0, ymax=26, color='black', alpha=1, linewidth=1, linestyles='dotted')

# Adiciona titulos e legendas
plt.yticks(my_range, df.sort_values(by="points")['team'])
#plt.yticks(my_range, list(range(20, 0, -1)))
plt.title('Pontos de cada time no campeonato brasileiro 2023', loc='center')
plt.xlabel('Número de Pontos')

#########################################################
#Teste A/B
#########################################################

# Definindo qual vai ser a versão A e B
version_A = df["home_points"]
version_B = df["away_points"]
# Gerando dados dos testes
t, p = ttest_ind(version_A, version_B)
print(f"t = {t:.3f}")
print(f"p = {p:.3f}")
mean_A = np.mean(version_A)
mean_B = np.mean(version_B)

#Gerando o gráfico para comparar
plt.hist(version_A, alpha=0.5, label='Pontos Casa')
plt.hist(version_B, alpha=0.5, label='Pontos Fora')
plt.axvline(mean_A, color='r', linestyle='dashed', linewidth=1)
plt.axvline(mean_B, color='b', linestyle='dashed', linewidth=1)
plt.legend(loc='upper left', labels=['Pontos Casa',"Pontos Fora","Média de Pontos"])
plt.show()