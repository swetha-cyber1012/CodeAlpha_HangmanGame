import random

# ============================
# CATEGORY WORD LIST
# ============================
WORD_CATEGORIES = {
    "Animals": ["tiger", "lion", "elephant", "zebra", "giraffe"],
    "Programming": ["python", "variable", "function", "loop", "compiler"],
    "Fruits": ["banana", "mango", "apple", "orange", "papaya"]
}

# ============================
# DIFFICULTY SETTINGS
# ============================
DIFFICULTY_LIVES = {
    "Easy": 8,
    "Medium": 6,
    "Hard": 4
}

# ============================
# SELECT CATEGORY
# ============================
def choose_category():
    print("\nChoose a Category:")
    for i, category in enumerate(WORD_CATEGORIES, start=1):
        print(f"{i}. {category}")

    while True:
        choice = input("Enter option (1-3): ")
        if choice in ["1", "2", "3"]:
            return list(WORD_CATEGORIES.keys())[int(choice) - 1]
        print("⚠ Invalid choice, try again.")

# ============================
# SELECT DIFFICULTY
# ============================
def choose_difficulty():
    print("\nChoose Difficulty:")
    print("1. Easy (8 lives)")
    print("2. Medium (6 lives)")
    print("3. Hard (4 lives)")

    while True:
        choice = input("Enter option (1-3): ")
        if choice == "1":
            return "Easy"
        elif choice == "2":
            return "Medium"
        elif choice == "3":
            return "Hard"
        print("⚠ Invalid choice, try again.")

# ============================
# MAIN GAME LOGIC
# ============================
def hangman_game():
    category = choose_category()
    difficulty = choose_difficulty()

    secret_word = random.choice(WORD_CATEGORIES[category])
    display = ["_"] * len(secret_word)
    guessed = set()
    lives = DIFFICULTY_LIVES[difficulty]
    score = 0

    print("\n===== HANGMAN GAME =====")
    print(f"Category: {category}")
    print(f"Hint: First letter is '{secret_word[0]}'")
    print(f"Lives: {lives}")

    while lives > 0 and "_" in display:
        print("\nWord:", " ".join(display))
        print("Guessed letters:", ", ".join(sorted(guessed)))
        
        guess = input("Guess a letter: ").lower()

        if not guess.isalpha() or len(guess) != 1:
            print("⚠ Enter a single letter!")
            continue

        if guess in guessed:
            print("⚠ Already guessed!")
            continue

        guessed.add(guess)

        if guess in secret_word:
            print("✅ Correct!")
            score += 10
            for i, letter in enumerate(secret_word):
                if letter == guess:
                    display[i] = guess
        else:
            lives -= 1
            print(f"❌ Wrong! {lives} lives left.")
            score -= 2

    # Game result
    print("\n==============================")
    if "_" not in display:
        print("🎉 YOU WON!")
        score += 20
    else:
        print("💀 GAME OVER!")

    print(f"The word was: {secret_word}")
    print(f"Your Score: {score}")
    print("==============================\n")

# ============================
# START GAME
# ============================
if __name__ == "__main__":
    hangman_game()
