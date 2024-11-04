from bs4 import BeautifulSoup
import requests
from datetime import datetime
import pandas as pd
import os

def paliativo_processamento():
    resultado = []
    ################################## Viniferas ##############################################
    linkViniferas = "http://vitibrasil.cnpuv.embrapa.br/download/ProcessaViniferas.csv"
    response = requests.get(linkViniferas)

    if response.status_code == 200:
        with open('ProcessaViniferas.csv', 'wb') as file:
            file.write(response.content)
        print("Arquivo Viniferas salvo com sucesso !")
    else:
        print(f"Falha ao baixar arquivo Viniferas.")

    csv_df = pd.read_csv("ProcessaViniferas.csv", sep=';')
    colunas = csv_df.loc[:, 'cultivar':].columns[1:].tolist()
    for i in colunas:
        csv_df[f'{i}'] = csv_df[f'{i}'].replace('*', '0')
        ##csv_df['cultivar'] = csv_df['cultivar'].apply(lambda x: x.encode('utf-8').decode('unicode_escape'))

        filtered_ti = csv_df[csv_df['control'].str.startswith("ti_")].copy()
        filtered_ti = filtered_ti.assign(
            aba="PROCESSAMENTO",
            sub_aba="Viniferas",
            categoria="TINTAS",
            ano=i
        )
        select_ti = filtered_ti[['aba', 'sub_aba', 'categoria', 'cultivar', f'{i}', 'ano']]
        select_ti = select_ti.rename(columns={f'{i}': 'quantidade_kg', 'cultivar': 'produto'}).to_dict(orient='records')
        resultado.extend(select_ti)

        filtered_br = csv_df[csv_df['control'].str.startswith("br_")].copy()
        filtered_br = filtered_br.assign(
            aba="PROCESSAMENTO",
            sub_aba="Viniferas",
            categoria="BRANCAS E ROSADAS",
            ano=i
        )
        select_br = filtered_br[['aba', 'sub_aba', 'categoria', 'cultivar', f'{i}', 'ano']]
        select_br = select_br.rename(columns={f'{i}': 'quantidade_kg', 'cultivar': 'produto'}).to_dict(orient='records')
        resultado.extend(select_br)
       # os.remove("ProcessaViniferas.csv")

    ################################### Americanas e Híbridas ##############################################
    linkAmHb = "http://vitibrasil.cnpuv.embrapa.br/download/ProcessaAmericanas.csv"
    response = requests.get(linkAmHb)

    if response.status_code == 200:
        with open('ProcessaAmericanas.csv', 'wb') as file:
            file.write(response.content)
        print("Arquivo Americanas e Hibridas salvo com sucesso !")
    else:
        print(f"Falha ao baixar arquivo Americanas e Hibridas.")
    
    csv_df2 = pd.read_csv("ProcessaAmericanas.csv", sep='\t')
    colunas = csv_df2.loc[:, 'cultivar':].columns[1:].tolist()
    for x in colunas:
        csv_df2[f'{x}'] = csv_df2[f'{x}'].replace('*','0')
        ##csv_df2['cultivar'] = csv_df2['cultivar'].apply(lambda x: x.encode('utf-8').decode('unicode_escape'))

        filtered_ti2 = csv_df2[csv_df2['control'].str.startswith("ti_")].copy()
        filtered_ti2 = filtered_ti2.assign(
            aba="PROCESSAMENTO",
            sub_aba="Americanas e Hibridas",
            categoria="TINTAS",
            ano=x
        )
        select_ti2 = filtered_ti2[['aba', 'sub_aba', 'categoria', 'cultivar', f'{x}', 'ano']]
        select_ti2 = select_ti2.rename(columns={f'{x}': 'quantidade_kg', 'cultivar': 'produto'}).to_dict(orient='records')
        resultado.extend(select_ti2)

        filtered_br2 = csv_df2[csv_df2['control'].str.startswith("br_")].copy()
        filtered_br2 = filtered_br2.assign(
            aba="PROCESSAMENTO",
            sub_aba="AMERICANAS E HIBRIDAS",
            categoria="BRANCAS E ROSADAS",
            ano=x
        )
        select_br2 = filtered_br2[['aba', 'sub_aba', 'categoria', 'cultivar', f'{x}', 'ano']]
        select_br2 = select_br2.rename(columns={f'{x}': 'quantidade_kg', 'cultivar': 'produto'}).to_dict(orient='records')
        resultado.extend(select_br2)
       # os.remove("ProcessaAmericanas.csv")

    ################################### Uvas de mesa ##############################################
    linkUMesa = "http://vitibrasil.cnpuv.embrapa.br/download/ProcessaMesa.csv"
    response = requests.get(linkUMesa)

    if response.status_code == 200:
        with open('ProcessaMesa.csv', 'wb') as file:
            file.write(response.content)
        print("Arquivo de Uvas de Mesa salvo com sucesso !")
    else:
        print("Falha ao baixar arquivo Uvas de Mesa")
    
    csv_df3 = pd.read_csv("ProcessaMesa.csv", sep='\t')
    colunas = csv_df3.loc[:, 'cultivar':].columns[1:].tolist()
    for u in colunas:
        csv_df3[f"{u}"] = csv_df3[f'{u}'].replace('*','0')
        ##csv_df3['cultivar'] = csv_df3['cultivar'].apply(lambda x: x.encode('utf-8').decode('unicode_escape'))

        filtered_ti3 = csv_df3[csv_df3['control'].str.startswith("ti_")].copy()
        filtered_ti3 = filtered_ti3.assign(
            aba="PROCESSAMENTO",
            sub_aba="Uvas de Mesa",
            categoria="TINTAS",
            ano=i
        )
        
        select_ti3 = filtered_ti3[['aba','sub_aba', 'categoria','cultivar', f'{u}', 'ano']]
        select_ti3 = select_ti3.rename(columns={f'{u}': 'quantidade_kg', 'cultivar': 'produto'}).to_dict(orient='records')
        resultado.extend(select_ti3)

        filtered_br3 = csv_df3[csv_df3['control'].str.startswith("br_")].copy()
        filtered_br3 = filtered_br3.assign(
            aba="PROCESSAMENTO",
            sub_aba="Uvas de Mesa",
            categoria="BRANCAS E ROSADAS",
            ano=u
        )
        select_br3 = filtered_br3[['aba', 'sub_aba', 'categoria', 'cultivar', f'{u}', 'ano']]
        select_br3 = select_br3.rename(columns={f'{u}': 'quantidade_kg', 'cultivar': 'produto'}).to_dict(orient='records')
        resultado.extend(select_br3)

    ################################### Uvas de mesa ##############################################
    linkSemClass = "http://vitibrasil.cnpuv.embrapa.br/download/ProcessaSemclass.csv"
    response = requests.get(linkSemClass)

    if response.status_code == 200:
        with open('ProcessaSemclass.csv', 'wb') as file:
            file.write(response.content)
        print("Arquivo de Sem Classificação salvo com sucesso !")
    else:
        print("Falha ao baixar arquivo Sem Classificação")
    
    csv_df4 = pd.read_csv("ProcessaSemclass.csv", sep='\t')
    colunas = csv_df4.loc[:, 'cultivar':].columns[1:].tolist()

    for c in colunas:
        csv_df4[f"{u}"] = csv_df4[f'{u}'].replace('*','0')
        #csv_df4['cultivar'] = csv_df4['cultivar'].apply(lambda x: x.encode('utf-8').decode('unicode_escape'))

        filtered = csv_df4[csv_df4['control'].str.startswith("Sem")].copy()
        filtered = filtered.assign(
            aba="PROCESSAMENTO",
            sub_aba="Sem Classificação",
            categoria="Sem classificação",
            ano=c
        )

        select = filtered[['aba', 'sub_aba', 'categoria', 'cultivar', f'{u}', 'ano']]
        select_sc = select.rename(columns={f'{u}': 'quantidade_kg', 'cultivar': 'produto'}).to_dict(orient='records')
        resultado.extend(select_sc)


    os.remove("ProcessaAmericanas.csv")
    os.remove("ProcessaViniferas.csv")
    os.remove("ProcessaMesa.csv")
    os.remove("ProcessaSemclass.csv")
    return resultado

