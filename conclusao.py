from src.faturamento_diario import quantidade, df_mes_max, df_mes_min

#conclusão
print(f"quantidade de dias em que a média diaria foi maior que a mensal: {quantidade}")
print(f"maior faturamento em um dia do mês: R$ {str(df_mes_max[0])}")
print(f"menor faturamento em um dia do mês: R$ {str(df_mes_min[0])}")
