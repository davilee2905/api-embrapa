from bs4 import BeautifulSoup
import requests
from datetime import datetime
import os
import pandas as pd

def paliativo_exportacao():
    resultado = []
    ## Vinhos de Mesa ##
    url_download = "http://vitibrasil.cnpuv.embrapa.br/download/ExpVinho.csv"
    response = requests.get(url_download)

    if response.status_code == 200:
        with open("ExpVinho.csv", 'wb') as file:
            file.write(response.content)
            print("Arquivo ExpVinho salvo com sucesso !")
    else:
        print("Falha ao salvar arquivo ExpVinho")

    csv_df = pd.read_csv('ExpVinho.csv', sep=';')
    for i in range(1970, datetime.now().year):
        csv_df = csv_df.rename(columns={f'{i}': f'quantidade_kg{i}', f'{i}.1': f'valor_dolar{i}'})
        csv_df = csv_df.assign(
            aba='EXPORTACAO',
            ano=i,
            categoria="Vinhos de Mesa"
        )

        selected1 = csv_df[['aba', 'ano', 'categoria', 'País', f'quantidade_kg{i}', f'valor_dolar{i}']]
        selected1 = selected1.rename(columns={f'quantidade_kg{i}': 'quantidade_kg', f'valor_dolar{i}':'valor_dolar', 'País': 'pais'}).to_dict(orient='records')
        resultado.extend(selected1)
    
    ## Espumantes ##
    url_download2 = "http://vitibrasil.cnpuv.embrapa.br/download/ExpEspumantes.csv"
    response = requests.get(url_download2)

    if response.status_code == 200:
        with open('ExpEspumantes.csv', 'wb') as file:
            file.write(response.content)
        print("Arquivo ExpEspumantes salvo com sucesso !")
    else:
        print(f"Falha ao baixar arquivo ExpEspumantes.")
    
    csv_df2 = pd.read_csv('ExpEspumantes.csv', sep=';')
    for i in range(1970, datetime.now().year):
        ##csv_df2['País'] = csv_df2['País'].str.encode('utf-8').str.decode('unicode_escape')
        csv_df2 = csv_df2.rename(columns={f'{i}': f'quantidade_kg{i}', f'{i}.1': f'valor_dolar{i}'})
        csv_df2 = csv_df2.assign(
            aba='EXPORTACAO',
            ano=i,
            categoria="Espumantes"
        )

        selected2 = csv_df2[['aba', 'ano', 'categoria', 'País', f'quantidade_kg{i}', f'valor_dolar{i}']]
        selected2 = selected2.rename(columns={f'quantidade_kg{i}': 'quantidade_kg', f'valor_dolar{i}':'valor_dolar', 'País': 'pais'}).to_dict(orient='records')
        resultado.extend(selected2)
    
    ## Uvas Frescas ##
    url_download3 = "http://vitibrasil.cnpuv.embrapa.br/download/ExpUva.csv"
    response = requests.get(url_download3)

    if response.status_code == 200:
        with open("ExpUva.csv", 'wb') as file:
            file.write(response.content)
            print("Arquivo Exp.Uva salvo com sucesso !")
    else:
        print(f"Falha ao baixar arquivo Exp.Uva.")

    csv_df3 = pd.read_csv("ExpUva.csv", sep=";")
    for i in range(1970, datetime.now().year):
        csv_df3 = csv_df3.rename(columns={f'{i}': f'quantidade_kg{i}', f'{i}.1': f'valor_dolar{i}'})
        csv_df3 = csv_df3.assign(
            aba='EXPORTACAO',
            ano=i,
            categoria="Uvas Frescas"
        )

        selected3 = csv_df3[['aba', 'ano', 'categoria', 'País', f'quantidade_kg{i}', f'valor_dolar{i}']]
        selected3 = selected3.rename(columns={f'quantidade_kg{i}': 'quantidade_kg', f'valor_dolar{i}':'valor_dolar', 'País': 'pais'}).to_dict(orient='records')
    
        resultado.extend(selected3)
    
    ## Suco de Uva ##
    url_download5 = "http://vitibrasil.cnpuv.embrapa.br/download/ExpSuco.csv"
    response = requests.get(url_download5)
    
    if response.status_code == 200:
        with open("ExpSuco.csv", 'wb') as file:
            file.write(response.content)
            print("Arquivo ExpSuco salvo com sucesso !")
    else:
        print("Arquivo ExpSuco com erro !")
    
    csv_df5 = pd.read_csv("ExpSuco.csv", sep=';')
    for i in range(1970, datetime.now().year):
        csv_df5 = csv_df5.rename(columns={f'{i}': f'quantidade_kg{i}', f'{i}.1': f'valor_dolar{i}'})
        csv_df5 = csv_df5.assign(
            aba='EXPORTACAO',
            ano=i,
            categoria="Suco de Uva"
        )

        selected5 = csv_df5[['aba', 'ano', 'categoria', 'País', f'quantidade_kg{i}', f'valor_dolar{i}']]
        selected5 = selected5.rename(columns={f'quantidade_kg{i}': 'quantidade_kg', f'valor_dolar{i}':'valor_dolar', 'País': 'pais'}).to_dict(orient='records')
    
        resultado.extend(selected5)
    
    os.remove("ExpEspumantes.csv")
    os.remove("ExpSuco.csv")
    os.remove("ExpUva.csv")
    os.remove("ExpVinho.csv")

    return resultado

def extrai_exportacao():
    sub_abas = ['Vinhos de Mesa', 'Espumantes', 'Uvas Frescas', 'Suco de Uva']
    resultados = []
    for s in range(1, len(sub_abas) + 1):
        for i in range(1970, datetime.now().year):
            url_exportacao = f"http://vitibrasil.cnpuv.embrapa.br/index.php?ano={i}&opcao=opt_06&subopcao=subopt_0{s}"
            response = requests.get(url_exportacao)
            soup = BeautifulSoup(response.text, 'html.parser')

            tables = soup.findAll(class_="tb_base tb_dados")
            valores = []
            for t in tables:
                td = t.findAll("td")
                for d in td:
                    if len(d.text.strip()) <= 50:
                        item = d.text.strip()
                        item = item.replace('.','')
                        item = item.replace('-','0')
                        valores.append(item)

            for x in range(0, len(valores), 3):
                pais = valores[x]
                quantidade_kg = valores[x + 1]
                valor_dolar   = valores[x + 2]

                resultados.append({
                    'aba': 'EXPORTACAO',
                    'categoria': sub_abas[s -1],
                    'pais': pais,
                    'quantidade_kg': quantidade_kg,
                    'valor_dolar': valor_dolar,
                    'ano': i
                })

    return resultados

def try_route_exportacao():
        try:
            return paliativo_exportacao()
        except:
            return extrai_exportacao()

# if __name__ == '__main__':
#     paliativo_exportacao()