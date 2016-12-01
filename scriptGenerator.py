import pprint
import sys
import random

from search import googleSearcher
from TextParser import findSubjectAndObject

def generateNewQuery(s,o):
	query = ''

	if len(o) > 0:
		oChoice = random.choice(o)
		query += oChoice
	elif len(s) > 0:
		sChoice = random.choice(s)
		query += sChoice
	else:
		query += 'Trump'
	return query

initial = [sys.argv[1],sys.argv[2]]
print initial

#def scriptGenerator(initial):

c = 0
query = initial
googleResults = []
result = ""

while c < 10:
	googleResults = googleSearcher(query)
	#sentenceSelection = random.choice(googleResults)#[0]
	#print googleResults
	sentenceSelection = googleResults[3]

	#print sentenceSelection
	#senSelDecomp = sentenceSelection.split(' ')
	#randInt = random.randint(0, len(senSelDecomp)-1)
	#query = senSelDecomp[randInt]
	subjects, objects = findSubjectAndObject(sentenceSelection)
	query = generateNewQuery(subjects,objects)
	result += " " + sentenceSelection
	print(sentenceSelection)
	print(query)

	c += 1



