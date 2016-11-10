import pprint
import sys
import random

from search import googleSearcher

initial = sys.argv[1]

#def scriptGenerator(initial):

c = 0
query = initial
googleResults = []
result = ""

while c < 10:
	googleResults = googleSearcher(query)
	sentenceSelection = googleResults[0]
	senSelDecomp = sentenceSelection.split(' ')
	randInt = random.randint(0, len(senSelDecomp)-1)
	query = senSelDecomp[randInt]
	result += " " + sentenceSelection
	pprint.pprint(query)
	pprint.pprint(sentenceSelection)
	c += 1

pprint.pprint(result)
