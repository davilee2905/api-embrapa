from bs4 import BeautifulSoup
import requests
import json
from datetime import datetime 
import pandas as pd
import os

def paliativo_producao():
    url_download = "http://vitibrasil.cnpuv.embrapa.br/download/Producao.csv"
    response = requests.get(url_download)

    if response.status_code == 200:
        with open('Producao.csv', 'wb') as file:
            file.write(response.content)
        print("Arquivo salvo com sucesso !")
    else:
        print(f"Falha ao baixar arquivo.")
    
    csv_df = pd.read_csv("Producao.csv", sep=';')
    colunas = csv_df.loc[:, 'produto':].columns[1:].tolist()
    resultado = []
    for i in colunas:
        filtered_vm = csv_df[csv_df['control'].str.startswith('vm_')].copy()
        filtered_vm = filtered_vm.assign(
            aba="PRODUCAO",
            categoria="VINHO DE MESA",
            ano=i
        )
        select_vm = filtered_vm[['aba', 'categoria', 'produto', f'{i}', 'ano']]
        select_vm = select_vm.rename(columns={f'{i}': 'quantidade_lt'}).to_dict(orient='records')
        resultado.extend(select_vm)

        filtered_vv = csv_df[csv_df['control'].str.startswith('vv_')].copy()
        filtered_vv = filtered_vv.assign(
            aba="PRODUCAO",
            categoria="VINHO FINO DE MESA (VINIFERA)",
            ano = i
        )
        select_vv = filtered_vv[['aba', 'categoria', 'produto', f'{i}', 'ano']]
        select_vv = select_vv.rename(columns={f'{i}': 'quantidade_lt'}).to_dict(orient='records')
        resultado.extend(select_vv)

        filtered_su = csv_df[csv_df['control'].str.startswith('su_')].copy()
        filtered_su = filtered_su.assign(
            aba="PRODUCAO",
            categoria="SUCO",
            ano=i
        )
        select_su = filtered_su[['aba','categoria','produto',f'{i}','ano']]
        select_su = select_su.rename(columns={f'{i}': 'quantidade_lt'}).to_dict(orient='records')
        resultado.extend(select_su)

        filtered_de = csv_df[csv_df['control'].str.startswith('de_')].copy()
        filtered_de = filtered_de.assign(
            aba="PRODUCAO",
            categoria="DERIVADOS",
            ano=i
        )
        select_de = filtered_de[['aba', 'categoria','produto', f'{i}', 'ano']]
        select_de = select_de.rename(columns={f'{i}': 'quantidade_lt'}).to_dict(orient='records')
        resultado.extend(select_de)

    os.remove('Producao.csv')
    return resultado

def extrai_producao():
    produtos = []
    for i in range(1970, datetime.now().year()):
        url_producao = f"http://vitibrasil.cnpuv.embrapa.br/index.php?ano={i}&opcao=opt_02"
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Trident/7.0; AS; rv:11.0) like Gecko"
        }

        response = requests.get(url_producao, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        td = soup.findAll("td")
        valores = []
        for t in td:
            if 'tb_item' in t.get('class', []) and t.text.isupper():
                categoria = t.text.strip()
                valores.append("cat" + categoria)
        
            if 'tb_subitem' in t.get('class', []):
                subitem = t.text.strip()
                subitem = subitem.replace('.','')
                subitem = subitem.replace('-','0')
                valores.append(subitem)
        
        categoria_atual = []
        for item in valores:
            if item.startswith("cat"):
                categoria_atual = item[3:]
            else:
                if item.isdigit():
                    valor = item
                    produto = produtos.pop()
                    produtos.append({
                        'aba': 'PRODUCAO',
                        'categoria': categoria_atual,
                        'produto': produto.encode('latin1').decode('utf-8', errors='ignore'),
                        'quantidade_lt': valor,
                        'ano': i
                    })
                else:
                    produtos.append(item)
        valores = []
        
    return produtos

def try_route_producao():
        try:
            return extrai_producao()
        except:
            return paliativo_producao()

if __name__ == '__main__':
    try_route_producao()