def extrai_processamento():
    produtos = []
    sub_abas = ['Viniferas', 'Americanas e hibridas', 'Uvas de Mesa', 'Sem classificacao']
    for s in range(1,len(sub_abas) + 1):
        for i in range(1970, datetime.now().year):
        #for i in range(2022, 2023):
            url_processamento = f"http://vitibrasil.cnpuv.embrapa.br/index.php?ano={i}&opcao=opt_03&subopcao=subopt_0{s}"
            response = requests.get(url_processamento)
            soup = BeautifulSoup(response.text, 'html.parser')

            td = soup.findAll("td")
            valores_viniferas = []
            for t in td:
                if 'tb_item' in t.get('class', []) and t.text.isupper():
                    categoria = t.text.strip()
                    valores_viniferas.append("cat" + categoria)
                
                if 'tb_subitem' in t.get('class', []):
                    subitem = t.text.strip()
                    subitem = subitem.replace('.','')
                    subitem = subitem.replace('-','0')
                    subitem = subitem.replace('*','0')
                    valores_viniferas.append(subitem)
            
            #print(valores_viniferas)
            categoria_atual = []
            for item in valores_viniferas:
                if item.startswith("cat"):
                    categoria_atual = item[3:]
                else:
                    if item.isdigit():
                        valor = item
                        produto = produtos.pop()
                        produto = produto.encode('latin1').decode('utf-8', errors='ignore')
                        produtos.append({
                            'aba': 'PROCESSAMENTO',
                            'sub_aba': sub_abas[s-1],
                            'categoria': categoria_atual,
                            'produto': produto,
                            'quantidade_kg': valor,
                            'ano': i
                        })
                    else:
                        produtos.append(item)
            valores_viniferas = []

    return produtos


def try_route_processamento():
        try:
            return paliativo_processamento()
        except:
            return extrai_processamento()


# if __name__ == '__main__':
#     paliativo_processamento()