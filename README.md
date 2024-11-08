## Api-embrapa (tech challenge)
Esta API é um projeto TECH Challenge da Pós-TECH FIAP, aqui, os dados são extraídos diretamente do site da Embrapa e disponibilizados em formato JSON.
Cada rota descrita no projeto possui 2 formas de extração, sendo a primeira a partir do site, utilizando o BeautifulSoup ou pelo link de download CSV.

## Estrutura do projeto
```
api-embrapa/
│
├── web_scrape/                  
│   ├── scrape_comercializacao.py
│   ├── scrape_exportacao.py
│   ├── scrape_importacao.py
│   └── scrape_processamento.py
│   └── scrape_producao.py
|
├── README.md
├── main.py
└── requirements.txt
```

## Tecnologias Utilizadas ##

- **Linguagem:** Python
- **Framework:** Flask
- **Bibliotecas:** Requests, flask_jwt_extended, pandas, python-dotenv, beautifulsoup4.

## Instalação ##

1. Clone o repositório dentro de sua pasta.
```
git clone https://github.com/davilee2905/api-embrapa.git
```

2. Crie um ambiente virtual. (Opcional, mas recomendado)

```
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

3. Navegue até o repositório.

```
cd api-embrapa
```

4. Instale as dependências.
```
pip install -r requirements.txt
```

5. Rode a API.
```
python3 main.py
```

As rotas estão protegidas pelo JWT.
Não esqueça de disponibilizar no seu código interno um arquivo ".env" com as credenciais que deseja utilizar.
Sendo elas: "JWT_SECRET_KEY", "USERNAME_API", "PASSWORD_API".

## Endpoints ##

- **/login**
Esta rota está disponível por conta da autenticação JWT, utilizada para obter o token de acesso.

- **/producao**
Rota protegida por JWT, retorna os dados JSON da aba Produção.

- **/processamento**
Rota protegida por JWT, retorna os dados JSON da aba Processamento.

- **/comercializacao**
Rota protegida por JWT, retorna os dados JSON da aba Comercialização.

- **/importacao**
Rota protegida por JWT, retorna os dados JSON da aba Importação.

- **/exportacao**
Rota protegida por JWT, retorna os dados JSON da aba Exportação.

## Exemplo de Resposta ##

```
{
  "aba": "PRODUCAO",
  "ano": "1997",
  "categoria": "DERIVADOS",
  "produto": "Espumante",
  "quantidade_lt": 0
},
{
  "aba": "PRODUCAO",
  "ano": "1997",
  "categoria": "DERIVADOS",
  "produto": "Espumante moscatel",
  "quantidade_lt": 0
},
{
  "aba": "PRODUCAO",
  "ano": "1997",
  "categoria": "DERIVADOS",
  "produto": "Base espumante",
  "quantidade_lt": 0
}...
```
