import spacy
nlp = spacy.load('en_core_web_md')

# Using readlines()
movie_file = open('movies.txt', 'r')
movie_list = movie_file.readlines()

movie_dict = {}


#my_information = {'name': 'Dionysia', 'age': 28, 'location': 'Athens'}
for movie in movie_list:
    movie_split = movie.split(":")
    movie_name = movie_split[0].strip()
    movie_description = movie_split[1].strip()
    movie_dict[movie_name] = movie_description
    #print(f"{movie_name},{movie_description}")

#print(movie_dict)

planet_hulk = f'''Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, 
the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace. 
Unfortunately, Hulk land on the planet Sakaar where he is sold into slavery and trained as a gladiator.'''

#print(planet_hulk)



def movie_recommendation(movie_list, description):
    comp_description = nlp(description)
    highest_similarity = 0
    movie_rec = ""

    for movie in movie_list:
        similarity = nlp(str(movie_list[movie])).similarity(comp_description)
        if similarity >= highest_similarity:
            highest_similarity = similarity
            movie_rec = f"{movie} : {movie_list[movie]}"
        
        print(f"{movie}: {similarity}")
    
    print(f"\n Recommended movie: {movie_rec}")

movie_recommendation(movie_dict, planet_hulk)
