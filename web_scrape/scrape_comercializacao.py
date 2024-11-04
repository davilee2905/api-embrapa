import requests
from bs4 import BeautifulSoup
from datetime import datetime
import pandas as pd
import os 

def paliativo_comercializacao():
    url_download = "http://vitibrasil.cnpuv.embrapa.br/download/Comercio.csv"
    response = requests.get(url_download)
    if response.status_code == 200:
        with open('Comercio.csv', 'wb') as file:
            file.write(response.content)
        print("Arquivo salvo com sucesso !")
    else:
        print(f"Falha ao baixar arquivo.")
    
    csv_df = pd.read_csv("Comercio.csv", sep=';')
    colunas = csv_df.loc[:, 'Produto':].columns[1:].tolist()
    valores = []
    for i in colunas:
        csv_df = csv_df[csv_df['Produto'].str.isupper()].reset_index(drop=True)
        linhas = csv_df.shape[0]
        
        for x in range(linhas):  
            categoria = csv_df.iloc[x]['Produto']
            valor = csv_df.iloc[x][i].item()
            cat_append = {
                'categoria': categoria,
                'valor': valor,
                'ano': i
            }
            valores.append(cat_append)
        
        filtered_vm = csv_df[csv_df['control'].str.startswith("vm_", na=False)].copy()
        filtered_vm = filtered_vm[filtered_vm['control'].apply(lambda x: x != [])]
        filtered_vm = filtered_vm.assign(
            aba='COMERCIALIZACAO',
            categoria="VINHO DE MESA",
            ano=i
        )
        select_vm = filtered_vm[['aba', 'categoria', 'Produto', f'{i}', 'ano']]
        select_vm = select_vm.rename(columns={f'{i}': 'valor'}).to_dict(orient='records')
        valores.append(select_vm)

        filtered_ve = csv_df[csv_df['control'].str.startswith("ve_", na=False)].copy()
        filtered_ve = filtered_ve[filtered_ve['control'].apply(lambda x: x != [])]
        filtered_ve = filtered_ve.assign(
            aba='COMERCIALIZACAO',
            categoria="VINHO DE MESA",
            ano=i
        )
        select_ve = filtered_ve[['aba', 'categoria', 'Produto', f'{i}', 'ano']]
        select_ve = select_ve.rename(columns={f'{i}': 'valor'}).to_dict(orient='records')
        valores.append(select_ve)

        filtered_es = csv_df[csv_df['control'].str.startswith("es_", na=False)].copy()
        filtered_es = filtered_es[filtered_es['control'].apply(lambda x: x != [])]
        filtered_es = filtered_es.assign(
            aba='COMERCIALIZACAO',
            categoria="VINHO DE MESA",
            ano=i
        )
        select_es = filtered_es[['aba', 'categoria', 'Produto', f'{i}', 'ano']]
        select_es = select_es.rename(columns={f'{i}': 'valor'}).to_dict(orient='records')
        valores.append(select_es)

        filtered_su = csv_df[csv_df['control'].str.startswith("su_", na=False)].copy()
        filtered_su = filtered_su[filtered_su['control'].apply(lambda x: x != [])]
        filtered_su = filtered_su.assign(
            aba='COMERCIALIZACAO',
            categoria="VINHO DE MESA",
            ano=i
        )
        select_su = filtered_su[['aba', 'categoria', 'Produto', f'{i}', 'ano']]
        select_su = select_su.rename(columns={f'{i}': 'valor'}).to_dict(orient='records')
        valores.append(select_su)       

        filtered_ou = csv_df[csv_df['control'].str.startswith("ou_", na=False)].copy()
        filtered_ou = filtered_ou[filtered_ou['control'].apply(lambda x: x != [])]
        filtered_ou = filtered_ou.assign(
            aba='COMERCIALIZACAO',
            categoria="VINHO DE MESA",
            ano=i
        )
        select_ou = filtered_ou[['aba', 'categoria', 'Produto', f'{i}', 'ano']]
        select_ou = select_ou.rename(columns={f'{i}': 'valor'}).to_dict(orient='records')
        valores.append(select_ou)
    
        os.remove("Comercio.csv")
    return valores

def extrai_comercializacao():
    produtos = []
    for i in range(1970, datetime.now().year):
        url_comercializacao = f'http://vitibrasil.cnpuv.embrapa.br/index.php?ano={i}&opcao=opt_04'
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Trident/7.0; AS; rv:11.0) like Gecko"
        }

        response = requests.get(url_comercializacao, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')

        td = soup.findAll("td")
        valores = []
        valores_cat = []
        for t in td:
            if 'tb_item' in t.get('class', []):
                item = t.text.strip()
                item = item.replace('.','')
                item = item.replace('-','0')
                item = item.replace('*','0')
                valores_cat.append(f'{i}' + item)

            if 'tb_item' in t.get('class', []) and t.text.isupper():
                categoria = t.text.strip()  
                valores.append("cat" + categoria)
            
            if 'tb_subitem' in t.get('class', []):
                subitem = t.text.strip()
                subitem = subitem.replace('.','')
                subitem = subitem.replace('-','0')
                subitem = subitem.replace('*','0')
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
                            'aba': 'COMERCIALIZACAO',
                            'categoria': categoria_atual,
                            'produto': produto,
                            'quantidade_lt': valor,
                            'ano': i
                        })
                else:
                    produtos.append(item)
        valores = []
        for i in range(0, len(valores_cat), 2):
                ano_categoria = valores_cat[i][:4]
                categoria = valores_cat[i][4:]
                valor = valores_cat[i + 1] if i + 1 < len(valores_cat) else None  # Verifica se há um valor correspondente
                produtos.append({'categoria': categoria, 'valor': valor, 'ano': ano_categoria})
    

    return produtos


def try_route_comercializacao():
        try:
            return paliativo_comercializacao()
        except:
            return extrai_comercializacao()

# if __name__ == '__main__':
#     extrai_comercializacao()