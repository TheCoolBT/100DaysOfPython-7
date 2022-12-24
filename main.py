import random

filepath = "words.txt"
with open(filepath) as f:
    wordlist = f.read().splitlines()
endgame = False
guessedletters = []
correctletters = []
lives = 6
easywords = []
mediumwords = []
hardwords = []
insanewords = []
for i in range(len(wordlist)):
    word = wordlist[i]
    if len(word) < 8:
        easywords.append(word)
    elif 13 > len(word) > 7:
        mediumwords.append(word)
    elif 18 > len(word) > 12:
        hardwords.append(word)
    elif len(word) > 17:
        insanewords.append(word)


def difficultyselect():
    while True:
        difficulty = input("Select Your Difficulty: \ne for easy \nm for medium \nh for hard \ni for insane\n").lower()
        if len(difficulty) != 1:
            print('Please enter a single letter.')
        elif difficulty not in 'emhi':
            print('Please enter e,m,h, or i.')
        else:
            if difficulty == 'e':
                guessword = random.choice(easywords)
            elif difficulty == 'm':
                guessword = random.choice(mediumwords)
            elif difficulty == 'h':
                guessword = random.choice(hardwords)
            elif difficulty == 'i':
                guessword = random.choice(insanewords)
            return guessword


# Displays the games data to the player, including guesses, lives, and the completion of the secret word
def displayboard():
    print("You have " + str(lives) + " lives left ")
    print("\nGuessed Letters:", end=" ")
    for letter in guessedletters:
        print(letter, end=" ")

    display = []
    for i in range(len(guessword)):
        display += "_"
    for position in range(len(guessword)):
        letter = guessword[position]
        if letter in correctletters:
            display[position] = letter

    print('\n')
    print(display)


# Controls user input and their guesses
def makeguess():
    while True:
        guess = input("\nGuess a letter: \n").lower()
        if len(guess) != 1:
            print('Please enter a single letter.')
        elif guess in guessedletters:
            print('You have already guessed that letter. Choose again.')
        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
            print('Please enter a LETTER.')
        else:
            guessedletters.append(guess)
            for position in range(len(guessword)):
                letter = guessword[position]
                if letter == guess:
                    # If letter is correct it goes into correct letters
                    correctletters.append(guess)
            return guess


# Checks to see if player has won the game based off word completion
def playerhaswon():
    foundallletters = True
    for i in range(len(guessword)):
        if guessword[i] not in correctletters:
            foundallletters = False
            break
    return foundallletters


# determines if player wants to play the game again
def playagain():
    pa = input("Would You like to play again? (y/n)").lower()
    return pa.startswith('y')


guessword = difficultyselect()
print(guessword)
while True:
    guess = makeguess()

    # Takes away a life if guess is incorrect
    if guess not in correctletters:
        lives = lives - 1
    displayboard()
    if playerhaswon():
        print("Congratulations! You guessed the correct word... " + guessword)
        endgame = True

    if lives == 0:
        print("You have lost, the correct word was... " + guessword)
        endgame = True

    if endgame:
        if playagain():
            guessedletters = []
            correctletters = []
            lives = 6
            guessword = difficultyselect()
            endgame = False
        else:
            break
