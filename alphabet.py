
"""Cleverbot chats with himself."""
from __future__ import print_function
import traceback
import random
import math
import sys

import cleverbot

#given the first sentence in the commandline will create conversation following the alphabet formula
#need to flush out the prefix dictionary
dictionary = {1: ["Accidently", "Absolutely", "As it turns out", "Actually"],2: ["But", "Because"], 3:["Consequently", "Can't believe it"],
              4: ["Definitely", "Damn it"], 5:["Excellent"], 6: ["Fuck you", "Fortunately"], 7: ["Good job"], 8:["Hell"], 9:["Interesting", "Ironically"], 10:["Jesus"], 11:["Kidding me"], 
              12:["literally","laughablly"], 13:["My word"], 14:["Nice"], 15:["Oh"], 16:["Perhaps"], 17:["Quite"], 18:["Random"], 19:["Subtle","Suprise"], 20:["That's awesome"],21:["Unfortunately"], 
              22:["Very good"], 23:["Well", "Wait"], 24:["Xena's tits"], 25:["Yes"], 26:["Zounds"]}



def main():
    # instantiate two Cleverbot objects
    cleverbot_client_one = cleverbot.Cleverbot()
    cleverbot_client_two = cleverbot.Cleverbot()

 
    #print('>> Mary: I like you')
    answer = cleverbot_client_two.ask(sys.argv[1])
    print('>> Mike: ' + sys.argv[1])
   

    for key in dictionary:
        num = random.uniform(0,1)
        index = math.floor(num*len(dictionary[key]))
        prefix = dictionary[key][int(index)]

        if (key%2 == 0):
            print('>> Mike: {} , {}'.format(prefix, answer))
            answer = cleverbot_client_one.ask(prefix + answer)
        else:
            print('>> Mary: {} , {}'.format(prefix,answer))
            answer = cleverbot_client_two.ask(prefix + answer)


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('>> Exiting...')
    except Exception as err:
        print(traceback.format_exc(err))
