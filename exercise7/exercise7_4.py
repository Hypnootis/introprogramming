movie_list = [{"name": "Casablanca", "year" : 1942},
           {"name": "Forrest Gump", "year" : 1942},
           {"name": "Avatar", "year": 2009},
           {"name": "Shrek", "year": 2001},
           {"name": "Titanic", "year": 1997},
           {"name": "Rölli ja metsän henki", "year": 2001},
           {"name": "The Grinch", "year": 2000}

]

before_2000 = []
after_2000 = []
separator = ", "

for i in movie_list:
    if i["year"] < 2000:
        before_2000.append(i["name"])
    else:
        after_2000.append(i["name"])

print("These movies have been released in year 2000 or later:")
print(separator.join(after_2000))
print("\n")
print("These movies have been released before the year 2000")
print(separator.join(before_2000))

