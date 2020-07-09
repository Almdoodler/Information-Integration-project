import requests
from Movie import Movie



class OMDB:

    search_url = 'https://www.omdbapi.com/?apikey=3c011de4&s='
    movie_url = 'https://www.omdbapi.com/?apikey=3c011de4&t='

    """ Gibt Ergebnisse für Film-Suchanfrage 'movieName' zurück. 
    return: movies (list<Movie>) """
    def search(self, movieName):
        r = requests.get(self.search_url + movieName)
        dic = r.json()
        
        if int(dic['totalResults'])>0:
            elements = self.cleanResult(dic['Search'], 'movie')
            movies = self.createMovie(elements)

            for movie in movies:
                r = requests.get(self.movie_url + movie.getTitle())
                dic = r.json()
                if dic['Response'] == 'True':
                    actors = [actor.strip(' ') for actor in dic['Actors'].split(',')]
                    movie.setActors(actors)
                    movie.setProduction(dic['Production'])
                    movie.setRuntime(dic['Runtime'])

        else:
            movies = []


        for movie in movies:
            print('Title' + movie.getTitle())
            print('Actors', movie.getActors())
        return movies
    
        
        
    
    """ Entfernt alle anderen Elemente außer Elemente mit type:filter
    return elements (dic) """
    def cleanResult(self, dic, filter):
        delete = []
        for i in range(0, len(dic)):

            if dic[i]['Type'] != filter:
                delete.append(i)
        
        for index in delete:
            del(dic[index])

        return dic
    
    
    def createMovie(self, elements):
        movies = []
        for element in elements:
            movies.append(Movie(element['Title'], element['Year'], element['imdbID']))
        return movies
            
        
         
if __name__ == "__main__":
    s = OMDB()
    s.search('Batman')