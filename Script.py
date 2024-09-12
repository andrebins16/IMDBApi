import requests

baseUrl = "https://imdbapi-gi8p.onrender.com"

def getAllMovies():
    response = requests.get(f"{baseUrl}/movies")
    if response.status_code == 200:
        return response.json()
    else:
        return response.json()

def getMovieById(movie_id):
    response = requests.get(f"{baseUrl}/movie/{movie_id}")
    if response.status_code == 200:
        return response.json()
    else:
        return response.json()

def addMovie(movie_data):
    response = requests.post(f"{baseUrl}/movie", json=movie_data)
    if response.status_code == 201:
        return response.json()
    else:
        return response.json()

def updateMovie(movie_id, update_data):
    response = requests.patch(f"{baseUrl}/movie/{movie_id}", json=update_data)
    if response.status_code == 200:
        return response.text
    else:
        return response.json()

def deleteMovie(movie_id):
    response = requests.delete(f"{baseUrl}/movie/{movie_id}")
    if response.status_code == 200:
        return response.text
    else:
        return response.json()

if __name__ == "__main__":
    print("\n")
    print(f"-Adicionar novo filme - Requisição: Método POST - {baseUrl}/movie ")
    print("""-Corpo da requisição: 
{
    "Series_Title": "O Auto da Compadecida",
    "Genre": "Comedy, Drama",
    "IMDB_Rating": 8.6,
    "Overview": "No Brasil, dois nordestinos pobres e espertos vivem de enganar pessoas para sobreviver. Quando conhecem uma moça rica, eles têm esperança de se darem bem, mas seus planos são interrompidos pela chegada de um bandido forasteiro.",
    "Runtime": "144 min",
    "Director": "Guel Arraes",
    "Star1": "Matheus Nachtergaele",
    "Star2": "Selton Mello",
    "Released_Year": 2000
}
""")
    print("-Pressione Enter para visualizar a resposta da requisição")
    input()
    new_movie = {
        "Series_Title": "O Auto da Compadecida",
        "Genre": "Comedy, Drama",
        "IMDB_Rating": 8.6,
        "Overview": "No Brasil, dois nordestinos pobres e espertos vivem de enganar pessoas para sobreviver. Quando conhecem uma moça rica, eles têm esperança de se darem bem, mas seus planos são interrompidos pela chegada de um bandido forasteiro.",
        "Runtime": "144 min",
        "Director": "Guel Arraes",
        "Star1": "Matheus Nachtergaele",
        "Star2": "Selton Mello",
        "Released_Year": 2000
    }
    print(addMovie(new_movie))


    print("\nPressione Enter para visualizar a próxima requisição")
    input()
    print("\n")
    print(f"-Buscar todos filmes - Requisição: Método GET - {baseUrl}/movies ")
    print("-Pressione Enter para visualizar a resposta da requisição")
    input()
    print(getAllMovies())


    print("\nPressione Enter para visualizar a próxima requisição")
    input()
    print("\n")
    print(f"-Buscar filme pelo id - Requisição: Método GET - {baseUrl}/movie/0 ")
    print("-Pressione Enter para visualizar a resposta da requisição")
    input()
    print(getMovieById(0))


    print("\nPressione Enter para visualizar a próxima requisição")
    input()
    print("\n")
    print(f"-Atualizar filme - Requisição: Método PATCH - {baseUrl}/movie/0 ")
    print("""-Corpo da requisição: 
{
    "IMDB_Rating": "9.0",
    "Series_Title": "Titulo alterado!"
}
""")
    print("-Pressione Enter para visualizar a resposta da requisição")
    input()
    update_data = {
        "IMDB_Rating": "9.0",
        "Series_Title": "FILME ATUALIZADO"
    }
    print(updateMovie(0, update_data))


    print("\nPressione Enter para visualizar a próxima requisição")
    input()
    print("\n")
    print(f"-Deletar filme - Requisição: Método DELETE - {baseUrl}/movie/0 ")
    print("-Pressione Enter para visualizar a resposta da requisição")
    input()
    print(deleteMovie(0))
