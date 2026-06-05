import random
import winsound

def play_hangman():

    easy_words = [
        "book", "tree", "fish", "game", "milk",
        "road", "star", "moon", "apple", "house"
    ]

    medium_words = [
        "python", "coding", "laptop", "mobile", "coffee",
        "django", "flask", "rocket", "school", "bridge"
    ]

    hard_words = [
        "algorithm", "framework", "compiler", "encryption",
        "processor", "blockchain", "artificial",
        "intelligence", "cybersecurity", "programming"
    ]

    print("\n" + "=" * 40)
    print("         HANGMAN GAME")
    print("=" * 40)

    print("\nChoose Difficulty:")
    print("1. Easy   (10 words, 8 chances)")
    print("2. Medium (10 words, 6 chances)")
    print("3. Hard   (10 words, 5 chances)")

    choice = input("\nEnter your choice (1-3): ")

    if choice == "1":
        word = random.choice(easy_words)
        attempts = 8
        difficulty = "Easy"

    elif choice == "2":
        word = random.choice(medium_words)
        attempts = 6
        difficulty = "Medium"

    elif choice == "3":
        word = random.choice(hard_words)
        attempts = 5
        difficulty = "Hard"

    else:
        print("Invalid choice!")
        return

    guessed_letters = []

    print(f"\nDifficulty Selected: {difficulty}")
    print(f"You have {attempts} chances.\n")

    while attempts > 0:

        display_word = ""

        for letter in word:
            if letter in guessed_letters:
                display_word += letter + " "
            else:
                display_word += "_ "

        print("\nWord:", display_word)
        print("Guessed Letters:", " ".join(guessed_letters))

        if "_" not in display_word:
            winsound.Beep(1500, 500)
            print("\nCongratulations!")
            print("You guessed the word:", word)
            return

        guess = input("\nEnter a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter only one alphabet.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess in word:
            winsound.Beep(1200, 200)
            print("Correct Guess!")

        else:
            attempts -= 1
            winsound.Beep(500, 400)
            print("Wrong Guess!")
            print("Remaining Chances:", attempts)

    print("\nGAME OVER!")
    print("The word was:", word)


while True:

    play_hangman()

    play_again = input("\nDo you want to play again? (y/n): ").lower()

    if play_again != "y":
        print("\nThanks for playing Hangman!")
        break   