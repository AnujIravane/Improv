import json
from watson_developer_cloud import AlchemyLanguageV1
from watson_developer_cloud import WatsonException
from stat_parser import Parser
import nltk.data
from collections import deque
from nltk.stem import PorterStemmer

alchemy_language = AlchemyLanguageV1(api_key='1f40ffda31d16a110a51ac72849438211ad26eab')
tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
parser = Parser()

def findSentences(url,subject):
    ps = PorterStemmer()
    try:   
        cleanText,success = getTextFromUrl(url)
    #print cleanText
        if success:
            output = []
            sentences = tokenizer.tokenize(cleanText)
            #print sentences
            #print subject
            #print  '\n\n'.join(sentences)
            for sentence in sentences:
                #print "its getting here"
                addSentenceFlag = False
                words = sentence.split()
                if len(words) <= 25:
                    for word in words:
                        for q in subject:
                            if ps.stem(word).lower() == ps.stem(q).lower():
                                #print "WTF is taking so long"
                                addSentenceFlag = True
                                break

                        if addSentenceFlag:
                            #print "WTF"
                            output.append(sentence)
                            #print sentence
                            break
            return output
        return []
    except WatsonException:






                    #if all(word in sentence.split() for word in subject):
                #if wordIsSubject(word,sentence):
                #findSubjectAndObject(sentence)
                #output.append(sentence)
        return []

def findSubjectAndObject(sentence):
    syntaxTree = parser.parse(sentence)
    subjects, objects = bfs(syntaxTree)
    #print "Subjects:" + '\n'.join(subjects)
    #print "Objects:" + '\n'.join(objects)
    return subjects, objects


def bfs(tree):
    subjects = []
    objects = []
    q = deque()
    if tree:
        q.appendleft(tree)
    while len(q) != 0:
        currentNode = q.pop()
        if currentNode.label() == 'NP':
            findSubjectInNP(currentNode,subjects)
        elif currentNode.label() == 'VP':
            findObjectInVP(currentNode,objects)
        else:
            childrenCount = len(currentNode)
            if childrenCount > 1:
                for i in xrange(0,childrenCount):
                    q.appendleft(currentNode[i])
    return (subjects,objects)


def findSubjectInNP(tree,subjects):
    if 'NN' in tree.label():
        subjects.append(tree[0])
    for children in tree:
        if isinstance(children,nltk.tree.Tree):
            findSubjectInNP(children,subjects)

def findObjectInVP(tree,objects):
    if 'NN' in tree.label():
        objects.append(tree[0])
    for children in tree:
        if isinstance(children,nltk.tree.Tree):
            findObjectInVP(children,objects)


def getTextFromUrl(url):
    jsonResult = json.loads(json.dumps(alchemy_language.text(url=url),indent=2))
    if jsonResult['status'] == 'OK':
        if jsonResult['text'] != "":
            return jsonResult['text'],True
    return "", False


