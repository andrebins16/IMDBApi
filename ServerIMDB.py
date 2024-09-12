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
            movie = {
                "Id": globalId,
                "Series_Title": row["Series_Title"],
                "Genre": row["Genre"],
                "IMDB_Rating": row["IMDB_Rating"],
                "Overview": row["Overview"],
                "Runtime": row["Runtime"],
                "Director": row["Director"],
                "Star1": row["Star1"],
                "Star2": row["Star2"],
                "Released_Year": row["Released_Year"],
            }
            auxMovies.append(movie)
            globalId += 1
        return auxMovies

@app.get("/movies")
def getMovies():
    return jsonify(moviesRepo), 200

@app.get("/movie/<int:id>")
def getMovieById(id):
    for movie in moviesRepo:
        if movie["Id"] == id:
            return jsonify(movie), 200
    return {"erro": "Filme nao encontrado"}, 404

@app.delete("/movie/<int:id>")
def deleteMovieById(id):
    for movie in moviesRepo:
        if(movie["Id"] == id):
            moviesRepo.remove(movie)
            return "Filme removido", 200
    return {"erro": 'Filme nao encontrado'}, 404

@app.post("/movie")
def addMovie():
    global globalId
    if request.is_json:
        body = request.get_json()
        try:
            auxMovie = {
                "Id": globalId,
                "Series_Title": body["Series_Title"],
                "Genre": body["Genre"],
                "IMDB_Rating": body["IMDB_Rating"],
                "Overview": body["Overview"],
                "Runtime": body["Runtime"],
                "Director": body["Director"],
                "Star1": body["Star1"],
                "Star2": body["Star2"],
                "Released_Year": body["Released_Year"],
            }
        except:
            return {"erro":"Formato do JSON inválido"}, 400
        if len(body) > 9:
            return {"erro":"Formato do JSON inválido"}, 400
        moviesRepo.append(auxMovie)
        globalId += 1
        return {'id':auxMovie["Id"]}, 201
    else:
        return {"erro":"Formato deve ser JSON"}, 415
    
@app.patch("/movie/<int:id>")
def updateMovie(id):
    allowedKeys = {"Series_Title", "Genre", "IMDB_Rating", "Overview", "Runtime", "Director", "Star1", "Star2", "Released_Year"}

    global globalId
    if request.is_json:
        body = request.get_json()

        for key in body.keys():
            if key not in allowedKeys:
                return {"erro":"Formato do JSON inválido"}, 400

        for movie in moviesRepo:
            if movie["Id"] == id:
                if "Series_Title" in body:
                    movie["Series_Title"]=body["Series_Title"]
                if "Genre" in body:
                    movie["Genre"]=body["Genre"]
                if "IMDB_Rating" in body:
                    movie["IMDB_Rating"]=body["IMDB_Rating"]
                if "Overview" in body:
                    movie["Overview"]=body["Overview"]
                if "Runtime" in body:
                    movie["Runtime"]=body["Runtime"]
                if "Director" in body:
                    movie["Director"]=body["Director"]
                if "Star1" in body:
                    movie["Star1"]=body["Star1"]
                if "Star2" in body:
                    movie["Star2"]=body["Star2"]
                if "Released_Year" in body:
                    movie["Released_Year"]=body["Released_Year"]
                return "Filme atualizado",200
        return {"erro": 'Filme nao encontrado'}, 404
    else:
             return {"erro":"Formato deve ser JSON"}, 415

if __name__ == "__main__":
    moviesRepo = read_movies_from_csv("imdb_top_1000.csv")
    app.run()