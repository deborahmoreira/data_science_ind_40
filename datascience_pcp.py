import pandas as pd
import numpy as np

# -- Importa planilha contendo infos do MRP para materia-prima

file_0 = "/caminho-da-pasta/nivel2.xlsx"
mrp = pd.read_excel(file_0,
                    header=1, 
                    index_col=None,
                    dtype={'COMPONENTE' : str,
                           'PANTONE' : str})

"""## Limpeza e definição de relacionamentos"""

# -- Exclui primeira coluna (vazia) e ultimas linhas (observações)
mrp.drop(mrp.columns[[0]], axis=1, inplace=True)
mrp.drop(mrp.index[-7:], axis=0, inplace=True)

# -- Renomear colunas:
mrp.rename(columns={"Estoque.FAL": "ESTOQUE"}, inplace = True)
mrp.rename(columns={"TEMBOARDADO": "TEMBORDADO"}, inplace = True)
mrp.rename(columns={"PEDIDOS": "PEDIDO"}, inplace = True)

mrp.drop(columns=['PROTOTIPO'], inplace=True) #existe essa coluna vazia no df

# -- Exclui componentes que representam um conjunto(short e blusa), 
# -- pois seus projetos já estão nessa coluna
mrp.drop(mrp[mrp.COMPONENTE == ".."].index, inplace=True)

# -- Seleciona colunas que serão usadas
mrp = mrp.loc[:,["DATA","PEDIDO","REFERENCIA","PROJETO", "FAMILIA", "DCO", "SITUACAOPROTOTIPO",
                 "PANTONE", "COMPONENTE", "COMPONENTE_BASE", "PARTE_PECA", "QTD", "CONSUMO", "RESERVA", 
                 "QTDE_ESTOQUE_ACB", "FAL", "ESTOQUE", "NOMEPROMOCAO", "PROGRAMADO", "TEMLAVPOSNAT", 
                 "TEMSILK", "TEMBORDADO", "TEMLAVPOSCOST", "TEMPRENSA", "TEMSUBLIMACAO", 
                 "GM", "DT_ENTREGA_CD", "PRIORIDADE", "SEQ_MRP", "ESTAGIO_FALS"]]

# -- Exclui instâncias que já foram programadas
mrp.drop(mrp[mrp.PROGRAMADO == "SIM"].index, inplace=True)

"""###Define os grupos através do DCO"""

mrp.DCO = mrp.DCO.astype(int)
mrp.DCO = mrp.DCO.astype(str)

mrp.loc[mrp["DCO"] == "100", "GRUPO"] = "INFANTIL"
mrp.loc[mrp["DCO"] == "102", "GRUPO"] = "INFANTIL"
mrp.loc[mrp["DCO"] == "105", "GRUPO"] = "INFANTIL"
mrp.loc[mrp["DCO"] == "106", "GRUPO"] = "INFANTIL"
mrp.loc[mrp["DCO"] == "110", "GRUPO"] = "INFANTIL"
mrp.loc[mrp["DCO"] == "115", "GRUPO"] = "INFANTIL"
mrp.loc[mrp["DCO"] == "120", "GRUPO"] = "INFANTIL"
mrp.loc[mrp["DCO"] == "125", "GRUPO"] = "INFANTIL"
mrp.loc[mrp["DCO"] == "142", "GRUPO"] = "INFANTIL"
mrp.loc[mrp["DCO"] == "145", "GRUPO"] = "INFANTIL"
mrp.loc[mrp["DCO"] == "148", "GRUPO"] = "INFANTIL"
mrp.loc[mrp["DCO"] == "150", "GRUPO"] = "INFANTIL"
mrp.loc[mrp["DCO"] == "151", "GRUPO"] = "INFANTIL"
mrp.loc[mrp["DCO"] == "165", "GRUPO"] = "INFANTIL"

mrp.loc[mrp["DCO"] == "200", "GRUPO"] = "FEMININO"
mrp.loc[mrp["DCO"] == "204", "GRUPO"] = "FEMININO"
mrp.loc[mrp["DCO"] == "205", "GRUPO"] = "FEMININO"
mrp.loc[mrp["DCO"] == "206", "GRUPO"] = "FEMININO"
mrp.loc[mrp["DCO"] == "208", "GRUPO"] = "FEMININO"
mrp.loc[mrp["DCO"] == "216", "GRUPO"] = "FEMININO"
mrp.loc[mrp["DCO"] == "217", "GRUPO"] = "FEMININO"
mrp.loc[mrp["DCO"] == "226", "GRUPO"] = "FEMININO"
mrp.loc[mrp["DCO"] == "227", "GRUPO"] = "FEMININO"
mrp.loc[mrp["DCO"] == "230.1", "GRUPO"] = "FEMININO"
mrp.loc[mrp["DCO"] == "230.2", "GRUPO"] = "FEMININO"
mrp.loc[mrp["DCO"] == "270", "GRUPO"] = "FEMININO"
mrp.loc[mrp["DCO"] == "290", "GRUPO"] = "FEMININO"
mrp.loc[mrp["DCO"] == "235", "GRUPO"] = "FEMININO"

