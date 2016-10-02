import urllib
import json


class Movie:
    """Class that stores movie info"""

    def __init__(self, title, trailer):
        self.title = title
        self.trailer = trailer
        self.info = self.getTMDBInfo(title)
        self.overview = self.info['overview']
        self.poster = self.info['poster']

    def getTMDBInfo(self, title):
        print('getting "' + title + '" data from TMDB')

        #get json data from TMDB
        #my keys inside
        #searchs for movie title
        connection = urllib.urlopen('http://api.themoviedb.org/3/search/movie?query='+title+'&api_key=30f431d2bcbda57feac3068e9aa1ac1e')

        #reads data
        output = connection.read()
        connection.close()

        #data to json
        data = json.loads(output)

        #return poster and overview info
        return {
            "poster": data["results"][0]["poster_path"],
            "overview": data["results"][0]["overview"]
        }
