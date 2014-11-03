import checker
import sys

def getNextGuess():
	print "Enter your next guess:"
	return raw_input()

def checkUniqueDigits(n):
	unique = True
	uniqueDict = {}
	for x in str(n):
		if x in uniqueDict:
			# print x + " is in dict"
			unique = False
			break
		else:
			# print x + " is not in dict"
			uniqueDict[x] = 1
	# raw_input()
	return unique

def digit(n, sum, nod):
	# print "starting loop: "+ str(n)+", "+ str(sum) + ", " + str(nod)
	if n <= nod:
			for i in range(1, 10):
				# print "i: " + str(i)
				if n < nod:
					digit((n + 1), (10 * (sum+i)), nod)
				elif n == nod:
					# print "check unique: "+str(sum+i)
					if checkUniqueDigits(sum+i):
						guessList.append(sum+i)
	# print "ending loop: "+ str(n)+", "+ str(sum) + ", " + str(nod)
	# raw_input()

done = False
answer = sys.argv[1]
maxGuesses = int(sys.argv[2])
noOfDigits = int(sys.argv[3])
noOfGuesses = 0
guessList = []

digit(1, 0, noOfDigits)
if maxGuesses < 0:
	maxGuesses = 9999999
while not done and noOfGuesses < maxGuesses:
	guess = guessList.pop() #getNextGuess()
	noOfGuesses += 1
	result = checker.check(answer, guess)
	print "Guess #"+str(noOfGuesses) + ": `" + str(guess) + "`; " + str(result)
	if result['bulls'] == noOfDigits:
		print "Well done!"
		done = True

if not done:
	print "You have reached the maximum allowed guesses! The answer is: "+ str(answer)