mrp.loc[mrp["DCO"] == "301", "GRUPO"] = "MASCULINO"
mrp.loc[mrp["DCO"] == "305", "GRUPO"] = "MASCULINO"
mrp.loc[mrp["DCO"] == "306", "GRUPO"] = "MASCULINO"
mrp.loc[mrp["DCO"] == "314", "GRUPO"] = "MASCULINO"
mrp.loc[mrp["DCO"] == "315", "GRUPO"] = "MASCULINO"
mrp.loc[mrp["DCO"] == "320", "GRUPO"] = "MASCULINO"
mrp.loc[mrp["DCO"] == "325", "GRUPO"] = "MASCULINO"
mrp.loc[mrp["DCO"] == "340", "GRUPO"] = "MASCULINO"
mrp.loc[mrp["DCO"] == "350", "GRUPO"] = "MASCULINO"
mrp.loc[mrp["DCO"] == "360", "GRUPO"] = "MASCULINO"
mrp.loc[mrp["DCO"] == "365", "GRUPO"] = "MASCULINO"
mrp.loc[mrp["DCO"] == "370", "GRUPO"] = "MASCULINO"
mrp.loc[mrp["DCO"] == "380", "GRUPO"] = "MASCULINO"
mrp.loc[mrp["DCO"] == "390", "GRUPO"] = "MASCULINO"

"""###Define fábricas através da família"""

mrp.FAMILIA = mrp.FAMILIA.astype(int)
mrp.FAMILIA = mrp.FAMILIA.astype(str)

mrp.loc[mrp["FAMILIA"] == '2150', 'FABRICA'] = '21'
mrp.loc[mrp.FAMILIA == '2151', 'FABRICA'] = '21'
mrp.loc[mrp.FAMILIA == '2152', 'FABRICA'] = '21'
mrp.loc[mrp.FAMILIA == '2153', 'FABRICA'] = '21'
mrp.loc[mrp.FAMILIA == '2154', 'FABRICA'] = '21'
mrp.loc[mrp.FAMILIA == '2155', 'FABRICA'] = '21'
mrp.loc[mrp.FAMILIA == '2156', 'FABRICA'] = '21'
mrp.loc[mrp.FAMILIA == '2157', 'FABRICA'] = '21'
mrp.loc[mrp.FAMILIA == '2158', 'FABRICA'] = '21'
mrp.loc[mrp.FAMILIA == '2159', 'FABRICA'] = '21'
mrp.loc[mrp.FAMILIA == '2160', 'FABRICA'] = '21'
mrp.loc[mrp.FAMILIA == '2161', 'FABRICA'] = '21'
mrp.loc[mrp.FAMILIA == '2162', 'FABRICA'] = '21'
mrp.loc[mrp.FAMILIA == '2163', 'FABRICA'] = '21'
mrp.loc[mrp.FAMILIA == '2164', 'FABRICA'] = '21'
mrp.loc[mrp.FAMILIA == '2165', 'FABRICA'] = '21'
mrp.loc[mrp.FAMILIA == '2166', 'FABRICA'] = '21'
mrp.loc[mrp.FAMILIA == '2167', 'FABRICA'] = '21'
mrp.loc[mrp.FAMILIA == '2168', 'FABRICA'] = '21'
mrp.loc[mrp.FAMILIA == '2169', 'FABRICA'] = '21'
mrp.loc[mrp.FAMILIA == '2170', 'FABRICA'] = '21'
mrp.loc[mrp.FAMILIA == '2171', 'FABRICA'] = '21'
mrp.loc[mrp.FAMILIA == '2172', 'FABRICA'] = '21'
mrp.loc[mrp.FAMILIA == '2173', 'FABRICA'] = '21'
mrp.loc[mrp.FAMILIA == '2174', 'FABRICA'] = '21'
mrp.loc[mrp.FAMILIA == '2175', 'FABRICA'] = '21'
mrp.loc[mrp.FAMILIA == '2176', 'FABRICA'] = '21'
mrp.loc[mrp.FAMILIA == '2177', 'FABRICA'] = '21'
mrp.loc[mrp.FAMILIA == '2178', 'FABRICA'] = '21'
mrp.loc[mrp.FAMILIA == '2179', 'FABRICA'] = '21'
mrp.loc[mrp.FAMILIA == '2180', 'FABRICA'] = '21'
mrp.loc[mrp.FAMILIA == '2181', 'FABRICA'] = '21'
mrp.loc[mrp.FAMILIA == '2182', 'FABRICA'] = '21'
mrp.loc[mrp.FAMILIA == '2183', 'FABRICA'] = '21'
mrp.loc[mrp.FAMILIA == '2184', 'FABRICA'] = '21'

mrp.loc[mrp.FAMILIA == '2353', 'FABRICA'] = '23'
mrp.loc[mrp.FAMILIA == '2354', 'FABRICA'] = '23'
mrp.loc[mrp.FAMILIA == '2357', 'FABRICA'] = '23'
mrp.loc[mrp.FAMILIA == '2358', 'FABRICA'] = '23'
mrp.loc[mrp.FAMILIA == '2359', 'FABRICA'] = '23'
mrp.loc[mrp.FAMILIA == '2360', 'FABRICA'] = '23'
mrp.loc[mrp.FAMILIA == '2360', 'FABRICA'] = '23'
mrp.loc[mrp.FAMILIA == '2361', 'FABRICA'] = '23'
mrp.loc[mrp.FAMILIA == '2362', 'FABRICA'] = '23'
mrp.loc[mrp.FAMILIA == '2363', 'FABRICA'] = '23'
mrp.loc[mrp.FAMILIA == '2364', 'FABRICA'] = '23'
mrp.loc[mrp.FAMILIA == '2365', 'FABRICA'] = '23'
mrp.loc[mrp.FAMILIA == '2366', 'FABRICA'] = '23'
mrp.loc[mrp.FAMILIA == '2367', 'FABRICA'] = '23'
mrp.loc[mrp.FAMILIA == '2368', 'FABRICA'] = '23'
mrp.loc[mrp.FAMILIA == '2369', 'FABRICA'] = '23'
mrp.loc[mrp.FAMILIA == '2370', 'FABRICA'] = '23'
mrp.loc[mrp.FAMILIA == '2371', 'FABRICA'] = '23'
mrp.loc[mrp.FAMILIA == '2372', 'FABRICA'] = '23'
mrp.loc[mrp.FAMILIA == '2373', 'FABRICA'] = '23'
mrp.loc[mrp.FAMILIA == '2376', 'FABRICA'] = '23'
mrp.loc[mrp.FAMILIA == '2379', 'FABRICA'] = '23'
mrp.loc[mrp.FAMILIA == '2380', 'FABRICA'] = '23'
mrp.loc[mrp.FAMILIA == '2381', 'FABRICA'] = '23'
mrp.loc[mrp.FAMILIA == '2382', 'FABRICA'] = '23'
mrp.loc[mrp.FAMILIA == '2383', 'FABRICA'] = '23'
mrp.loc[mrp.FAMILIA == '2384', 'FABRICA'] = '23'

