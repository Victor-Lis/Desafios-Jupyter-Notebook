from flask import Flask, request, jsonify

app = Flask(__name__)

# Criando a função de cálculo (lógica do exercicio10.ipynb)
def calcular_preco_passagem(distancia):
    """
    Calcula o preço da passagem com base na distância.
    - R$ 0.50/km para viagens de até 200 km.
    - R$ 0.45/km para viagens mais longas.
    """
    if distancia < 200:
        custo = distancia * 0.50
    else:
        custo = distancia * 0.45
    return custo

# Definindo a rota (endpoint) da nossa API
@app.route('/calcular-passagem', methods=['GET'])
def api_calcular_passagem():
    
    distancia_str = request.args.get('distancia')

    if not distancia_str:
        return jsonify({"erro": "O parâmetro 'distancia' é obrigatório."}), 400
    
    try:
        distancia_float = float(distancia_str)
    except ValueError:
        return jsonify({"erro": "O valor de 'distancia' deve ser um número."}), 400

    preco = calcular_preco_passagem(distancia_float)

    return jsonify({
        "distancia_km": distancia_float,
        "preco_passagem_R$": round(preco, 2)
    })

if __name__ == '__main__':
    app.run(debug=True)