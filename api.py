from flask import Flask, request, jsonify
import pickle
import pandas as pd

app = Flask(__name__)

# Carrega o modelo Random Forest previamente treinado
with open('random_forest_model.pkl', 'rb') as model_file:
    modelo = pickle.load(model_file)

# Carrega a estrutura das colunas usadas no treinamento
with open('colunas_treinamento.pkl', 'rb') as colunas_file:
    colunas_treinamento = pickle.load(colunas_file)

# Carrega os LabelEncoders, se necessário
try:
    with open('label_encoders.pkl', 'rb') as encoders_file:
        label_encoders = pickle.load(encoders_file)
except FileNotFoundError:
    label_encoders = None  # Caso não seja necessário

# Função para preprocessar a entrada de acordo com o treinamento
def preprocessar_dados(nome_peca, problema, quilometragem, condicoes_uso):
    dados = {
        'Nome da Peça': [nome_peca],
        'Sinal': [problema],
        'Quilometragem': [quilometragem],
        'Condições de Uso': [condicoes_uso]
    }
    entrada = pd.DataFrame(dados)
    
    # Aplica os encoders, se houver
    if label_encoders:
        for coluna in ['Nome da Peça', 'Sinal', 'Condições de Uso']:
            entrada[coluna] = label_encoders[coluna].transform(entrada[coluna])

    # Converte variáveis categóricas em variáveis dummy para combinar com as colunas de treinamento
    entrada = pd.get_dummies(entrada)
    
    # Garante que todas as colunas esperadas estejam presentes
    entrada = entrada.reindex(columns=colunas_treinamento, fill_value=0)
    
    return entrada

@app.route('/prever', methods=['POST'])
def prever():
    # Extrai os dados enviados no corpo da requisição
    dados_requisicao = request.get_json()
    nome_peca = dados_requisicao.get('nome_peca')
    problema = dados_requisicao.get('problema')
    quilometragem = dados_requisicao.get('quilometragem')
    condicoes_uso = dados_requisicao.get('condicoes_uso')
    
    # Preprocessa os dados para que estejam no formato esperado pelo modelo
    entrada_preprocessada = preprocessar_dados(nome_peca, problema, quilometragem, condicoes_uso)
    
    # Realiza a previsão
    predicao = modelo.predict(entrada_preprocessada)[0]
    
    # Converte a previsão para um rótulo legível, se necessário
    if label_encoders and 'Resultado' in label_encoders:
        predicao = label_encoders['Resultado'].inverse_transform([predicao])[0]
    
    # Retorna o resultado como JSON
    return jsonify({'resultado': predicao})

if __name__ == "__main__":
    app.run(debug=True)
