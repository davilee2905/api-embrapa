from bs4 import BeautifulSoup
import requests
from datetime import datetime
import os
import pandas as pd

def paliativo_importacao():
    resultado = []
    ################################## Vinhos de Mesa ##############################################
    url_download = "http://vitibrasil.cnpuv.embrapa.br/download/ImpVinhos.csv"
    response = requests.get(url_download)

    if response.status_code == 200:
        with open('ImpVinhos.csv', 'wb') as file:
            file.write(response.content)
        print("Arquivo Imp.Vinhos de Mesa salvo com sucesso !")
    else:
        print(f"Falha ao baixar arquivo Imp.Vinhos de Mesa.")

    csv_df = pd.read_csv('ImpVinhos.csv', sep=';')
    for i in range(1970, datetime.now().year):
        csv_df = csv_df.rename(columns={f'{i}': f'quantidade_kg{i}', f'{i}.1': f'valor_dolar{i}'})
        csv_df = csv_df.assign(
            aba='IMPORTACAO',
            ano=i,
            categoria="Vinhos de Mesa"
        )

        selected1 = csv_df[['aba', 'ano', 'categoria', 'País', f'quantidade_kg{i}', f'valor_dolar{i}']]
        selected1 = selected1.rename(columns={f'quantidade_kg{i}': 'quantidade_kg', f'valor_dolar{i}':'valor_dolar', 'País': 'pais'}).to_dict(orient='records')
        resultado.extend(selected1)
    

    ################################## Espumantes ##############################################
    url_download2 = "http://vitibrasil.cnpuv.embrapa.br/download/ImpEspumantes.csv"
    response = requests.get(url_download2)

    if response.status_code == 200:
        with open('ImpEspumantes.csv', 'wb') as file:
            file.write(response.content)
        print("Arquivo Imp.Espumantes salvo com sucesso !")
    else:
        print(f"Falha ao baixar arquivo Imp.Espumantes.")
    
    csv_df2 = pd.read_csv('ImpEspumantes.csv', sep=';')
    for i in range(1970, datetime.now().year):
        ##csv_df2['País'] = csv_df2['País'].str.encode('utf-8').str.decode('unicode_escape')
        csv_df2 = csv_df2.rename(columns={f'{i}': f'quantidade_kg{i}', f'{i}.1': f'valor_dolar{i}'})
        csv_df2 = csv_df2.assign(
            aba='IMPORTACAO',
            ano=i,
            categoria="Espumantes"
        )

        selected2 = csv_df2[['aba', 'ano', 'categoria', 'País', f'quantidade_kg{i}', f'valor_dolar{i}']]
        selected2 = selected2.rename(columns={f'quantidade_kg{i}': 'quantidade_kg', f'valor_dolar{i}':'valor_dolar', 'País': 'pais'}).to_dict(orient='records')
        resultado.extend(selected2)

    ################################## Uvas frescas ##############################################
    url_download3 = "http://vitibrasil.cnpuv.embrapa.br/download/ImpFrescas.csv"
    response = requests.get(url_download3)

    if response.status_code == 200:
        with open("ImpFrescas.csv", 'wb') as file:
            file.write(response.content)
            print("Arquivo Imp.Frescas salvo com sucesso !")
    else:
        print(f"Falha ao baixar arquivo Imp.Frescas.")

    csv_df3 = pd.read_csv("ImpFrescas.csv", sep=";")
    for i in range(1970, datetime.now().year):
        csv_df3 = csv_df3.rename(columns={f'{i}': f'quantidade_kg{i}', f'{i}.1': f'valor_dolar{i}'})
        csv_df3 = csv_df3.assign(
            aba='IMPORTACAO',
            ano=i,
            categoria="Uvas Frescas"
        )

        selected3 = csv_df3[['aba', 'ano', 'categoria', 'País', f'quantidade_kg{i}', f'valor_dolar{i}']]
        selected3 = selected3.rename(columns={f'quantidade_kg{i}': 'quantidade_kg', f'valor_dolar{i}':'valor_dolar', 'País': 'pais'}).to_dict(orient='records')
    
        resultado.extend(selected3)

    ################################## Uvas frescas ##############################################
    url_download4 = "http://vitibrasil.cnpuv.embrapa.br/download/ImpPassas.csv"
    response = requests.get(url_download4)

    if response.status_code == 200:
        with open("ImpPassas.csv", "wb") as file:
            file.write(response.content)
            print("Arquivo ImpPassas salvo com sucesso !")
    else:
        print("Falha ao salvar arquivo ImpPassas.")

    csv_df4 = pd.read_csv("ImpPassas.csv", sep=';')
    for i in range(1970, datetime.now().year):
        csv_df4 = csv_df4.rename(columns={f'{i}': f'quantidade_kg{i}', f'{i}.1': f'valor_dolar{i}'})
        csv_df4 = csv_df.assign(
            aba='IMPORTACAO',
            ano=i,
            categoria="Uvas Passas"
        )

        selected4 = csv_df4[['aba', 'ano', 'categoria', 'País', f'quantidade_kg{i}', f'valor_dolar{i}']]
        selected4 = selected4.rename(columns={f'quantidade_kg{i}': 'quantidade_kg', f'valor_dolar{i}':'valor_dolar', 'País': 'pais'}).to_dict(orient='records')
    
        resultado.extend(selected4)


    ################################## Suco de uva ##############################################
    url_download5 = "http://vitibrasil.cnpuv.embrapa.br/download/ImpSuco.csv"
    response = requests.get(url_download5)
    
    if response.status_code == 200:
        with open("ImpSuco.csv", 'wb') as file:
            file.write(response.content)
            print("Arquivo ImpSuco salvo com sucesso !")
    else:
        print("Arquivo ImpPassas com erro !")
    
    csv_df5 = pd.read_csv("ImpPassas.csv", sep=';')
    for i in range(1970, datetime.now().year):
        csv_df5 = csv_df5.rename(columns={f'{i}': f'quantidade_kg{i}', f'{i}.1': f'valor_dolar{i}'})
        csv_df5 = csv_df5.assign(
            aba='IMPORTACAO',
            ano=i,
            categoria="Suco de Uva"
        )

        selected5 = csv_df5[['aba', 'ano', 'categoria', 'País', f'quantidade_kg{i}', f'valor_dolar{i}']]
        selected5 = selected5.rename(columns={f'quantidade_kg{i}': 'quantidade_kg', f'valor_dolar{i}':'valor_dolar', 'País': 'pais'}).to_dict(orient='records')
    
        resultado.extend(selected5)

    os.remove("ImpEspumantes.csv")
    os.remove("ImpFrescas.csv")
    os.remove("ImpVinhos.csv")
    os.remove("ImpPassas.csv")
    os.remove("ImpSuco.csv")
    return resultado

def extrai_importacao():
    sub_abas = ['Vinhos de Mesa','Espumantes','Uvas Frescas','Uvas Passas', 'Suco de uva']
    resultados = []
    for s in range(1, len(sub_abas) + 1):
        for i in range(1970, datetime.now().year):
            url_processamento = f'http://vitibrasil.cnpuv.embrapa.br/index.php?ano={i}&opcao=opt_05&subopcao=subopt_0{s}'
            response = requests.get(url_processamento)
            soup = BeautifulSoup(response.text,'html.parser')

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
                    'aba': 'IMPORTACAO',
                    'categoria': sub_abas[s -1],
                    'pais': pais,
                    'quantidade_kg': quantidade_kg,
                    'valor_dolar': valor_dolar,
                    'ano': i
                })

    return resultados


def try_route_importacao():
        try:
            return paliativo_importacao()
        except:
            return extrai_importacao()


# if __name__ == "__main__":
#     paliativo_importacao()