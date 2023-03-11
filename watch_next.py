import spacy

nlp = spacy.load("en_core_web_md")

list_movies = []

with open("movies.txt", "r", encoding="utf-8") as file:
    file_read = file.readlines()

# Iterate over the movies from the text file
for line in file_read:
    list_movies.append(nlp(line))

sample = """Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, the
         illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live 
         in peace. Unfortunately, Hulk land on the planet Sakaar where he is sold into slavery and trained as a 
         gladiator."""

comparison = nlp(sample)

# Create two variables to find the most similar movie
maxi = 0
best_match = ""

# For loop to retrieve max similarity and best match
for i in list_movies:
    if i.similarity(comparison) > maxi:
        print(i.similarity(comparison))
        maxi = i.similarity(comparison)
        best_match = i

print(best_match)
