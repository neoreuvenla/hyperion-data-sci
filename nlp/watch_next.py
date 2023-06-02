# task 21b - semantic similarity (nlp)
# purpose - suggest a similar movie by comparing descriptions

# note that with these inputs, the highest similarity is 0.88 and next two are 
# both 0.87. if this were to be expanded, it would be wise to print a list of 
# titles within a range of scores
#
# additionally, the code could be refactored in the future. for example the file
# loader could be made into a function, allowing for flexibility and reuse.

# import spacy for similarity and os to help locate files
import os
import spacy

# load the medium english language model globally
nlp = spacy.load('en_core_web_md') 

# assumes movies.txt input file is in the same folder as the running code
# find the directory of this code and use it to build the input file path
code_path = os.path.dirname(os.path.realpath(__file__))
file_path = os.path.join(code_path, 'movies.txt')

# dictionary to hold imported movie titles and calculated tokens
movie_dict = {}

# error handling for file loading
try:
    # load the input file as read only and produce a dictionary
    with open(file_path, 'r') as file:

        # loop to read each line as a new movie
        for line in file:

            # split the movie title and description using the colon
            movie, description = line.split(':')
            
            # strip any resulting whitespace from the removal of the colon
            movie = movie.strip()
            description = description.strip()

            # create dictionary from movie title and description tokens
            movie_dict[movie] = nlp(description)

# file not found error message
except FileNotFoundError:
    print("Error: File not found.")

# io error message
except IOError:
    print("Error: Unable to read the file.")

# other error message
except Exception as e:
    print("Error:", str(e))

# recommends a movie stored in a dictionary from a user description
def recommend_movie(user_description):
    
    # tokenises the provided description
    user_description = nlp(user_description)
    
    # hold the highest similarity score and title seen
    max_similarity = -1 
    most_similar_movie = None

    # loop over each movie description pair in the dictionary
    for movie, movie_description in movie_dict.items():

        # calculate similarity of the user and dictionary item description
        similarity = user_description.similarity(movie_description)
        
        # update the max similarity seen and most similar movie
        if similarity > max_similarity:
            max_similarity = similarity
            most_similar_movie = movie

    # returns the movie with the highest similarity score
    return most_similar_movie

# film description provided by the user
user_description = """Will he save their world or destroy it? When the Hulk becomes 
                    too dangerous for the Earth, the Illuminati trick Hulk into a 
                    shuttle and launch him into space to a planet where the Hulk can 
                    live in peace. Unfortunately, Hulk lands on the planet Sakaar 
                    where he is sold into slavery and trained as a gladiator."""

# call the function to recommened a movie
print("\n" + "-" * 27)
print("Recommended movie: ", recommend_movie(user_description))
print("-" * 27, "\n")