mrp.loc[mrp.FAMILIA == '2453', 'FABRICA'] = '24'
mrp.loc[mrp.FAMILIA == '2457', 'FABRICA'] = '24'
mrp.loc[mrp.FAMILIA == '2459', 'FABRICA'] = '24'
mrp.loc[mrp.FAMILIA == '2460', 'FABRICA'] = '24'
mrp.loc[mrp.FAMILIA == '2461', 'FABRICA'] = '24'
mrp.loc[mrp.FAMILIA == '2462', 'FABRICA'] = '24'
mrp.loc[mrp.FAMILIA == '2463', 'FABRICA'] = '24'
mrp.loc[mrp.FAMILIA == '2464', 'FABRICA'] = '24'
mrp.loc[mrp.FAMILIA == '2465', 'FABRICA'] = '24'
mrp.loc[mrp.FAMILIA == '2466', 'FABRICA'] = '24'
mrp.loc[mrp.FAMILIA == '2467', 'FABRICA'] = '24'
mrp.loc[mrp.FAMILIA == '2468', 'FABRICA'] = '24'
mrp.loc[mrp.FAMILIA == '2469', 'FABRICA'] = '24'
mrp.loc[mrp.FAMILIA == '2470', 'FABRICA'] = '24'
mrp.loc[mrp.FAMILIA == '2471', 'FABRICA'] = '24'
mrp.loc[mrp.FAMILIA == '2472', 'FABRICA'] = '24'
mrp.loc[mrp.FAMILIA == '2473', 'FABRICA'] = '24'
mrp.loc[mrp.FAMILIA == '2474', 'FABRICA'] = '24'
mrp.loc[mrp.FAMILIA == '2475', 'FABRICA'] = '24'
mrp.loc[mrp.FAMILIA == '2476', 'FABRICA'] = '24'
mrp.loc[mrp.FAMILIA == '2477', 'FABRICA'] = '24'
mrp.loc[mrp.FAMILIA == '2478', 'FABRICA'] = '24'
mrp.loc[mrp.FAMILIA == '2479', 'FABRICA'] = '24'
mrp.loc[mrp.FAMILIA == '2480', 'FABRICA'] = '24'
mrp.loc[mrp.FAMILIA == '2481', 'FABRICA'] = '24'
mrp.loc[mrp.FAMILIA == '2482', 'FABRICA'] = '24'
mrp.loc[mrp.FAMILIA == '2483', 'FABRICA'] = '24'
mrp.loc[mrp.FAMILIA == '2484', 'FABRICA'] = '24'

"""### Classifica origem e beneficiamento de MP"""

"""
  Classifica matéria-prima em interna ou externa 

  Uma função que análisa todos os componentes e retorna se sua matéria-prima 
  é de origem interna, caso tenha como primeiro caractere a letra 'R' e o segundo
  caractere é outra letra qualquer. 
  Ou se é externa, caso inicie com 'M', 'S', 'A', 'T', 'I', 'A0' ou 'R' 
  seguido de um número.
  """
def classifica_mp(componente):
  if componente.startswith(('M', 'S', 'A', 'T', 'I', 'A0')):
    return "MP EXTERNA"
  elif componente.startswith('R'):
    if componente[1].isdigit():
      return "MP EXTERNA"
    if componente[1].isalpha():
      return "MP INTERNA"
  else:
    return "MP INTERNA"

mrp["ORIGEM_MP"] = mrp.apply(
    lambda row: classifica_mp(row['COMPONENTE']), axis=1
)

'''
  Classifica beneficiamento de MP.

  Se a identificação do componente contem "DG" ou "DI" ou "AV" ou "EDC" este 
  recebe beneficiamento digital.
  Se a identificação do componente contem "CL" ou "TP" ou "CAL" este recebe
  beneficiamento calandra.
  Se a identificação do componente contem "ACB" ou "RET" ou "LAV" este é tingido.
  Se não atender a nehuma dessas condições, não é beneficiado.
'''
conditions_2 = [(mrp["COMPONENTE"].str.contains("DG", case=False, regex=False)), 
              (mrp["COMPONENTE"].str.contains("DI", case=False, regex=False)), 
              (mrp["COMPONENTE"].str.contains("AV", case=False, regex=False)),
              (mrp["COMPONENTE"].str.contains("EDC", case=False, regex=False)), 
              (mrp["COMPONENTE"].str.contains("CL", case=False, regex=False)), 
              (mrp["COMPONENTE"].str.contains("TP", case=False, regex=False)),
              (mrp["COMPONENTE"].str.contains("CAL", case=False, regex=False)),
              (mrp["COMPONENTE"].str.contains(".ACB.", case=False, regex=False)), 
              (mrp["COMPONENTE"].str.contains(".RET.", case=False, regex=False)),
              (mrp["COMPONENTE"].str.contains(".LAV.", case=False, regex=False))]
