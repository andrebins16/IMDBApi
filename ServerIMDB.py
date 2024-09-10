from flask import Flask, jsonify, request
import csv
   
app = Flask(__name__)
moviesRepo =[]
globalId = 0

def read_movies_from_csv(file_path):
    auxMovies = []
    global globalId
    with open(file_path, mode='r', encoding='utf-8') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            row["id"]=globalId
            auxMovies.append(row)
            globalId += 1
        return auxMovies

@app.get("/movies")
def getMovies():
    return jsonify(moviesRepo), 200

@app.get("/movie/<int:id>")
def getMovieById(id):
    for movie in moviesRepo:
        if movie["id"] == id:
            return jsonify(movie), 200
    return {"erro": "Filme nao encontrado"}, 404

@app.delete("/movie/<int:id>")
def deleteMovieById(id):
    for movie in moviesRepo:
        if(movie["id"] == id):
            moviesRepo.remove(movie)
            return "Filme removido", 200
    return {"erro": 'Filme nao encontrado'}, 404

@app.post("/movie")
def addMovie():
    global globalId
    if request.is_json:
        auxMovie = request.get_json()
        auxMovie["id"]=globalId
        moviesRepo.append(auxMovie)
        globalId += 1
        return {'id':auxMovie["id"]}, 201
    else:
        return {"erro":"Formato deve ser JSON"}, 415
    
@app.put("/movie/<int:id>")
def updateMovie(id):
    global globalId
    if request.is_json:
        auxMovie = request.get_json()
        for movie in moviesRepo:
            if movie["id"] == id:
                moviesRepo.remove(movie)
                auxMovie["id"]=id
                moviesRepo.append(auxMovie)
                return "Filme atualizado",200
            
        return {"erro": 'Filme nao encontrado'}, 404

    else:
             return {"erro":"Formato deve ser JSON"}, 415

if __name__ == "__main__":
    moviesRepo = read_movies_from_csv("imdb_top_1000.csv")
    for movie in moviesRepo:
        print(movie)
        print("\n")
    app.run()