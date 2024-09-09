from flask import Flask, request, jsonify
import csv
class Movie:
    def __init__(self, poster_link, series_title, released_year, certificate, runtime, genre, imdb_rating, overview, meta_score, director, star1, star2, star3, star4, no_of_votes, gross):
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

def read_movies_from_csv(file_path):
    auxMovies = []
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
            newMovie = Movie(poster_link,series_title,released_year,certificate,runtime,genre,imdb_rating,overview,meta_score,director,star1,star2,star3,star4,no_of_votes,gross)
            auxMovies.append(newMovie)
        return auxMovies



if __name__ == "__main__":
    moviesRepo = read_movies_from_csv("imdb_top_1000.csv")
    for movie in moviesRepo:
        print(movie)
    # app.run()