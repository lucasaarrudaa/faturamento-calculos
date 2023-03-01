import json
import pandas as pd


def ler_json(arq_json):
    with open(arq_json, 'r', encoding='utf8') as f:
        return json.load(f)

def ler_semana(semana, nome):
    # le o arquivo .json e jogar na variável 'data'
    data = ler_json('./Faturamento_calculos/semana.json')

    # pega as chaves de dentro de 'semanas' e joga na variável 'keys'
    keys = data['semana'][semana].keys()

    # pega os de dentro de 'semanas' e jogar na variável 'values'
    values = data['semana'][semana].values()

    # cria a tabela em um dataframe sem números = 0
    df = pd.DataFrame(values, index=keys, columns=['semana']).query('semana > 0')
    df.rename({'semana': f'semana{nome}'}, axis = 1)
    return df

# Concatenando semanas
df_mes = pd.concat([(ler_semana(0, 1)), (ler_semana(1, 2)), (ler_semana(2, 3)),(ler_semana(3, 4))], axis=1).round(2)

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

#lista para armazenar contagem de dias que a media foi maior que a media mensal
quant_dias = []

#contando quantos dias a media diaria foi maior que a media mensal (convertida para lista unica).
for i in df_mes:
    if i > df_mes_med[0]:
        df_mes.count(df_mes[0])
        df_mes.count(df_mes[0])
        quant_dias.append(lista_unica(df_mes).count(lista_unica(df_mes)[0]))

# quantidade de dias em que a média diaria foi maior que a mensal:
quantidade = (len(quant_dias))

#conclusão
print(f"quantidade de dias em que a média diaria foi maior que a mensal: {quantidade}")
print(f"maior faturamento em um dia do mês: {lista_unica(df_mes_max)}")
print(f"menor faturamento em um dia do mês: {lista_unica(df_mes_min)}")








