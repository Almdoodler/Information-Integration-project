from OMDB import *
from TMDB import *
from SimilarityMeasure import *
from Movie import *
import operator

if __name__ == "__main__":
    omdb = OMDB()
    tmdb = TMDB()
    movies = []
    r1 = omdb.search("john wick")
    r1 = sorted(r1, key=operator.attrgetter("imdbID"), reverse=False)
    r2 = tmdb.search("john wick")
    r1 = sorted(r1, key=operator.attrgetter("imdbID"), reverse=False)    
    print("r1 ", len(r1))
    print("r2 ", len(r2))
    print("all ", len(r1) + len(r2))

    for i in reversed(range(0, len(r1))):
        for j in reversed(range(0, len(r2))):
            #print(r1[i].getImbID(), " vs ", r2[j].getImbID())
            if r1[i].getImbID() == r2[j].getImbID():
                print("same")
                movies.append(r1[i])
                del(r1[i])
                del(r2[j])
                break
    print("r1 ", len(r1))
    print("r2 ", len(r2))
    print("m ", len(movies))
    print("all ", len(r1) + len(r2) + len(movies))

    sm = SimilarityMeasure()
    similarities = [[-1 for x in range(len(r1))] for y in range(len(r2))]
    for j in range(0, len(r2)):
        similarity = 0
        for i in range(0, len(r1)):
            x = sm.similar(str(r2[j].getRuntime()), str(r1[i].getRuntime()))
            x = x + sm.similar(str(r2[j].getYear()), str(r1[i].getYear()))
            x = x + sm.similar(str(r2[j].getTitle()), str(r1[i].getTitle()))
            a1 = sorted(r1[i].getActors())
            a2 = sorted(r2[j].getActors())
            seperator = ','
            x = x + sm.similar(seperator.join(a1), seperator.join(a2))

            p1 = sorted(r1[i].getProduction())
            p2 = sorted(r2[j].getProduction())
            seperator = ','
            x = x + sm.similar(seperator.join(p1), seperator.join(p2))

            if similarity < x/5:
                similarity = x/5
                if(similarity > 0.5):
                    similarities[j][i] = similarity
    

    complement = []
    for i in range(0, len(r1)):
        max_index = -1
        max_value = -1
        for j in range(0, len(r2)):
            if(similarities[j][i] > max_value):
                max_index = j
                max_value = similarities[j][i]
        complement.append(max_index)
        similarities[j] = [-1]*len(r1)

    """
    for i in range(0, len(r1)):
        if complement[i] > -1:
            print(r1[i].string())
            print(similarities[complement[i]][i])
            print(r2[complement[i]].string())
            print('----------------------------------------')
        else:
            print(r1[i].string())
            print(similarities[complement[i]][i])
            print('----------------------------------------')"""
    
    complement = sorted(complement, reverse= True)
    print("complement ", complement)
    for index in complement:
        if index > -1:
            #print("index ", index)
            #print("len ", len(r2))
            del(r2[index])
    
    r = r1 + r2
    """
    for movie in r:
        print(movie.string())
        print('----------------------------------------')"""

    print("all ", len(r))

   # er = SimilarityMeasure()
    #print(er.simJaro("batman", "begidfdasd batman"))
    #print(er.similar("batman", "begidfdasd batman"))
    #print(er.get_jaccard_sim("batman", "begidfdasd batman"))
    #print(er.get_similarity("batman", "begidfdasd batman"))