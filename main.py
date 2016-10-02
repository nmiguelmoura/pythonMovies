import movie
import indexPage

#build dictionary with all movies
movies = {
    0: {
        'title': 'Cinema Paraiso',
        'trailer': 'https://www.youtube.com/watch?v=maV1ZYdAExw'
    },
    1: {
        'title': 'The legend of 1900',
        'trailer': 'https://www.youtube.com/watch?v=2uf-LDlZMFE'
    },
    2: {
        'title': 'Hero (Ying xiong)',
        'trailer': 'https://www.youtube.com/watch?v=srFhXDZhUZI'
    },
    3: {
        'title': 'Batman',
        'trailer': 'https://www.youtube.com/watch?v=DRM1G58SI2E'
    },
    4: {
        'title': 'House of flying daggers',
        'trailer': 'https://www.youtube.com/watch?v=zLkedDMb8vI'
    },
    5: {
        'title': 'O tigre e o dragao',
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
    mov = movie.Movie(movieInfo["title"], movieInfo["trailer"])
    moviesList.append(mov)

#call function open_movies_page from indexPage
indexPage.open_movies_page(moviesList)