choices_2 = ["DIGITAL","DIGITAL","DIGITAL","DIGITAL",
             "CALANDRA","CALANDRA","CALANDRA", 
             "TINGIMENTO", "TINGIMENTO", "TINGIMENTO"]
mrp["BENEFICIAMENTO"] = np.select(conditions_2, choices_2, default="NÃO BENEFICIADO")

"""##Protótipos"""

'''
  Classifica na base de dados a Situação do Protótipo(estágio) de cada projeto:
    Protótipo liberado = OK
    Protótipo não finalizado = PENDENTE
    
  Foi escolhido mapear a situação do protótipo a partir dos estágios de 
  protótipo não liberado, porque, apesar de em maior número, mapear os 
  estágios liberados exigiria saber os nomes dos analistas, que varia bastante.
'''
mrp.loc[mrp["SITUACAOPROTOTIPO"] == "01a - Modelagem", 'PROTOTIPO'] = "PENDENTE"
mrp.loc[mrp["SITUACAOPROTOTIPO"] == "01b - Aguardando Aprovação Variante", 'PROTOTIPO'] = "PENDENTE"
mrp.loc[mrp["SITUACAOPROTOTIPO"] == "02a - Pegar MP", 'PROTOTIPO'] = "PENDENTE"
mrp.loc[mrp["SITUACAOPROTOTIPO"] == "02c - Descanso de MP", 'PROTOTIPO'] = "PENDENTE"
mrp.loc[mrp["SITUACAOPROTOTIPO"] == "03a - Corte", 'PROTOTIPO'] = "PENDENTE"
mrp.loc[mrp["SITUACAOPROTOTIPO"] == "03b - Plissado", 'PROTOTIPO'] = "PENDENTE"
mrp.loc[mrp["SITUACAOPROTOTIPO"] == "04a - Falta de Aviamento", 'PROTOTIPO'] = "PENDENTE"
mrp.loc[mrp["SITUACAOPROTOTIPO"] == "04b - Falta de Aviamento - Peça Acabada", 'PROTOTIPO'] = "PENDENTE"
mrp.loc[mrp["SITUACAOPROTOTIPO"] == "04c - FULL KIT (Corte)", 'PROTOTIPO'] = "PENDENTE"
mrp.loc[mrp["SITUACAOPROTOTIPO"] == "05 - Customização", 'PROTOTIPO'] = "PENDENTE"
mrp.loc[mrp["SITUACAOPROTOTIPO"] == "06a - Costura", 'PROTOTIPO'] = "PENDENTE"
mrp.loc[mrp["SITUACAOPROTOTIPO"] == "06b - Medição/Costura", 'PROTOTIPO'] = "PENDENTE"
mrp.loc[mrp["SITUACAOPROTOTIPO"] == "07 - Estilo definição de Customização", 'PROTOTIPO'] = "PENDENTE"
mrp.loc[mrp["SITUACAOPROTOTIPO"] == "08 - Customização Pós Costura", 'PROTOTIPO'] = "PENDENTE"
mrp.loc[mrp["SITUACAOPROTOTIPO"] == "09a - Prova", 'PROTOTIPO'] = "PENDENTE"
mrp.loc[mrp["SITUACAOPROTOTIPO"] == "09b - Aprovação Virtual", 'PROTOTIPO'] = "PENDENTE"
mrp.loc[mrp["SITUACAOPROTOTIPO"] == "10a - Lavanderia", 'PROTOTIPO'] = "PENDENTE"
mrp.loc[mrp["SITUACAOPROTOTIPO"] == "10b - Medição/Lavagem", 'PROTOTIPO'] = "PENDENTE"
mrp.loc[mrp["SITUACAOPROTOTIPO"] == "11 - Acabamento", 'PROTOTIPO'] = "PENDENTE"
mrp.loc[mrp["SITUACAOPROTOTIPO"] == "13 - Consumo (Analise de Custo)", 'PROTOTIPO'] = "PENDENTE"
mrp.loc[mrp["SITUACAOPROTOTIPO"] == "14 - Tempo", 'PROTOTIPO'] = "PENDENTE"
mrp.loc[mrp["SITUACAOPROTOTIPO"] == "15 - Preço (Analise de Custo)", 'PROTOTIPO'] = "PENDENTE"
mrp.loc[mrp["SITUACAOPROTOTIPO"] == "16b - Aprov. Licenciados", 'PROTOTIPO'] = "PENDENTE"
mrp.loc[mrp["SITUACAOPROTOTIPO"] == "16c - Pendência Suprimentos", 'PROTOTIPO'] = "PENDENTE"
mrp.loc[mrp["SITUACAOPROTOTIPO"] == "18 - Amostra Parcial Concluída", 'PROTOTIPO'] = "PENDENTE"
mrp.loc[mrp["SITUACAOPROTOTIPO"] == "16a - Ficha Técnica", 'PROTOTIPO'] = "PENDENTE"
mrp.loc[mrp["SITUACAOPROTOTIPO"] == "31a - Pronto para Lacre", 'PROTOTIPO'] = "PENDENTE"
mrp.loc[mrp["SITUACAOPROTOTIPO"] == "31b - Pronto para Montagem (Lacrada)", 'PROTOTIPO'] = "PENDENTE"
mrp.loc[mrp["SITUACAOPROTOTIPO"] == "32c - Peça Lacrada", 'PROTOTIPO'] = "PENDENTE"
mrp.loc[mrp["SITUACAOPROTOTIPO"] == "33 - Montagem de Linha", 'PROTOTIPO'] = "PENDENTE"
mrp.loc[mrp["SITUACAOPROTOTIPO"] == "34a - Pendencia de Estilo", 'PROTOTIPO'] = "PENDENTE"
mrp.loc[mrp["SITUACAOPROTOTIPO"] == "34b - Peça com Estilista", 'PROTOTIPO'] = "PENDENTE"
mrp.loc[mrp["SITUACAOPROTOTIPO"] == "40a - Bandeira/Silk (Protótipo)", 'PROTOTIPO'] = "PENDENTE"
mrp.loc[mrp["SITUACAOPROTOTIPO"] == "40b - Bandeira/Bordado", 'PROTOTIPO'] = "PENDENTE"
mrp.loc[mrp["SITUACAOPROTOTIPO"] == "40c - Bandeira/Est. Dig.", 'PROTOTIPO'] = "PENDENTE"
mrp.loc[mrp["SITUACAOPROTOTIPO"] == "50 - Stand by", 'PROTOTIPO'] = "PENDENTE"
mrp.loc[mrp["SITUACAOPROTOTIPO"] == "55 - A definir", 'PROTOTIPO'] = "PENDENTE"
mrp.loc[mrp["SITUACAOPROTOTIPO"] == "60 - Cancelado", 'PROTOTIPO'] = "PENDENTE"
mrp.loc[mrp["SITUACAOPROTOTIPO"] == "65 - Reativado", 'PROTOTIPO'] = "PENDENTE"
mrp.loc[mrp["SITUACAOPROTOTIPO"] == "70 - Falta de MP (Modelagem)", 'PROTOTIPO'] = "PENDENTE"
mrp.loc[mrp["SITUACAOPROTOTIPO"] == "75 - Publicado", 'PROTOTIPO'] = "PENDENTE"
mrp.loc[mrp["SITUACAOPROTOTIPO"] == "80 - Esqueleto", 'PROTOTIPO'] = "PENDENTE"
mrp.loc[mrp["SITUACAOPROTOTIPO"] == "85 - Sem Situação", 'PROTOTIPO'] = "PENDENTE"
mrp.loc[mrp["SITUACAOPROTOTIPO"] == "95 - Validação de cortes Externos", 'PROTOTIPO'] = "PENDENTE"
mrp.loc[mrp["SITUACAOPROTOTIPO"] == "95b - Refação", 'PROTOTIPO'] = "PENDENTE"
mrp.loc[mrp["SITUACAOPROTOTIPO"] == "Alfândega", 'PROTOTIPO'] = "PENDENTE"
mrp.loc[mrp["SITUACAOPROTOTIPO"] == "ALMOXARIFADO", 'PROTOTIPO'] = "PENDENTE"
mrp.loc[mrp["SITUACAOPROTOTIPO"] == "BORDADO", 'PROTOTIPO'] = "PENDENTE"
mrp.loc[mrp["SITUACAOPROTOTIPO"] == "BORDADO (DESENVOLVIMENTO ARTE)", 'PROTOTIPO'] = "PENDENTE"
mrp.loc[mrp["SITUACAOPROTOTIPO"] == "CL - ESTAMPARIA DIGITAL", 'PROTOTIPO'] = "PENDENTE"
mrp.loc[mrp["SITUACAOPROTOTIPO"] == "ESTAMPADO EM TERCEIROS", 'PROTOTIPO'] = "PENDENTE"
mrp.loc[mrp["SITUACAOPROTOTIPO"] == "EXTERNA", 'PROTOTIPO'] = "PENDENTE"
mrp.loc[mrp["SITUACAOPROTOTIPO"] == "Falta de retilínea", 'PROTOTIPO'] = "PENDENTE"
mrp.loc[mrp["SITUACAOPROTOTIPO"] == "Falta Endereçar", 'PROTOTIPO'] = "PENDENTE"
mrp.loc[mrp["SITUACAOPROTOTIPO"] == "FOTOGRAVAÇÃO", 'PROTOTIPO'] = "PENDENTE"
mrp.loc[mrp["SITUACAOPROTOTIPO"] == "INTERNA", 'PROTOTIPO'] = "PENDENTE"
mrp.loc[mrp["SITUACAOPROTOTIPO"] == "LAVANDERIA", 'PROTOTIPO'] = "PENDENTE"
mrp.loc[mrp["SITUACAOPROTOTIPO"] == "MP EXTERNA", 'PROTOTIPO'] = "PENDENTE"
mrp.loc[mrp["SITUACAOPROTOTIPO"] == "MS - ESTAMPARIA DIGITAL", 'PROTOTIPO'] = "PENDENTE"
mrp.loc[mrp["SITUACAOPROTOTIPO"] == "MS - PREPARAÇÃO DE BASE", 'PROTOTIPO'] = "PENDENTE"
mrp.loc[mrp["SITUACAOPROTOTIPO"] == "Pesquisa e Desenvolvimento", 'PROTOTIPO'] = "PENDENTE"
mrp.loc[mrp["SITUACAOPROTOTIPO"] == "REPOSIÇÃO", 'PROTOTIPO'] = "PENDENTE"
mrp.loc[mrp["SITUACAOPROTOTIPO"] == "Reposição de MP", 'PROTOTIPO'] = "PENDENTE"
mrp.loc[mrp["SITUACAOPROTOTIPO"] == "SILK", 'PROTOTIPO'] = "PENDENTE"
mrp.loc[mrp["SITUACAOPROTOTIPO"] == "SILK (DESENVOLVIMENTO ARTE)", 'PROTOTIPO'] = "PENDENTE"
mrp.loc[mrp["SITUACAOPROTOTIPO"] == "SUBLIMAÇÃO", 'PROTOTIPO'] = "PENDENTE"
mrp.loc[mrp["SITUACAOPROTOTIPO"] == "SUBLIMAÇÃO (DESENVOLVIMENTO ARTE)", 'PROTOTIPO'] = "PENDENTE"
mrp.loc[mrp["SITUACAOPROTOTIPO"] == "TRANSF ENTRE UNIDADES", 'PROTOTIPO'] = "PENDENTE"
mrp.loc[mrp["SITUACAOPROTOTIPO"] == "12 - Ampliação / Liberação", 'PROTOTIPO'] = "PENDENTE"
mrp.loc[mrp["SITUACAOPROTOTIPO"] == "13 - Consumo", 'PROTOTIPO'] = "PENDENTE"
mrp.loc[mrp["SITUACAOPROTOTIPO"] == "15 - Preço", 'PROTOTIPO'] = "PENDENTE"
mrp.loc[mrp["SITUACAOPROTOTIPO"] == "19 - Controle", 'PROTOTIPO'] = "PENDENTE"
mrp.loc[mrp['PROTOTIPO'] != "PENDENTE", 'PROTOTIPO'] = "OK"
mrp.drop(columns=['SITUACAOPROTOTIPO'], inplace=True)

