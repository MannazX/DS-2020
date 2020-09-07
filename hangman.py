def checkCorrect(guess):
	global ErrorCount
	if guess in set(word):
		updateShown(guess)
	else:
		ErrorCount += 1
		wrongGuess.append(guess)
	print('No. of mistakes: ', ErrorCount)
	print('Wrong guesses: ', sorted(wrongGuess))


def updateShown(guess):
	for idx, letter in enumerate(word):
		if letter == guess.lower():
			shown[idx] = letter
	printResult(shown)

def printResult(someList):
	result = ''
	for i in someList:
		result += i
	print(result)

wrongGuess = []
ErrorCount = 0
word = list('Andreas'.lower())
shown = list('*' * len(word))

while word != shown and ErrorCount <= 7:
	yourGuess = input('Guess a letter: ')
	checkCorrect(yourGuess)

if word == shown:
	print('Good job, you won!')
else:
	print('Sorry, you lost!')