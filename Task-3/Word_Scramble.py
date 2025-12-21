import random
unscrambled_words = ['python', 'javascript', 'java', 'automation', 'pytest', 'guvi', 'selenium']
scrambled_words = []
for word in unscrambled_words:
    scrambled = ''.join(random.sample(word, len(word)))
    scrambled_words.append(scrambled)
print("Welcome to the Word Scramble Game!")
for i in range(len(unscrambled_words)):
    print(f"Scrambled word: {scrambled_words[i]}")
    user_guess = input("User guess: ")
    if user_guess == unscrambled_words[i]:
        print("Correct!")
    else:
        print(f"Wrong! The correct word was: {unscrambled_words[i]}")