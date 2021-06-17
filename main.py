import random
HANGMAN_PICS = ['''
    +---+
        |
        |
        |
       ===''', '''
    +---+
    o   |
        |
        |
       ===''', '''
    +---+
    o   |
	|   |
        |
       ===''', '''
    +---+
    o   |
   /|   |
        |
       ===''', ''' 
    +---+
    o   |
   /|\  |
        |
       ===''', ''' 
    +---+
    o   |
   /|\  |
   /    |
       ===''', '''
    +---+
    o   |
   /|\  |
   / \  |
       ===''']
words = []
# read txt file
f = open('words.txt')
for word in f.read().split():
	words.append(word)

def getSecretWord(wordList):
	secretIndex = random.randint(0, len(wordList) - 1)
	return wordList[secretIndex]

def displayBoard(missedLetters, correctLetters, secretWord):
	print(HANGMAN_PICS[len(missedLetters)])
	print()

	print('Missed Letters: ', end=' ')
	for letter in missedLetters:
		print(letter,end=' ')
	print()

	blanks = '_' * len(secretWord)

	for i in range(len(secretWord)):
		if secretWord[i] in correctLetters:
			blanks = blanks[:i] + secretWord[i] + blanks[i+1:]
	
	for letter in blanks: 
		print(letter, end=' ')
	print()
def guessLetter(alreadyGuessed):
	while True:
		print('Guess a letter.')
		guess = input()
		guess = guess.lower()
		if len(guess) != 1:
			print('Please enter a single letter.')
		elif guess in alreadyGuessed:
			print('You have already guess that letter. Try again.')
		elif guess not in 'abcdefghijklmnopqrstuvwxyz':
			print('Please print a letter.')
		else:
			return guess

def playAgain():
	print('Would you like to play again? (yes or no)')
	return input().lower().startswith('y')

# ------------------Main method-------------------------

print('H A N G M A N')
missedLetters = ''
correctLetters = ''
secretWord = getSecretWord(words)
gameOver = False

while True:
	displayBoard(missedLetters, correctLetters, secretWord)
	guess = guessLetter(missedLetters + correctLetters)
	print('secret word: ' + secretWord)

	if guess in secretWord:
		correctLetters = correctLetters + guess

		#Check if the user won
		foundAllLetters = True
		for i in range (len(secretWord)):
			if secretWord[i] not in correctLetters:
				foundAllLetters = False
				break
		if foundAllLetters:
				print('You have won. The secret word is "' + secretWord + '".')
				gameOver = True
	else:
		missedLetters = missedLetters + guess
		if len(missedLetters) == len(HANGMAN_PICS) - 1:
			displayBoard(missedLetters, correctLetters, secretWord)
			print('You have run out of guesses. Sorry, you lose. The secret word was y"' + secretWord + '".')
			gameOver = True

	if gameOver:
		if playAgain():
			missedLetters = ''
			correctLetters = ''
			gameOver = False
			secretWord = getSecretWord(words)
		else:
			break