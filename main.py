from flask import Flask, jsonify
# importamos Flask

app= Flask(__name__)

@app.route('/personas', methods=['GET'])
#declaramos el metodo a utilizar
def index():
#definimos la funcion
    lista_personas = [
        {'name': 'Fabian julio Polanco'},
        {'name': 'Jineth Julio'},
        {'name': 'Maria Martinez'},
        {'name': 'Olga'}
    ]   
    return jsonify(lista_personas)
#retornamos los datos en formato Json

if __name__ == '__main__':
    app.run(debug=True)

