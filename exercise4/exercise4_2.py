text = str(input("Give some text:\n"))


text_reversed = text[::-1]

print(text_reversed)

if text != "":
    if text_reversed == text:
        print("Palindrome: YES")
    else:
        print("Palindrome: NO")

else:
    print("Your text is empty.")
