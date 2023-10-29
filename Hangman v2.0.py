import random

categorized_words = [["tiger", "lion", "monkey", "bear", "elephant", "hippopotamus", "mouse", "cat", "whale", "deer"],
                     ["banana", "tomato", "orange", "pomegranate", "blueberry", "kiwi", "mango", "guava", "avacado"],
                     ["pop", "rap", "jazz", "oldies", "country", "rock", "reggae", "blues", "indie", "classical"]]

word_categories = ["Mammals", "Fruits", "Music"]

def print_hangman(tries):
    # Hangman Visuals
    if tries == 5:
        print(f'''
             ____
            |   |
                |
                |
                |
      --------------------
        ''')
    if tries == 4:
        print(f'''
                     _____
                     |   |
                    ()   |
                         |
                         |
             --------------------
                   ''')
    elif tries == 3:
        print(f'''
                     _____
                     |   |
                    ()   |
                   /|    |
                         |
             --------------------
                           ''')
    elif tries == 2:
        print(f'''
                     _____
                     |   |
                    ()   |
                   /||{chr(92)}  |
                         |
             --------------------
                           ''')
    elif tries == 1:
        print(f'''
                     _____
                     |   |
                    ()   |
                   /||{chr(92)}  |
                    /    |
             --------------------
                           ''')
    elif tries == 0:
        print(f'''
                     _____
                     |   |
                    ()   |
                   /||{chr(92)}  |
                    /{chr(92)}   |
             --------------------
                           ''')

def play():

    # Prints the word_categories list into string format
    def print_categories():
        for i in range(0, len(word_categories)):
            print(f"{i+1}. ", word_categories[i], end="  ", sep="")

    # Returns proper category input
    def get_category():

        print_categories()

        # Calculated num of categories in a str list
        str_nums = [str(i) for i in range(1, len(word_categories)+1)]  # Ex: If 2 categories - > ["1", "2"]

        while True:
            either = ""                                                # Turns list into (1,2,...,n) form
            for num in str_nums:                                       # Ex: [1, 2, 3] - > (1, 2, 3)
                either += num + ", " if num != str_nums[len(str_nums) - 1] else num

            usr_input = input(f"\nChoose a category to start ({either}): ")
            print("")  # prints new line

            # Checks if usr_input is valid category input
            if usr_input.isdigit() and usr_input in str_nums:
                return [usr_input, (word_categories[int(usr_input)-1]+"! Got it.")]
            else:
                print(f"Either {either}")

    # Returns proper guess input
    def get_guess():
        while True:
            user_guess = input("Guess a letter > ")
            if len(user_guess) == 1 and user_guess.isalpha():
                return user_guess
            else:
                if user_guess.isalpha() and user_guess != 1:
                    print("Last I checked a letter was one character!")
                else:
                    print("Letters only!")

    # ===GAME START MENU===
    print("         ***HANGMAN***\nGuess the word before the man hangs!", end="")

    while True:

        # ==Setting up the game_info variables==
        attempts = 5

        print_hangman(attempts)

        # Gets the chosen category input
        category_input = get_category()
        category = int(category_input[0]) - 1  # word_categories[category]

        info = category_input[1]          # displays user's category choice

        # Choose random secret word
        random_index = random.randint(0, len(categorized_words[category])-1)
        secret_word = categorized_words[category][random_index]

        # Creates word list
        wordlist = list(secret_word)
        guesslist = [" " for i in range(len(secret_word))]

        guessed_letters = []

        def print_game_info():
            guessed_str = ", ".join(guessed_letters)
            print(
                  f"Category: {word_categories[category]} • ",
                  f"Letters Guessed: {guessed_str}\n",
                  f"Attempts: {attempts} • ",
                  f"Info: {info}\n",
                  f"Your word has {len(secret_word)} letters.  {guesslist}", end="", sep="")
            print_hangman(attempts)

        # ===Start Game===
        while play:

            print_game_info()

            # Store users_guess
            users_guess = get_guess()

            # ==Update game_info variables==
            if users_guess in guessed_letters:
                responses = ["You already guessed that", "No mas guesso", "Should I start taking attempts away?"]
                info = responses[random.randint(0, len(responses)-1)]  # Updates info
                if guessed_letters.count(users_guess) >= 5:
                    attempts -= 1
                    info = "I warned you!"
            elif users_guess in wordlist:                              # Updates guesslist if letter guessed
                responses = ["Nice! That was it!", "Good guess!", "Too easy...", "You got a letter!"]
                info = responses[random.randint(0, len(responses)-1)]  # Updates info
                for i in range(len(wordlist)):
                    if users_guess == wordlist[i]:
                        guesslist[i] = users_guess
            else:
                attempts -= 1                                          # Updates attempts if letter guesses wrong
                responses = ["Wrong guess", "Incorrect guess!", "Actually think about it...", "Try a little harder"]
                info = responses[random.randint(0, len(responses)-1)]  # Updates info

            guessed_letters.append(users_guess)                        # Updates guessed_letters

            # ==End Game Checks==
            play_again = False

            if guesslist == wordlist:  # Checks if word was guessed
                print(f"You WON!\nYou guessed the word {secret_word} with {attempts} remaining.")
                play_again = True

            if attempts == 0:          # Checks if game was lost
                print(f"No more attempts\nYour word was {secret_word}\nGAME OVER!")
                play_again = True

            restart = False            # Asks user if they want to play again if game won or lost
            if play_again:
                while True:
                    again = input("Would you like to play again? (y, n) > ")
                    if again == "y":
                        restart = True
                        break
                    elif again == "n":
                        print("Bye!")
                        quit()
                    else:
                        print("Either yes or no")
            if restart: break





























while True:
    play()



