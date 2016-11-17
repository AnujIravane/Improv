import json
from watson_developer_cloud import AlchemyLanguageV1
from stat_parser import Parser
import nltk.data
from collections import deque

alchemy_language = AlchemyLanguageV1(api_key='bb8f3178b6678d4c860b4b68b04e09f95ec3c02b')
tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
parser = Parser()

def findSentences(url,subject):
    cleanText,success = getTextFromUrl(url)
    if success:
        output = []
        sentences = tokenizer.tokenize(cleanText)
        #print  '\n\n'.join(sentences)
        for sentence in sentences:
            if all(word in sentence.split() for word in subject):
                #if wordIsSubject(word,sentence):
                #findSubjectAndObject(sentence)
                output.append(sentence)
        return '\n-----\n'.join(output)

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


