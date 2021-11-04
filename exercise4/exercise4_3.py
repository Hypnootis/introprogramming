
# The variable names are messy here but I originally understood the exercise differently, so I left them as is :)

text = "The quick brown fox jumps over the lazy dog. That sentence contains every letter in the English alphabet. Isn't that neat!\n"

print(text)

print(text.replace("fox", "duck"))

removed_word = str(input("Which word should be removed?\n"))

new_text = text.replace(removed_word, " ")

print(new_text)

print(str(len(new_text)) + " characters")

print(new_text.replace(".", "\n"))

shorter_text = new_text[0:20]

shorter_text += "..."

print(shorter_text)
