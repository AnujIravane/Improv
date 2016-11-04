from vaderSentiment import sentiment as vaderSentiment

listofstrings = ("I slapped myself on the ass.", "I love myself!", "your mama is a hottie")

def saddest(listofstrings):
	sentiment = 1
	sadsent = "test"
	for sentence in listofstrings:
		vs = vaderSentiment(sentence)["compound"]
		if vs < sentiment:
			sadsent = sentence
			sentiment = vs
	return sadsent
print saddest(listofstrings)

print "______________________"
def happiest(listofstrings):
	sentiment = -1
	happysent = "test"
	for sentence in listofstrings:
		vs = vaderSentiment(sentence)["compound"]
		if vs > sentiment:
			happysent = sentence
			sentiment = vs

	return happysent

print happiest(listofstrings)