"""## Pedidos"""

# -- Classifica status dos Pedidos
mrp["PEDIDO"] = mrp["PEDIDO"].fillna("PENDENTE")
mrp.loc[mrp["PEDIDO"] != "PENDENTE", "PEDIDO"] = "OK"

"""## Matéria-prima

### Saldo MP INTERNA
"""

'''
  Calcula porcentagem de estoque/reserva.

  Em produtos que recebem beneficamento digital é descontado 16%, nos que
  recebem tingimento como beneficiamento é descontado 10%. Para os demais, 
  não se altera o total.
'''
def porcentagem_fal(estoque, reserva, beneficiamento):
  try:
    if beneficiamento == "DIGITAL":
      return (estoque/reserva - 0.16) * 100
    elif beneficiamento == "TINGIMENTO":
      return (estoque/reserva - 0.1) * 100
    else:
      return (estoque/reserva) * 100
  except ZeroDivisionError:
    return 0
mrp["ESTOQUE_FAL%"] = mrp.apply(
    lambda row: porcentagem_fal(row['ESTOQUE'], row['RESERVA'], row['BENEFICIAMENTO']),
    axis = 1
)

'''
  Analisa Status da FAL.

  Caso a porcentagem de estoque/reserva esteja acima de 95% a FAL 
  (Ficha de Acompanhamento de Lote) seu status recebe "OK". 
  Se a coluna "FAL" tem o numeral zero, seu status recebe "SEM FAL",
  pois a mesma não foi emitida. 
  Se a coluna mesma coluna contém quaisquer outros símbolos, 
  seu status recebe " FAL", significa que esta foi emitida, mas ainda não está 
  liberada.
'''

