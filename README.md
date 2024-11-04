## Api-embrapa (tech challenge)
Esta API é um projeto TECH Challenge da Pós-TECH FIAP, aqui, os dados são extraídos diretamente do site da Embrapa e disponibilizados em formato JSON.

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
