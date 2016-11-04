from vaderSentiment import sentiment as vaderSentiment

sentence = "I slapped myself on the ass."
listofstrings = ("I love myself!", "your mama is a hottie")

print sentence,
vs = vaderSentiment(sentence)
print "\n\t" + str(vs)
print vs["compound"]

for sentence in listofstrings:
	print sentence
	print vaderSentiment(sentence)
	print "sentiment: " + str(vaderSentiment(sentence)["compound"])
