import json
from watson_developer_cloud import AlchemyLanguageV1
import nltk.data

alchemy_language = AlchemyLanguageV1(api_key='bb8f3178b6678d4c860b4b68b04e09f95ec3c02b')
tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')

def findSentences(url,subject):
    cleanText,success = getTextFromUrl(url)
    if success:
        return '\n-----\n'.join(tokenizer.tokenize(cleanText))


def getTextFromUrl(url):
    jsonResult = json.loads(json.dumps(alchemy_language.text(url=url),indent=2))
    print jsonResult
    if jsonResult['status'] == 'OK':
        if jsonResult['text'] != "":
            return jsonResult['text'],True
    return "", False