conditions_3 = [(mrp["ESTOQUE_FAL%"] >= 0.95), 
                (mrp["FAL"] != 0), 
                (mrp["FAL"] == 0)]
choices_3 = ["OK", "FAL", "SEM FAL"]
mrp["STATUS_FAL"] = np.select(conditions_3, choices_3, default= " ")

"""### Saldo MP EXTERNA"""

'''
  Análise de saldo de componentes de matéria-prima externa.

  Caso a coluna "COMPONENTE" contenha o subgrupo .RET. na sua identificação,
  se faz necessário análise do saldo pela coluna "COMPONENTE_BASE".
  Caso contrário, se analisa o saldo pela coluna "COMPONENTE".
  Em ambos os casos, são agrupados e somados as reservas e os estoques 
  de um componente. Se a diferença entre estoque e reserva for positiva, pode-se
  afirmar que há MP para uma determinada necessidade.
'''
# -- Analisa saldo por componente
saldo_comp = mrp.groupby(["COMPONENTE"]).agg( 
    sum_reserva=('RESERVA', 'sum'),  
    sum_estoque=('ESTOQUE', 'sum') 
) 
saldo_comp['status'] = saldo_comp.apply( 
    lambda row: 'OK' if row.sum_estoque - row.sum_reserva > 0 else 'PENDENTE', 
    axis=1 
) 

# -- Analisa saldo por componente_base
saldo_comp_base = mrp.groupby(["COMPONENTE_BASE"]).agg( 
    sum_reserva=('RESERVA', 'sum'),  
    sum_estoque=('ESTOQUE', 'sum') 
) 
saldo_comp_base['status'] = saldo_comp_base.apply( 
    lambda row: 'OK' if row.sum_estoque - row.sum_reserva > 0 else 'PENDENTE', 
    axis=1 
) 

def saldo_mp_externa(ori_mp, componente, componente_base, saldo_comp, saldo_comp_base):
  if ori_mp == "MP EXTERNA" and ".RET." in componente:
    return saldo_comp_base.loc[[componente_base], 'status'].values[0]
  else:
    return saldo_comp.loc[[componente], 'status'].values[0]

saldo = mrp.apply(
    lambda row: saldo_mp_externa(row.ORIGEM_MP, row.COMPONENTE, row.COMPONENTE_BASE, saldo_comp, saldo_comp_base),
    axis=1
)

"""### Reune informações para análise de MP"""

# -- Classifica situação da matéria prima
mrp.loc[(mrp["STATUS_FAL"] == "OK") & (mrp["ORIGEM_MP"] == "MP INTERNA"), "MP"] = "OK"
mrp.loc[(mrp["STATUS_FAL"] != "OK") & (mrp["ORIGEM_MP"] == "MP INTERNA"), "MP"] = "PENDENTE"
mrp.loc[(saldo == "OK") & (mrp["ORIGEM_MP"] == "MP EXTERNA"), "MP"] = "OK"
mrp.loc[(saldo == "PENDENTE") & (mrp["ORIGEM_MP"] == "MP EXTERNA"), "MP"] = "PENDENTE"

