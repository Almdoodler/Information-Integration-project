from OMDB import *
from TMDB import *
from SimilarityMeasure import *
from Movie import *
import operator

if __name__ == "__main__":
    omdb = OMDB()
    tmdb = TMDB()
    movies = []
    r1 = omdb.search("naruto")
    r1 = sorted(r1, key=operator.attrgetter("imdbID"), reverse=False)
    r2 = tmdb.search("naruto")
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
    similarities = [-1] * len(r1)
    for i in range(0, len(r1)):
        similarity = 0
        for j in range(0, len(r2)):
            x = sm.similar(str(r1[i].getRuntime()), str(r2[j].getRuntime()))
            x = x + sm.similar(str(r1[i].getYear()), str(r2[j].getYear()))
            x = x + sm.similar(str(r1[i].getTitle()), str(r2[j].getTitle()))
            actors1 = sorted(r1[i].getActors())
            actors2 = sorted(r2[j].getActors())
            seperator = ','
            x = x + sm.similar(seperator.join(actors1), seperator.join(actors1))

            p1 = sorted(r1[i].getProduction())
            p2 = sorted(r2[j].getProduction())
            seperator = ','
            x = x + sm.similar(seperator.join(p1), seperator.join(p2))
            print("x ", x/5)

            if similarity<x/5:
                print("hjh", similarities)
                similarity = x/5
                similarities[i]=j
    
    for i in range(0, len(r1)):
        print(r1[i].string())
        print(similarities[i])
        print(r2[similarities[i]].string())
        print('----------------------------------------')


   # er = SimilarityMeasure()
    #print(er.simJaro("batman", "begidfdasd batman"))
    #print(er.similar("batman", "begidfdasd batman"))
    #print(er.get_jaccard_sim("batman", "begidfdasd batman"))
    #print(er.get_similarity("batman", "begidfdasd batman"))