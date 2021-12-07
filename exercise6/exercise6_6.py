basket = ["apple", "banana", "cherry", "carrot", "potato", "tomato", "cabbage"]

word = input("Which word to ignore?\n")

if word not in basket:
    print("Word not found.")
else:
    for i in basket:
        if i == word:
            pass
        else:
            print(i)
