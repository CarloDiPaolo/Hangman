import random
HANGMAN_PICS = ['''
  +---+
      |
      |
      |
     ===''', '''
  +---+
  O   |
      |
      |
     ===''', '''
  +---+
  O   |
  |   |
      |
     ===''', '''
  +---+
  O   |
 /|   |
      |
     ===''', '''
  +---+
  O   |
 /|\  |
      |
     ===''', '''
  +---+
  O   |
 /|\  |
 /    |
     ===''', '''
  +---+
  O   |
 /|\  |
 / \  |
     ===''', '''
  +---+
 [O   |
 /|\  |
 / \  |
     ===''', '''
  +---+
 [O]  |
 /|\  |
 / \  |
     ===''']
words = {'Colors' : 'red orange yellow green blue indigo violet white black brown'.split(),
         'Shapes' : 'square triangle rectangle circle ellipse rhombus trapezoid chevron pentagon hexagon septagon octagon'.split(),
         'Fruits' : 'apple orange lemon lime pear watermelon grape grapefruit cherry banana cantaloupe mango strawberry tomato'.split(),
         'Animals' : 'bat bear beaver cat cougar crab deer dog donkey duck eagle fish frog goat leech lion lizard monkey moose mouse otter owl panda python rabbit rat shark sheep skunk squid tiger turkey turtle weasel whale wolf wombat zebra'.split()}

def getRandomWord(wordDict):
    #returns a random word from the dictionary and its key
    #select random key
    wordKey = random.choice(list(wordDict.keys()))

    #select random word from the key's list
    wordIndex = random.randint(0, len(wordDict[wordKey]) -1)

    return [wordDict[wordKey][wordIndex], wordKey]

def displayBoard(missedLetters, correctLetters, secretWord):
    print(HANGMAN_PICS[len(missedLetters)])
    print()

    print('Missed letters:', end=' ')
    for letter in missedLetters:
        print(letter, end=' ')
    print()

    blanks = '_' * len(secretWord)

    for i in range(len(secretWord)): 
        if secretWord[i] in correctLetters:
            blanks = blanks[:i] + secretWord[i] + blanks[i+1:]

    for letter in blanks: 
        print(letter, end=' ')
    print()

def getGuess(alreadyGuessed):
    #returns the letter input by the player and makes sure the letter is lowercase
    while True:
        print('Guess a letter:')
        guess=input()
        guess=guess.lower()
        if len(guess)!=1:
            print("please input a single letter")
        elif guess in alreadyGuessed:
            print("this letter was already guessed, pick another")
        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
            print("please input a LETTER")
        else:
            return guess

def playAgain():
    #returns true if the player chooses to play again
    print("Would you like to play again? ('yes' or 'no')")
    return input().lower().startswith('y')


print('H A N G M A N')

difficulty = 'X'
while difficulty not in "EMH":
    print('Please choose a difficulty level:\n E - Easy\n M - Medium\n H - Hard')
    difficulty = input().upper()
    if difficulty == 'M':
        del HANGMAN_PICS[8]
        del HANGMAN_PICS[7]
    elif difficulty == 'H':
        del HANGMAN_PICS[8]
        del HANGMAN_PICS[7]
        del HANGMAN_PICS[5]
        del HANGMAN_PICS[3]

missedLetters = ''
correctLetters = ''
secretWord, secretSet = getRandomWord(words)
gameIsDone = False

while True:
    print('The secret word is in the set: ' + secretSet)
    displayBoard(missedLetters, correctLetters, secretWord)

    #have player guess a word
    guess = getGuess(missedLetters + correctLetters)

    if guess in secretWord:
        correctLetters = correctLetters + guess

        #check if player has won
        foundAllLetters = True
        for i in range(len(secretWord)):
            if secretWord[i] not in correctLetters:
                foundAllLetters = False
                break
        if foundAllLetters:
            print ('Amazing! the secret word is, in fact "' + secretWord + '"!')
            gameIsDone = True
    else:
        missedLetters = missedLetters + guess

        #check if player has lost
        if len(missedLetters) == len(HANGMAN_PICS) -1:
            displayBoard(missedLetters, correctLetters, secretWord)
            print('Blast! You have run out of guesses!\nAfter ' + str(len(missedLetters)) + 'missed guesses and ' + str(len(correctLetters)) + 'correct guesses, the word was:"' + secretWord + '"')
            gameIsDone = True

        #ask player if the wish to play again
        if gameIsDone:
            if playAgain():
                missedLetters = ''
                correctLetters = ''
                gameIsDone = False
                secretWord, secretSet = getRandomWord(words)
            else:
                break
