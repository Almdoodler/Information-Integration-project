import requests
from Movie import Movie



class OMDB:

    url = 'https://www.omdbapi.com/?apikey=3c011de4&s='

    """ Gibt Ergebnisse für Film-Suchanfrage 'movieName' zurück. 
    return: movies (list<Movie>) """
    def getMovie(self, movieName):
        r = requests.get(self.url + movieName)
        dic = r.json()

        print(dic)
        
        if int(dic['totalResults'])>0:
            elements = self.cleanResult(dic['Search'], 'movie')
            movies = self.createMovie(elements)
        else:
            movies = []


        for movie in movies:
            print(movie.getTitle())
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
            
        
 """           
if __name__ == "__main__":
    s = OMDB()
    s.getMovie('Batman v Superman')"""