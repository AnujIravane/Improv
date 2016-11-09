from TextParser import findSentences
import nltk
import unicodedata
import random
import string



def good_bad_ugly():
	problem = raw_input("What is a problem you're having? Enter in the form 'I have a _________ problem.'\n")
	keyword = problem.split()[3]
	
	vowel_start = False
	if keyword[0].lower() in ["a", "e", "i", "o", "u"]:
		vowel_start = True
	
	get_coach_advice(keyword, vowel_start)
	
	

def get_coach_advice(keyword, vowel_start):
	# football coach urls
	url2 = 'http://www.saturdaydownsouth.com/2012/bear-bryant-50-quotes/'
	url1 = 'http://www.goodreads.com/quotes/tag/coaching'
	url3 = 'http://www.goodreads.com/quotes/tag/coaching?page=2'
	
	urls = []
	urls.extend([url1, url2, url3])
	
	# parse for body text sentences
	text_list = []
	for url in urls:
		text = findSentences(url, '')
		list = text.split('\n-----\n')
		text_list.extend(list)
	
	# remove/format sentences
	sentences = []
	for phrase in text_list:
		if '?' in phrase:
			text_list.remove(phrase)
		elif hasNumbers(phrase):
			text_list.remove(phrase)
		elif '\n' in phrase:
			text_list.remove(phrase)
		else:
			phrase.replace('\n', ' ')
			phrase = unicodedata.normalize('NFKD', phrase).encode('ascii', 'ignore')
			phrase.split('.', 1)[0] + '.'
			phrase = phrase.lstrip()
			sentences.append(phrase)
	
	# arrays for holding different types of sentences
	problem_phrases = []
	i_phrases = []
	you_phrases = []
	object_phrases = []
	command_phrases = []
	other_phrases = []
	
	# parse each sentence to determine its type
	for phrase in sentences:
		if keyword in phrase:
			problem_phrases.append(phrase)
		else:
			text = nltk.word_tokenize(phrase)
			tags = nltk.pos_tag(text)
			#print tags
			if "I" in tags[0] or "I" in tags[1]:
				i_phrases.append(phrase)
			else:
				for index, word in enumerate(tags):
					if "you" in word or "You" in word and index < len(tags)-2:
						if "VB" in tags[index+1][1] and ("NN" in tags[index+2][1] or "DT" in tags[index+2][1]):
							if "NN" in tags[index+2][1]:
								text[index+2] = "the "+keyword
								new_phrase = "".join([" "+w if not w.startswith("'") and w not in string.punctuation else w for w in text]).strip()
								object_phrases.append(new_phrase)
							elif "DT" in tags[index+2][1] and "NN" in tags[index+3][1]:
								if "an" in tags[index+2][0] and vowel_start is False:
									text[index+2] = "a"
								elif "a" in tags[index+2][0] and vowel_start is True:
									text[index+2] = "an"
								text[index+3] = keyword
								new_phrase = "".join([" "+w if not w.startswith("'") and w not in string.punctuation else w for w in text]).strip()
								object_phrases.append(new_phrase)
							else:
								you_phrases.append(phrase)
						else:
							you_phrases.append(phrase)
					else:
						other_phrases.append(phrase)
					index += 1
			
	#print i_phrases
	#print '\n\n'
	#print you_phrases
	#print '\n\n'
	#print object_phrases
	
	print '\n'
	print 'Football Coach: \n'
	rand1 = random.randint(0, len(i_phrases)-1)
	print i_phrases[rand1]
	rand2 = random.randint(0, len(you_phrases)-1)
	print you_phrases[rand2]
	rand3 = random.randint(0, len(object_phrases)-1)
	print object_phrases[rand3]
	
	

	
			
def hasNumbers(inputString):
	return any(char.isdigit() for char in inputString)

if __name__ == "__main__":
	good_bad_ugly()