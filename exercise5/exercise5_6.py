movie = {"name": "Pulp Fiction",
         "year": 1994,
         "director": "Quentin Tarantino",
         "genre": "Crime, Drama",
         "duration": 154}
print("WITH a loop:\n")

for i in movie:
    print(movie[i])

print("\nWITHOUT a loop:\n")

print(movie["name"])
print(movie["year"])
print(movie["director"])
print(movie["genre"])
print(movie["duration"])
