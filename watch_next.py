import spacy

# This function takes a dictionary of movie titles with their descriptions
# and the description of the movie to make the "next movie to watch" recommendation 

def movie_recommendation(movie_dict, description):

    comp_description = nlp(description)
    # Keep track of the highest similarity between two descriptions
    highest_similarity = 0
    # Place holder for the recommended movie
    movie_rec = ""

    # Iterate through the movie dictionary and compare each movie description 
    # to the movie the recommendation is being made for
    for movie in movie_dict:

        similarity = nlp(str(movie_dict[movie])).similarity(comp_description)

        # If the similarity of the current description is higher than any previous comparison
        if similarity >= highest_similarity:
            # Update the highest_similarity value 
            # and the movie_rec (movie recommendation) variable to the current movie
            highest_similarity = similarity
            movie_rec = f"{movie}"
        
    return movie_rec

# Load spacy "en_core_web_md" module to compare movie descriptions
nlp = spacy.load('en_core_web_md')

# Read the movie.txt script and add each movie to a list - movie_list
movie_file = open('movies.txt', 'r')
movie_list = movie_file.readlines()

# Create an empty dictionary to store the movie name and description as a key-value pair
movie_dict = {}

# Movie description to test
description_to_compare = f'''Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, 
the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace. 
Unfortunately, Hulk land on the planet Sakaar where he is sold into slavery and trained as a gladiator.'''

# Iterate through movie list to create dictionary of movie names with their description
for movie in movie_list:
    movie_split = movie.split(":")
    movie_name = movie_split[0].strip()
    movie_description = movie_split[1].strip()
    movie_dict[movie_name] = movie_description

# Print the next recommended movie to watch
print(f"What to watch next: {movie_recommendation(movie_dict, description_to_compare)}")
