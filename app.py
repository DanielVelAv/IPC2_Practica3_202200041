from flask import Flask,jsonify,request
from flask_cors import CORS
from collections import namedtuple

app = Flask(__name__)
CORS(app)

Peliculas = namedtuple("Peliculas",["movield","nombre","genero"])
Movies = []

@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'

@app.route('/api/new-movie/',methods=['POST'])
def peliculaNueva():
    if request.method == 'POST':
        Id = request.json['movieId']
        nombre = request.json['name']
        genero = request.json['genre']
        Peli = Peliculas(Id,nombre,genero)
        Movies.append(Peli)
        return jsonify({"message":"Pelicula Ingresada correctamente"})

@app.route('/api/all-movies-by-genre/<genero>',methods=['GET'])
def filtroGenero(genero):
    genre = genero
    concat = ""
    for i in range(len(Movies)):
        if Movies[i][2] == genre:
            concat += f'{Movies[i][1]}' + " , "
    return jsonify({"message":genre,"peliculas":concat})

@app.route('/api/update-movie',methods=['PUT'])
def updateMovie():
    if request.method == 'PUT':
        IdNuevo = request.json['movieId']
        NombreNuevo = request.json['name']
        GeneroNuevo = request.json['genre']

        for i in range(len(Movies)):
            if Movies[i][0] == IdNuevo:
                Movies[i][1] == NombreNuevo
                Movies[i][2] == GeneroNuevo
                return jsonify({"message":"Los datos se han actualizado Exitosamente","idk":NombreNuevo})
            else:
                return jsonify({"message":"no se encontro la pelicula"})


if __name__ == '__main__':
    app.run(debug=True, port=8000)
