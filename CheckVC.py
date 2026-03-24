char = input("Enter the character what you want to check: ").lower()

if char in ("a", "e", "i", "o", "u"):
    print("Vowel letter")
else:
    print("Consonant letter")