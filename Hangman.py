import random

# categories
# show each letter when guessed
# show letters already guessed

# Word selector
random_words = ["voxel", "dead", "tiger", "space", ]

# Categories - Animals, Food, Brand Names, States, Sports
category_ask = True
categorized_words = [["tiger", "lion", "frog", "monkey", "bear", "elephant", "hippopotamus", "ant", "bee", "lizard"],
                     ["banana", "apple", "orange", "chicken", "bread", "beans", "eggs", "cereal", "nuts", "chips"]]


word_categories = ["Animals", "Food", "Sports"]
wc_counter = 0
wc_output = ""
wc_len = len(word_categories)

# Word Categories to String
for word in word_categories:
    wc_counter += 1
    wc_output += str(word)
    if wc_counter < wc_len:
        wc_output += ", "

# Category to Number
word_categories_numconvert = {
    "animals": 0,
    "animal": 0,
    "foods": 1,
    "food": 1
}

application_start = True
game_start = False
game_won = False
game_failed = False
can_game_start = False
start_w = "start"
start_fk = 0
word_list = []
attempts = 5
trys = 0
game_word = ""
game_letter_counter = -1
game_letter_index = []
gl_list = []
gl_len = len(gl_list)
gl_counter = 0
guessed_letters = ""


hangman = f'''
             ____
            |   |
                |
                |
                |
     --------------------
    '''


def game_info(letter_count, tries, wordlist, category, guessed):
    game_info_output = "\033[1m" + "Attempts:" + "\033[0m" + f" {tries}\n"
    game_info_output += "\033[1m" + "Category:" + "\033[0m" + f" {category}\n" + "\033[1m"+"Letters Guessed: "+"\033[0m"
    if guessed == "":
        game_info_output += "None"
    else:
        game_info_output += guessed
    game_info_output += "\033[1m" + f"\nYour word has" + f" {len(letter_count)}" + f" letters.  {wordlist}" + "\033[0m"
    game_info_output += hangman
    return game_info_output


start_list = ["start", "commence", "begin", "forward", "undertake", "initiate", "kick off", "launch", "embark", "go"]

print("         ***HANGMAN***\nGuess word before the man hangs!" + hangman + f"\nBefore we begin,"
       f" what category would you like:", end=" ")

