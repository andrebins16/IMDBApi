from flask import Flask, jsonify, request
import csv
class Movie:
    def __init__(self, id,poster_link, series_title, released_year, certificate, runtime, genre, imdb_rating, overview, meta_score, director, star1, star2, star3, star4, no_of_votes, gross):
        self.id = id
        self.poster_link = poster_link
        self.series_title = series_title
        self.released_year = released_year
        self.certificate = certificate
        self.runtime = runtime
        self.genre = genre
        self.imdb_rating = imdb_rating
        self.overview = overview
        self.meta_score = meta_score
        self.director = director
        self.star1 = star1
        self.star2 = star2
        self.star3 = star3
        self.star4 = star4
        self.no_of_votes = no_of_votes
        self.gross = gross

    def __str__(self):
        return f"<Movie {self.series_title} ({self.released_year})>"
    

app = Flask(__name__)
moviesRepo =[]
globalId = 0

def read_movies_from_csv(file_path):
    auxMovies = []
    global globalId
    with open(file_path, mode='r', encoding='utf-8') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            poster_link=row['Poster_Link']
            series_title=row['Series_Title']
            released_year=int(row['Released_Year'])
            certificate=row['Certificate'] if row['Certificate'] else None
            runtime=int(row['Runtime'].split()[0])
            genre=row['Genre']
            imdb_rating=float(row['IMDB_Rating'])
            overview=row['Overview']
            meta_score=int(row['Meta_score']) if row['Meta_score'] else None
            director=row['Director']
            star1=row['Star1']
            star2=row['Star2']
            star3=row['Star3']
            star4=row['Star4']
            no_of_votes=int(row['No_of_Votes'])
            gross=float(row['Gross'].replace(',', '')) if row['Gross'] else None
            newMovie = Movie(globalId,poster_link,series_title,released_year,certificate,runtime,genre,imdb_rating,overview,meta_score,director,star1,star2,star3,star4,no_of_votes,gross)
            auxMovies.append(newMovie)
            globalId += 1
        return auxMovies

@app.get("/movies")
def getMovies():
    return jsonify(list(map(lambda elem: elem.__dict__, moviesRepo))), 200

@app.get("/movies/<int:id>")
def getMovieById(id):
    for movie in moviesRepo:
        if movie.id == id:
            return jsonify(movie.__dict__), 200
    return {"erro": "Filme nao encontrado"}, 404

@app.delete("/movies/<int:id>")
def deleteMovieById(id):
    for movie in moviesRepo:
        if(movie.id == id):
            moviesRepo.remove(movie)
            return "Filme removido", 200
    return {"erro": 'Filme nao encontrado'}, 404

@app.post("/movies/add")
def addMovie():
    global globalId
    if request.is_json:
        auxMovie = request.get_json()

        poster_link=auxMovie['poster_link'] if auxMovie['poster_link'] else None
        series_title=auxMovie['series_title']
        released_year=int(auxMovie['released_year'])
        certificate=auxMovie['certificate'] if auxMovie['certificate'] else None
        runtime=int(auxMovie['runtime'])
        genre=auxMovie['genre']
        imdb_rating=float(auxMovie['imdb_rating'])
        overview=auxMovie['overview']
        meta_score=int(auxMovie['meta_score']) if auxMovie['meta_score'] else None
        director=auxMovie['director']
        star1=auxMovie['star1']
        star2=auxMovie['star2']
        star3=auxMovie['star3']
        star4=auxMovie['star4']
        no_of_votes=int(auxMovie['no_of_votes'])
        gross=float(auxMovie['gross']) if auxMovie['gross'] else None
        newMovie = Movie(globalId,poster_link,series_title,released_year,certificate,runtime,genre,imdb_rating,overview,meta_score,director,star1,star2,star3,star4,no_of_votes,gross)
        moviesRepo.append(newMovie)
        globalId += 1

        return 'Added id: ' + str(newMovie.id),200
    else:
        return "Wrong json format",400

if __name__ == "__main__":
    moviesRepo = read_movies_from_csv("imdb_top_1000.csv")
    # for movie in moviesRepo:
    #     print(movie)
    app.run()