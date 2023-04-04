# Faturamento_calculos
Calculos dados de um faturamento mensal, semanal e diario.

Resumo dos objetivos: 

O projeto consistiu em analisar os dados de faturamento mensal, semanal e diário de um estabelecimento. Um arquivo JSON com as semanas do mês foi fornecido e foi necessário realizar conversões para BRL. As bibliotecas do Python json e pandas foram utilizadas, json para ler o arquivo e pandas para análise dos dados. 

As conclusões alcançadas incluíram a média do faturamento mensal, a média de cada semana do mês, a quantidade de dias em que a média diária foi maior que a mensal, o maior faturamento em um dia do mês e o menor faturamento em um dia do mês.



Descrição do código:

O código apresentado é uma classe chamada "Faturamento" que tem como objetivo ler um arquivo JSON e realizar algumas operações de análise de dados no conteúdo do arquivo.

Na função "init", é passado o caminho relativo do arquivo JSON como parâmetro, que é armazenado na variável "arq_json". Além disso, é chamada a função "ler_json", que é responsável por ler o arquivo JSON e retornar seu conteúdo, que é armazenado na variável "data".

Na função "ler_json", é aberto o arquivo JSON com a função "open" e o conteúdo é carregado com a função "json.load". Em seguida, o conteúdo é retornado.

Na função "ler_semana", é passado dois parâmetros: "semana" e "nome". A função é responsável por pegar as chaves e os valores de dentro da lista "semana" do arquivo JSON e criar uma tabela em um dataframe sem números = 0. O dataframe é armazenado na variável "df" e é renomeado a coluna para "semana{nome}". O dataframe é então retornado.

Na função "concatenar_semanas", é concatenado os dataframes criados pelas funções "ler_semana" para cada semana, criando assim um dataframe final para todo o mês. O dataframe final é armazenado na variável "df_mes" e é retornado.

Na função "media_semana", é calculado a média de faturamento para cada semana do mês e armazenado em um dataframe. O dataframe é então retornado.

Na função "media_faturamento_mes", é calculado a média de faturamento para todo o mês e armazenado na variável "df_mes_med". A média é então retornada.

Na função "dia_faturamento_menor_mes", é calculado o menor faturamento do mês e armazenado na variável "df_mes_min". O menor faturamento é então retornado.

Na função "dia_faturamento_maior_mes", é calculado o maior faturamento do mês e armazenado na variável "df_mes_max". O maior faturamento é então retornado.

Na função "quantidade_media_maior_media_mensal", é criada uma função interna chamada "lista_unica", que é responsável por transformar uma lista de listas em uma lista única. Em seguida, é criada uma lista chamada "quant_dias" que irá armazenar a quantidade de dias em que a média diária foi maior que a média mensal. Depois, é percorrido cada dia do mês e, caso a média diária seja maior que a média mensal, é contado como um dia em que a média diária foi maior que a média mensal. A quantidade de dias é armazenada na lista "quant_dias". Por fim, é retornado o valor da quantidade de dias.
