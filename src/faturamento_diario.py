from src.calculos import Faturamento
import locale 

def formatar_brl(lista):
    # setar a localidade para o Brasil
    locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
    # converter o primeiro elemento para o formato de moeda BRL
    primeiro_elemento_formatado = locale.currency(lista[0], grouping=True)
    # substituir o primeiro elemento na lista pela versão formatada
    lista[0] = primeiro_elemento_formatado
    return lista

faturamento = Faturamento(r'.\faturamento\mes.json')
faturamento.concatenar_semanas()

quantidade = faturamento.quantidade_media_maior_media_mensal()
df_mes_max = formatar_brl(faturamento.dia_faturamento_maior_mes())
df_mes_min = formatar_brl(faturamento.dia_faturamento_menor_mes())