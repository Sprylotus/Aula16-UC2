import os

os.system('cls')
import polars as pl
from datetime import datetime

ENDERECO_DADOS = r'./Dados/'

try:
    hora_inicio = datetime.now()

    df_dados = pl.read_csv(ENDERECO_DADOS + 'dados_teste.csv', separator=',', encoding='utf-8')

    df_dados_lazy = df_dados.lazy()

    df_dados_lazy = (
        df_dados_lazy
        .filter(pl.col('total_vendas') > 1000)
        .group_by('regiao', 'forma_pagamento')
        .agg((pl.col('quantidade').sum().alias('soma_qtd')))
    )

    df_bf = df_dados_lazy.collect()

    print(df_bf)

    hora_fim = datetime.now()

    print(f'Tempo de execução: {hora_fim - hora_inicio}')

    print('Dados obtidos com sucesso!')

except ImportError as e:
    print(f'Erro ao obter dados: {e}')