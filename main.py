import movie
import indexPage

#build dictionary with all movies
movies = {
    0: {
        'title': 'Cinema Paraiso',
        'poster': 'https://upload.wikimedia.org/wikipedia/fi/thumb/2/2f/Cinema_Paradiso_dvd-videotallennekansikuva.jpg/848px-Cinema_Paradiso_dvd-videotallennekansikuva.jpg',
        'trailer': 'https://www.youtube.com/watch?v=maV1ZYdAExw'
    },
    1: {
        'title': 'A lenda de 1900',
        'poster': 'https://images-na.ssl-images-amazon.com/images/M/MV5BMTA3MTcxNjE0NzNeQTJeQWpwZ15BbWU4MDc3NjUxNDAx._V1_UX182_CR0,0,182,268_AL_.jpg',
        'trailer': 'https://www.youtube.com/watch?v=2uf-LDlZMFE'
    },
    2: {
        'title': 'Hero',
        'poster': 'https://images-na.ssl-images-amazon.com/images/M/MV5BMTk5NjQyMzIwM15BMl5BanBnXkFtZTcwODQyNjYyMQ@@._V1_UX182_CR0,0,182,268_AL_.jpg',
        'trailer': 'https://www.youtube.com/watch?v=srFhXDZhUZI'
    },
    3: {
        'title': 'Batman',
        'poster': 'https://images-na.ssl-images-amazon.com/images/M/MV5BMTMxNTMwODM0NF5BMl5BanBnXkFtZTcwODAyMTk2Mw@@._V1_UX182_CR0,0,182,268_AL_.jpg',
        'trailer': 'https://www.youtube.com/watch?v=EXeTwQWrcwY'
    },
    4: {
        'title': 'House of flying daggers',
        'poster': 'https://images-na.ssl-images-amazon.com/images/M/MV5BMzg4MDE0NzIwNl5BMl5BanBnXkFtZTcwMDI2NDcyMQ@@._V1_UX182_CR0,0,182,268_AL_.jpg',
        'trailer': 'https://www.youtube.com/watch?v=zLkedDMb8vI'
    },
    5: {
        'title': 'O tigre e o dragao',
        'poster': 'https://images-na.ssl-images-amazon.com/images/M/MV5BMDEyNjIyODktM2M0NC00MTgwLTk2ZTItMTZlZGEyNzg4MDkyXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_SY1000_CR0,0,676,1000_AL_.jpg',
        'trailer': 'https://www.youtube.com/watch?v=QzPf15U8bLI'
    }
}

#create an empty list to put movies created
moviesList = []

#get length of movies dictionary
moviesLength = len(movies)
movieInfo = None
mov = None

#loop through movies dictionary and instanciate Movie class for all
#append the new instance to moviesList
for i in range(0, moviesLength):
    movieInfo = movies[i]
    mov = movie.Movie(movieInfo["title"], movieInfo["poster"], movieInfo["trailer"])
    moviesList.append(mov)

#call function open_movies_page from indexPage
indexPage.open_movies_page(moviesList)

