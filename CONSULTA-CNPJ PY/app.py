from flask import Flask, render_template, request
import http.client
import json
import os
import sys

app = Flask(__name__, template_folder=os.path.join(sys._MEIPASS, 'templates'))

def get_cnpj_data(cnpj):
    conn = http.client.HTTPSConnection("receitaws.com.br")
    headers = { 'Accept': "application/json" }
    conn.request("GET", f"/v1/cnpj/{cnpj}", headers=headers)
    res = conn.getresponse()
    data = res.read()
    return json.loads(data.decode("utf-8"))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/debug', methods=['GET'])
def debug():
    return "Rota GET funcionando!"

@app.route('/search', methods=['POST'])
def search():
    cnpj = request.form['cnpj']
    print(f"Received CNPJ: {cnpj}")
    json_data = get_cnpj_data(cnpj)
    
    data = {
        'nome': json_data.get("nome", "Não disponível"),
        'fantasia': json_data.get("fantasia", "Não disponível"),
        'cnpj': json_data.get("cnpj", "Não disponível"),
        'abertura': json_data.get("abertura", "Não disponível"),
        'situacao': json_data.get("situacao", "Não disponível"),
        'endereco': f"{json_data.get('logradouro', 'Não disponível')}, {json_data.get('numero', 'Não disponível')}, {json_data.get('bairro', 'Não disponível')}, {json_data.get('municipio', 'Não disponível')}, {json_data.get('uf', 'Não disponível')}, {json_data.get('cep', 'Não disponível')}",
        'atividade_principal': json_data.get("atividade_principal", [{}])[0].get("text", "Não disponível"),
        'capital_social': json_data.get("capital_social", "Não disponível"),
    }

    return render_template('result.html', data=data)

if __name__ == '__main__':
    app.run(port=5500, debug=True)