"""## Cria chave para cada projeto"""

# -- Cria chave única para cada projeto
mrp["PANTONE"] = mrp.apply(
    lambda row: row.PANTONE.replace(".0", "") if row.PANTONE.endswith(".0") else row.PANTONE,
    axis=1
)
mrp[["SEQ_MRP"]] = mrp[["SEQ_MRP"]].astype(int)
mrp[["DATA", "REFERENCIA", "SEQ_MRP"]] = mrp[["DATA", "REFERENCIA", "SEQ_MRP"]].astype(str)
mrp["CHAVE"] = mrp["DATA"] + mrp["REFERENCIA"] + mrp["PANTONE"] + mrp["SEQ_MRP"]


"""# ANÁLISE AVIAMENTOS (NÍVEL 9)
"""

# -- Importa planilha contendo infos do MRP para aviamentos

file_1 = "/caminho-da-pasta/nivel9.xlsx"
av = pd.read_excel(file_1, header=0, index_col=None)

"""## Limpeza e definição de relacionamentos"""

'''
  Nesse dataset não foi preciso excluir a primeira coluna (vazia) e 
  ultimas linhas (observações), mas geralmente no layout usual precisa.   
  
  Caso seja necessário, usar:
  av.drop(av.columns[[0]], axis=1, inplace=True)
  av.drop(av.index[-7:], axis=0, inplace=True)
'''
# -- Renomear colunas:
av.rename(columns={"TEMBOARDADO": "TEMBORDADO"}, inplace = True)
av.rename(columns={"PEDIDOS": "PEDIDO"}, inplace = True)

# -- Seleciona colunas que serão usadas
av = av.loc[:,["DATA", "REFERENCIA","PROJETO", "FAMILIA", "DCO", 
                 "PANTONE", "COMPONENTE", "PARTE_PECA", "QTD", "CONSUMO", "RESERVA", 
                 "QTDE_ESTOQUE_ACB", "FAL", "NOMEPROMOCAO", "PROGRAMADO", "TEMLAVPOSNAT", 
                 "TEMSILK", "TEMBORDADO", "TEMLAVPOSCOST", "TEMPRENSA", "TEMSUBLIMACAO", 
                 "GM", "DT_ENTREGA_CD", "PRIORIDADE", "SEQ_MRP", "ESTAGIO_FALS", "ATENDIDO"]]

# -- Define tipo de coluna componente e exclui virgulas (ocorre em componentes que são só números)
av.COMPONENTE = av.COMPONENTE.astype(str)
av.COMPONENTE = av.COMPONENTE.str.replace(",","")

# -- Exclui instâncias que já foram programadas
av.drop(av[av.PROGRAMADO == "SIM"].index, inplace=True)
av.drop(av[av.ATENDIDO == "SIM"].index, inplace=True)

"""### Classifica origem e beneficiamento de AV"""

"""
  Classifica aviamento em MP interna ou externa.

  Uma função que análisa todos os componentes e retorna se sua matéria-prima 
  é de origem interna, caso tenha como segundo caractere a letra 'B'.
  Ou se é externa, caso contrário.
"""

av["ORIGEM_MP"] = av.apply(
    lambda row: 'MP INTERNA' if row["COMPONENTE"][1] == "B" else 'MP EXTERNA', axis=1
)

'''
  Classifica beneficiamento de MP.

  Se segunda letra do componente é B, significa que ele é beneficiado.
  Caso contrário, ele não é beneficiado.
'''
av["BENEFICIAMENTO"] = av.apply(
    lambda row: 'SIM' if row["COMPONENTE"][1] == "B" else 'NÃO', axis=1
)

"""## Importa estoque de aviamentos

Como as informações de estoque de todos os aviamentos se encontra em outro arquivo, é necessário importá-lo.
"""

# -- Importa planilha contendo infos do saldo de todos os aviamentos

file_2 = "/caminho-da-pasta/estoque_nivel9.xlsx"

estoque_n9 = pd.read_excel(file_2, 
                           header=0, 
                           index_col=None,  
                           dtype={'CODCONSUMO': str, "ESTOQUE_ATUAL": float})

# -- Seleciona as colunas necessárias
estoque_n9 = estoque_n9.loc[:,['CODCONSUMO', "ESTOQUE_ATUAL"]]

# -- Exclui virgulas (ocorre em componentes que são só números)
estoque_n9.CODCONSUMO = estoque_n9.CODCONSUMO.str.replace(",", "")
estoque_n9 = estoque_n9.set_index('CODCONSUMO')

# -- Preenche células vazias com zero
estoque_n9["ESTOQUE_ATUAL"] = estoque_n9["ESTOQUE_ATUAL"].fillna(0)

# Transforma dataframe em dicionário para acelerar a busca
estoque_dict = pd.DataFrame(estoque_n9).to_dict()['ESTOQUE_ATUAL']

# -- Preenche coluna ESTOQUE com as infos do dicionário
def get_estoque(componente, dictt):
  if componente in dictt:
    return dictt[componente]

av["ESTOQUE"] = av.apply(
    lambda row: get_estoque(row.COMPONENTE, estoque_dict),
    axis=1)

"""## Saldo AV"""

# -- Analisa saldo
saldo = av.groupby(["COMPONENTE"]).agg( 
    sum_reserva=('RESERVA', 'sum'),  
    sum_estoque=('ESTOQUE', 'sum') 
) 

