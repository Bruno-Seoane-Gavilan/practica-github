letra=input()
if letra.islower():
    print("lowercase")
if letra.isupper():
    print("uppercase")
if letra in "AEIOUaeiou":
    print("vowel")
if letra not in "AEIOUaeiou":
    print("consonant")