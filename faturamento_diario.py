import json
import pandas as pd

def ler_json(arq_json):
    with open(arq_json, 'r', encoding='utf8') as f:
        return json.load(f)

def ler_semana(semana):
    # le o arquivo .json e jogar na variável 'data'
    data = ler_json('semana.json')

    # pega as chaves de dentro de 'semanas' e jogar na variável 'keys'
    keys = data['semana'][semana].keys()

    # pega os de dentro de 'semanas' e jogar na variável 'values'
    values = data['semana'][semana].values()

    # cria a tabela em um dataframe
    df = pd.DataFrame(values, index=keys, columns=['semana'])
    df
    return df

#colocando semanas nas variaveis e tirando os valores = 0
semana_1 = ler_semana(0).query('semana > 0').rename({'semana': 'semana1'}, axis = 1)
semana_2 = ler_semana(1).query('semana > 0').rename({'semana': 'semana2'}, axis = 1)
semana_3 = ler_semana(2).query('semana > 0').rename({'semana': 'semana3'}, axis = 1)
semana_4 = ler_semana(3).query('semana > 0').rename({'semana': 'semana4'}, axis = 1)

# Concatenando semanas
df_mes = pd.concat([semana_1, semana_2,semana_3,semana_4], axis=1).round(2)

# media do mes por semana
df_media_semana = df_mes.groupby(['mes','mes','mes','mes'], axis=1).mean()

#media do faturamento no mês
df_mes_med = df_mes.describe().round(2).loc[['mean']].groupby(['mes','mes','mes','mes'], axis=1).mean().values.tolist()

#dia com faturamento menor no mês
df_mes_min = df_mes.describe().round(2).loc[['min']].groupby(['mes','mes','mes','mes'], axis=1).min().values.tolist()

#dia com maior faturamento no mês
df_mes_max = df_mes.describe().round(2).loc[['max']].groupby(['mes','mes','mes','mes'], axis=1).max().values.tolist()

#criando uma função para tirar as listas dentro de uma lista.
def lista_unica(lista):
    if isinstance(lista, list):
        return [sub_elem for elem in lista for sub_elem in lista_unica(elem)]
    else:
        return [lista]

#colocando os valores de cada dia do mês numa lista e convertendo para uma lista unica.
df_mes = df_mes.values.tolist()

#convertendo para uma lista unica:
df_mes = lista_unica(df_mes)
df_mes_med = lista_unica(df_mes_med)
df_mes_min = lista_unica(df_mes_min)
df_mes_max = lista_unica(df_mes_max)

#lista para armazenar contagem de dias que a media foi maior que a media mensal
quant_dias = []

#contando quantos dias a media diaria foi mairo que a media mensal.
for i in df_mes:
    if i > df_mes_med[0]:
        df_mes.count(df_mes[0])
        df_mes.count(df_mes[0])
        quant_dias.append(df_mes.count(df_mes[0]))

# quantidade de dias em que a média diaria foi maior que a mensal:
quantidade = (len(quant_dias))

#conclusão
print(f"quantidade de dias em que a média diaria foi maior que a mensal: {quantidade}")
print(f"maior faturamento em um dia do mês: {df_mes_max}")
print(f"menor faturamento em um dia do mês: {df_mes_min}")








