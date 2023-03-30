import pandas as pd 
import json 

class Faturamento:
    
    def __init__(self, arq_json):
        '''
        Parametros:
                arq_json é o caminho relativo do arquivo json.
        '''
        self.arq_json = arq_json
        self.data = self.ler_json()

    def ler_json(self):
        '''
        Lê o arquivo json
        '''
        with open(self.arq_json, 'r', encoding='utf8') as f:
            return json.load(f)
        
    def ler_semana(self, semana, nome):
        '''
        Le as semanas.
        '''
        # pega as chaves de dentro de 'semanas' e joga na variável 'keys'
        keys = self.data['semana'][semana].keys()

        # pega os de dentro de 'semanas' e jogar na variável 'values'
        values = self.data['semana'][semana].values()

        # cria a tabela em um dataframe sem números = 0
        self.df = pd.DataFrame(values, index=keys, columns=['semana']).query('semana > 0')
        self.df.rename({'semana': f'semana{nome}'}, axis = 1)
        return self.df

    def concatenar_semanas(self):
        '''
        Concatena as semanas, juntando tudo em um dataframe. 
        '''
        self.df_mes = pd.concat([(self.ler_semana(0, 1)), (self.ler_semana(1, 2)), (self.ler_semana(2, 3)),(self.ler_semana(3, 4))], axis=1).round(2)
        return self.df_mes

    def media_semana(self):
        '''
        Media do mes por semana
        '''
        df_media_semana = self.df_mes.groupby(['mes','mes','mes','mes'], axis=1).mean()
        return df_media_semana

    def media_faturamento_mes(self):
        '''
        Media do faturamento no mês
        '''
        self.df_mes_med = self.df_mes.describe().round(2).loc[['mean']].groupby(['mes','mes','mes','mes'], axis=1).mean().values.tolist()
        df_mes_med = self.df_mes_med
        return df_mes_med[0]

    def dia_faturamento_menor_mes(self):
        #dia com faturamento menor no mês
        self.df_mes_min = self.df_mes.describe().round(2).loc[['min']].groupby(['mes','mes','mes','mes'], axis=1).min().values.tolist()
        df_mes_min = self.df_mes_min
        return df_mes_min[0]

    def dia_faturamento_maior_mes(self):
        #dia com maior faturamento no mês
        self.df_mes_max = self.df_mes.describe().round(2).loc[['max']].groupby(['mes','mes','mes','mes'], axis=1).max().values.tolist()
        df_mes_max = self.df_mes_max
        return df_mes_max[0]

    def quantidade_media_maior_media_mensal(self):
        '''
        Retorna a quantidade de dias em que a média diaria foi maior que a mensal
        '''
        def lista_unica(lista):
            '''
            Criando uma função para tirar as listas dentro de uma lista.
            '''
            if isinstance(lista, list):
                return [sub_elem for elem in lista for sub_elem in lista_unica(elem)]
            else:
                return [lista]

        #colocando os valores de cada dia do mês numa lista e convertendo para uma lista unica.
        df_mes = self.df_mes.values.tolist()

        #lista para armazenar contagem de dias que a media foi maior que a media mensal
        quant_dias = []

        #contando quantos dias a media diaria foi maior que a media mensal (convertida para lista unica).
        for i in df_mes:
            if i > self.media_faturamento_mes():
                df_mes.count(df_mes[0])
                df_mes.count(df_mes[0])
                quant_dias.append(lista_unica(df_mes).count(lista_unica(df_mes)[0]))
        quantidade = (len(quant_dias))         
        return quantidade 