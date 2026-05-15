import random

# 1. SETUP: Dictionary with words and their related hints
word_data = {
    "python": "A popular programming language named after a snake.",
    "coding": "The process of writing instructions for a computer.",
    "github": "A platform used for version control and hosting code.",
    "alpha": "The first letter of the Greek alphabet.",
    "logic": "Reasoning conducted according to strict principles."
}

# Pick a random word from the keys of our dictionary
target_word = random.choice(list(word_data.keys()))
display_word = ["_"] * len(target_word)

lives = 6
guessed_letters = []
hint_used = False

print("--- Welcome to CodeAlpha Hangman! ---")

while lives > 0 and "_" in display_word:
    print(f"\nWord: {' '.join(display_word)}")
    print(f"Lives: {lives} | Guessed: {', '.join(guessed_letters)}")
    
    # Offer the hint if they haven't used it and have enough lives
    if not hint_used and lives > 2:
        print("Type 'hint' to see a description (costs 2 lives).")
    
    guess = input("Guess a letter: ").lower()

    # 2. DESCRIPTIVE HINT LOGIC
    if guess == "hint" and not hint_used:
        if lives > 2:
            hint_used = True
            lives -= 2
            print(f"\n💡 HINT: {word_data[target_word]}") # Displays the sentence
            continue
        else:
            print("\nNot enough lives for a hint!")
            continue

    # 3. VALIDATION
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single letter.")
        continue
    
    if guess in guessed_letters:
        print("You already guessed that!")
        continue

    guessed_letters.append(guess)

    # 4. CHECK GUESS
    if guess in target_word:
        for index in range(len(target_word)):
            if target_word[index] == guess:
                display_word[index] = guess
        print("Correct!")
    else:
        lives -= 1
        print(f"Wrong! '{guess}' is not in the word.")

# 5. END GAME
if "_" not in display_word:
    print(f"\nVictory! You found the word: {target_word}")
else:
    print(f"\nGame Over. The word was: {target_word}")