while application_start:
    while category_ask:
        print("\033[1m" + f"\n{wc_output}" + "\033[0m")
        user_category = input("Type a category > ").capitalize()

        # To Find Category Index
        if user_category in word_categories:
            c_index = word_categories_numconvert.get(user_category.lower())
            print(f"\n{user_category}! Got it.")
            category_ask = False
        else:
            print(f"{user_category} isn't a listed category, try again")

    while not game_start:
        # iykyk
        if start_fk > 2:
            start_w = start_w.upper()

        # Category Input and Random Word Selector
        starting_input = str(input(f"Type {start_w} to begin > "))
        random_word_choice = random.choice(categorized_words[c_index])

        # Start Checker
        for starters in start_list:
            if starting_input.lower() == starters:
                can_game_start = True
                break

        # Game Starts, Now What?
        if can_game_start:
            start_fk = 0
            start_w = "start"
            guessed_letters = ""
            attempts = 5
            game_word = random_word_choice
            e = "_"

            # Words Guessed Visual
            for ticks in range(1, len(game_word) + 1):
                word_list.append(e)

            # Game Info
            if start_fk >= 2:
                print(f"\nFinally! Let's begin!)")
                print(game_info(game_word, attempts, word_list, user_category, None))
            else:
                print(f"\nLet's begin!")
                print(game_info(game_word, attempts, word_list, user_category, guessed_letters))
            game_start = True
            break
        # If User Didn't Start, How Do We Clap Back?
        else:
            start_fk += 1
            if start_fk == 1:
                print(f"{starting_input.capitalize()}? Pretty sure that's not start or begin or anything that moves us"
                      " forward. Here, let's try again.")
            if start_fk == 2:
                print("Ok ok, I can understand that maybe your first try was a mistake. But now you're just messing"
                      " with me. From the beginning!")
            if start_fk == 3:
                print("Alright bud this is your last chance, either play the game or leave I don't have time for this.")
            if start_fk == 4:
                print("\nGAME OVER")
                break

    while game_start:
        users_guess = input("Guess a letter > ")

        # Hangman Visuals
        if attempts == 4:
            hangman = f'''
                  _____
                  |   |
                 ()   |
                      |
                      |
          --------------------
                '''
        elif attempts == 3:
            hangman = f'''
                  _____
                  |   |
                 ()   |
                /|    |
                      |
          --------------------
                        '''
        elif attempts == 2:
            hangman = f'''
                  _____
                  |   |
                 ()   |
                /||{chr(92)}  |
                      |
          --------------------
                        '''
        elif attempts == 1:
            hangman = f'''
                  _____
                  |   |
                 ()   |
                /||{chr(92)}  |
                 /    |
          --------------------
                        '''
        elif attempts == 0:
            hangman = f'''
                  _____
                  |   |
                 ()   |
                /||{chr(92)}  |
                 /{chr(92)}   |
          --------------------
                        '''

        if len(users_guess) == 1:
            if users_guess.isalpha():

                if users_guess in game_word:
                    trys += 1

                    # Reset
                    game_letter_counter = -1
                    game_letter_index.clear()

                    # Replacing all "_" for user_guess in word_list
                    for letter in game_word:
                        game_letter_counter += 1
                        if users_guess == letter:
                            game_letter_index.append(game_letter_counter)
                    for index in game_letter_index:
                        word_list[index] = users_guess

                    # Letters Guessed
                    gl_list.append(users_guess)
                    guessed_letters = ""
                    gl_counter = 0
                    for guess in gl_list:
                        gl_counter += 1
                        guessed_letters += str(guess)
                        if gl_counter >= gl_len:
                            guessed_letters += ", "
                    guessed_letters = guessed_letters[:-2]

                    # Game Word
                    print("\033[1m" + f"\nNice! That was it!" + "\033[0m")
                    print(game_info(game_word, attempts, word_list, user_category, guessed_letters))

                else:
                    attempts -= 1
                    trys += 1

                    # Hangman Visuals 2.0
                    if attempts == 4:
                        hangman = f'''
                              _____
                              |   |
                             ()   |
                                  |
                                  |
                      --------------------
                            '''
                    elif attempts == 3:
                        hangman = f'''
                              _____
                              |   |
                             ()   |
                            /|    |
                                  |
                      --------------------
                                    '''
                    elif attempts == 2:
                        hangman = f'''
                              _____
                              |   |
                             ()   |
                            /||{chr(92)}  |
                                  |
                      --------------------
                                    '''
                    elif attempts == 1:
                        hangman = f'''
                              _____
                              |   |
                             ()   |
                            /||{chr(92)}  |
                             /    |
                      --------------------
                                    '''
                    elif attempts == 0:
                        hangman = f'''
                              _____
                              |   |
                             ()   |
                            /||{chr(92)}  |
                             /{chr(92)}   |
                      --------------------
                                    '''

                    # Letters Guessed
                    if users_guess not in gl_list:
                        gl_list.append(users_guess)
                    guessed_letters = ""
                    gl_counter = 0
                    for guess in gl_list:
                        gl_counter += 1
                        guessed_letters += str(guess)
                        if gl_counter >= gl_len:
                            guessed_letters += ", "
                    guessed_letters = guessed_letters[:-2]

                    # Game Status
                    print("\033[1m" + f"\n{users_guess.capitalize()} isn't in the word." + "\033[0m")
                    print(game_info(game_word, attempts, word_list, user_category, guessed_letters))

            else:
                print("Letters only.")
        else:
            print("One character only.")

        if "_" not in word_list:
            game_start = False
            game_won = True
            break
        elif attempts == 0:
            game_start = False
            game_failed = True
            break

    while game_won or game_failed:
        if game_won:
            print("\033[1m" + "You won!" + "\033[0m")
            print("You guessed the word" + "\033[1m" f" {game_word}" + "\033[0m" + " in" + "\033[1m" f" {trys} " + "\033[0m"+
                  "attempts.")
        if game_failed:
            print("\033[1m" + "No more attempts." + "\033[0m")
            print("Your word was" + "\033[1m" f" {game_word}" + "\033[0m" + "\nGAME OVER!")
        try:
            if game_won:
                play_again_ask = str(input("\nWould you like to play again? > ")).lower()
            if game_failed:
                play_again_ask = str(input("\nMaybe next time, play again? > ")).lower()

            if play_again_ask == "yes" or play_again_ask == "yeah":
                play_again = True
            elif play_again_ask == "no" or play_again_ask == "nah":
                play_again = False

            if play_again:
                game_won = False
                game_failed = False
                category_ask = True
                trys = 0
                word_list.clear()
                hangman = f'''
                             ____
                            |   |
                                |
                                |
                                |
                     --------------------
                    '''
                break
            else:
                application_start = False
                break
        except NameError:
            print("Either yes or no, lets recap.\n")
