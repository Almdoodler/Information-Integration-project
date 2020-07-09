
class Movie:

    def __init__(self, title, year, imdbID):
    		self.title, self.year, self.imdbID = title, year, imdbID

    def getTitle(self):
        return self.title
    
    def getYear(self):
        return self.year

    def getImbID(self):
        return self.imdbID
    