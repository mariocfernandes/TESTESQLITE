import pandas as pd
import streamlit as st
from datetime import datetime
import openpyxl


# titulo
st.title('CJ SHOPS')
st.header('Consulta Segmentada de Clientes - RFV')


# carrega arquivos 
arquivo1 = 'rfm_table.xlsx'
arquivo2 = 'clientes_cjshops.xlsx'

colunas1 = ['Cliente Varejo','Codigo_Cliente','vendedor','CNPJ / CPF','recencia','frequencia','valor_monetario','Segmento','Ddd','Telefone','mes_niver']
colunas2 = ['Codigo_Cliente','Qtde','Desc Produto','Desc Cor Produto','Dt_Venda']

@st.cache
def get_data1():
    return pd.read_excel(arquivo1, dtype = {'Codigo_Cliente':object,'valor_monetario':float},usecols = colunas1, engine = 'openpyxl')
def get_data2():
    return pd.read_excel(arquivo2, dtype = {'Codigo_Cliente':object}, usecols = colunas2,engine = 'openpyxl')


df1 = get_data1()
df2 = get_data2()
df2['Dt_Venda'] = df2['Dt_Venda'].dt.strftime('%d-%m-%Y')

lista_vendedor = df1.vendedor.unique()

escolha_vendedor = st.selectbox('Vendedor',lista_vendedor)


df3  = df1[df1.vendedor == escolha_vendedor]

lista_segmentos = df3.Segmento.unique()

escolha_segmento = st.selectbox('Escolha um Segmento de Clientes',lista_segmentos)


df_filtro = df3.Segmento == escolha_segmento

st.dataframe(df3[df_filtro].style.format({'valor_monetario':'{:.2f}'}))


cod_cliente = st.sidebar.text_input('Digite o Codigo do Cliente')

df_filtro2 = df2['Codigo_Cliente'] == cod_cliente


st.sidebar.table(df2[df_filtro2])




