import random

print "Coing guessing game." 

f = open("highScore.txt","r+")

highScore = f.read()

score = 0

print "All time high score:", highScore, "correct"

while True:

	guess = raw_input("Predict heads or tails>")

	answer = random.choice(["heads", "tails"])

	print "it is", answer 

	if guess == answer:
		score += 1
		print "your score is", score

	else:

		print "game over"
		print "Your Score:", score
		f.seek(0)
		if score > int(highScore):
			f.truncate()
			score = str(score)
			f.write(score)
			highScore = score
		break
print"you high score is", highScore