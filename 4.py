def check_vowel(letters:str):
    vowels = ["a","e","i","o","u"]
    for i in range(len(vowels)):
        if vowels[i].upper() == letters.upper():
            return True
    return False
print(check_vowel("U"))
