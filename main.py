from flask import Flask, jsonify, request
from flask_jwt_extended import JWTManager, create_access_token, jwt_required
from web_scrape import scrape_producao, scrape_processamento, scrape_comercializacao, scrape_importacao, scrape_exportacao
import time
import requests
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

# Configuração do JWT
app.config['JWT_SECRET_KEY'] = os.getenv("JWT_KEY") 
jwt = JWTManager(app)

# Rota de autenticação para obter o token
@app.route('/login', methods=['POST'])
def login():
    username = request.json.get('username')
    password = request.json.get('password')
    
    ## AUTENTICAÇÃO BASICA (NAO UTILIZAVEL PROD) ##
    if username == os.getenv("USERNAME_API") and password == os.getenv("PASSWORD_API"):
        access_token = create_access_token(identity=username)
        return jsonify(access_token=access_token), 200
    return jsonify({"erro": "Usuário ou senha inválidos!"}), 401

@app.route('/producao', methods=['GET'])
@jwt_required()
def producao():
    tentativas = 5
    for i in range(tentativas):
        try:
            data = scrape_producao.try_route_producao()
            return jsonify(data)
        except Exception as e:
            time.sleep(5)
            print(f"Tentativa {i + 1} falhou: {e}")  
            if i == tentativas - 1:  
                return jsonify({"erro": "Quantidade de vezes excedida! Site fora do ar, tente novamente!"}), 500

@app.route('/processamento', methods=['GET'])
@jwt_required()
def processamento():
    tentativas = 5
    for i in range(tentativas):
        try:
            data = scrape_processamento.try_route_processamento()
            return jsonify(data) 
        except Exception as e:
            time.sleep(5)
            print(f"Tentativa {i + 1} falhou: {e}")  
            if i == tentativas - 1:  
                return jsonify({"erro": "Quantidade de vezes excedida! Site fora do ar, tente novamente!"}), 500

    return jsonify({"erro": "Um erro inesperado ocorreu."}), 500  # Caso ocorra algum erro não previsto

@app.route('/comercializacao', methods=['GET'])
@jwt_required()
def comercializacao():
    tentativas = 5
    for i in range(tentativas):
        try:
            data = scrape_comercializacao.try_route_comercializacao()
            return jsonify(data)
        except Exception as e:
            time.sleep(5)
            print(f"Tentativa {i + 1} falhou: {e}")  
            if i == tentativas - 1:  
                return jsonify({"erro": "Quantidade de vezes excedida! Site fora do ar, tente novamente!"}), 500
            
@app.route('/importacao', methods=['GET'])
@jwt_required()
def importacao():
    tentativas = 5 
    for i in range(tentativas):
        try:
            data = scrape_importacao.try_route_importacao()
            return jsonify(data)
        except Exception as e:
            print(f"Tentativa {i +1} falhou: {e}")
            if i == tentativas - 1:
                return jsonify({"erro": "Quantidade de vezes excedida! Site fora do ar, tente novamente!"}), 500

@app.route('/exportacao', methods=['GET'])
@jwt_required()
def exportacao():
    tentativas = 5 
    for i in range(tentativas):
        try:
            data = scrape_exportacao.try_route_exportacao()
            return jsonify(data)
        except Exception as e:
            print(f"Tentativa {i +1} falhou: {e}")
            if i == tentativas - 1:
                return jsonify({"erro": "Quantidade de vezes excedida! Site fora do ar, tente novamente!"}), 500


if __name__ == '__main__':
    app.run(debug=True)