saldo['status'] = saldo.apply( 
    lambda row: 'OK' if row.sum_estoque - row.sum_reserva > 0 else 'ANALISAR', 
    axis=1 
) 
av["saldo_n9"] = av.apply( 
    lambda row: saldo.loc[[(row.COMPONENTE)], 'status'].values[0], 
    axis=1 
)

"""## Cria chave para cada projeto"""

# -- Cria chave única para cada projeto
av["PANTONE"] = av["PANTONE"].astype(str)
av["PANTONE"] = av.apply(
    lambda row: row.PANTONE.replace(".0", "") if row.PANTONE.endswith(".0") else row.PANTONE,
    axis=1
)
av[["SEQ_MRP"]] = av[["SEQ_MRP"]].astype(int)
av[["DATA", "REFERENCIA", "SEQ_MRP"]] = av[["DATA", "REFERENCIA", "SEQ_MRP"]].astype(str)
av["CHAVE"] = av["DATA"] + av["REFERENCIA"] + av["PANTONE"] + av["SEQ_MRP"]


"""# DISPONÍVEL PARA GERAR OP
"""

# -- Cria dicionário {CHAVE:SALDO_AV} para associar informações do nível 9 com o nível 2
saldo_por_chave = av[['CHAVE', 'saldo_n9']].groupby('CHAVE').apply(lambda row: 'OK' if (row.saldo_n9 == "OK").all() else 'PENDENTE')
df = pd.DataFrame(saldo_por_chave) 
dict_saldo_por_chave = pd.DataFrame(saldo_por_chave).to_dict()
dict_saldo_por_chave = dict_saldo_por_chave[0]

# -- Preenche coluna "SALDO_AV" com as infos do dicionário
def get_saldo_av(chave, dictt):
  if chave in dictt:
    return dictt[chave]
  else:
    return "OK" #não encontrou chave em aviamentos, supõe que não influencia no fullkit
mrp["SALDO_AV"] = mrp.apply(
    lambda row: get_saldo_av(row.CHAVE, dict_saldo_por_chave),
    axis=1
)

mrp['values'] = mrp.apply(
    lambda row: "OK" if (row[["PEDIDO", "MP", "PROTOTIPO", "SALDO_AV"]] == "OK").all() else "PENDENTE",
    axis=1
)

fk = mrp[['CHAVE', 'values']].groupby('CHAVE')['values'].apply(lambda x: 'OK' if 'PENDENTE' not in x.unique().tolist() else 'PENDENTE')

full_kit_dict = pd.DataFrame(fk).to_dict()['values']
mrp["FULLKIT"] = mrp.apply(
    lambda row: full_kit_dict[row.CHAVE],
    axis=1
)


"""# PENDÊNCIAS
"""

# -- Concatena verticalmente os dois principais dataframes
all = pd.concat([mrp, av])

'''
  Sumariza pendências de todos os componentes.

  Se o componente tem "OK" na coluna criada na seção anterior (FULLKIT), este 
  pode ter sua ordem gerada. Para os demais que possuem pendências, existem 
  quatro situaçãoes possíveis: 
      - pendência de protótipo
      - pendência de matéria-prima
      - pendência de pedido
      - pendência de aviamento
'''
all["STATUS"] = str("")

def analisar_situacao(full_kit, prototipo, mp, beneficiamento, status_fal, ori_mp, pedido, saldo_n9):
  # -- Situação F: componente pode ter sua ordem gerada
  if full_kit == "OK":
   return "DISPONÍVEL PARA PROGRAMAR"
  else:
    # -- Situação A: protótipo pendente 
    a = "PROTOTIPO" if prototipo == "PENDENTE" else ""
    # -- Situação B: matéria prima pendente
    b = ""
    if mp != "OK":
      if ori_mp == "MP EXTERNA":
        b = "MP EXTERNA"
      elif status_fal == "SEM FAL":
        if beneficiamento == "TINGIMENTO" or beneficiamento == "NÃO BENEFICIADO":
          b = "SEM FAL"
        if beneficiamento == "DIGITAL":
          b = "SEM FAL DIGITAL"
        if beneficiamento == "CALANDRA":
          b = "SEM FAL CALANDRA"
      elif status_fal == "FAL":
        if beneficiamento == "TINGIMENTO" or beneficiamento == "NÃO BENEFICIADO":
          b = "FAL"
        if beneficiamento == "DIGITAL":
          b = "FAL DIGITAL"
        if beneficiamento == "CALANDRA":
          b = "FAL CALANDRA"
    # -- Situação C: pedido pendente
    c = "PEDIDO" if pedido == "PENDENTE" else ""
    # -- Situação D: aviamento pendente
    d = "AV" if saldo_n9 == "PENDENTE" else ""
    return a + " | " + b + " | " + c + " | " + d
    
all["STATUS"] = all.apply( 
    lambda row: analisar_situacao(row["FULLKIT"], 
                                  row["PROTOTIPO"], 
                                  row["MP"], 
                                  row["BENEFICIAMENTO"], 
                                  row["STATUS_FAL"], 
                                  row["ORIGEM_MP"], 
                                  row["PEDIDO"],
                                  row["saldo_n9"]), 
    axis=1)

# Retirando colunas usadas apenas para relações
all.drop(columns=["values", "saldo_n9"], inplace=True)


"""# DOWNLOAD .xlsx

Para acessar as planilhas, siga a até a pasta de destino escolhida.
"""

mrp.to_excel(r"/caminho-pasta-destino/mp.xlsx", index = True)

av.to_excel(r"/caminho-pasta-destino/av.xlsx", index = True)

all.to_excel(r"/caminho-pasta-destino/a_programar.xlsx", index = True)
