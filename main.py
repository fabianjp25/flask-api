from flask import Flask, jsonify


app= Flask(__name__)

@app.route('/personas', methods=['GET'])
def index():
    lista_personas = [
        {'name': 'Fabian julio Polanco'},
        {'name': 'Jineth Julio'},
        {'name': 'Maria Martinez'},
        {'name': 'Olga'}
    ]   
    return jsonify(lista_personas)

if __name__ == '__main__':
    app.run(debug=True)

