#!/usr/bin/python3.4
"""mapper.py"""

import sys
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import re

def coocc(tokens):
    try:
        return zip(tokens,tokens[1:]+[tokens[0]])
    except:
        return zip(tokens,tokens)

with open(0, 'rb') as f:
    line = f.read()       
    
    line = line.decode('utf-8').strip()
    # remove leading and trailing whitespace
#    line = line.strip()

    line = re.sub('[^a-zA-Z\n]',' ', line)
    line = re.sub(r'\b\w{1,3}\b','',line)
    line = re.sub("<.*>|<|!|\.|@|#|\$|\*|:|%|\+|…|\\\\|\/|«|»|···|\||\•|\?|\(|\)|=|-|&|;|\_|—|~|¯|\{|\}|\[|\]|£|€|¥|¿|–", "", line)
    line = re.sub("\“|\”|\‘|\’|\"|,|'", " ", line)
    line = re.sub("[0-9]+|http[a-zA-Z0-9]+", " ", line)
    line = line.lower()
    line = re.sub(" [a-z] |aa+[a-z]* | ab | aba | abc | ac | acc | acq | az | ba | baa* | ca | czq | czt | da | daca  | ec | ed | rt | co ", " ", line)
    line = re.sub(" amp | get | pi | marc | someon | talking | speaking | ever | done | less ", " ", line)
    
    stop_words = (stopwords.words('english'))
    bad_words = ['if','who', 'would', 'the', 'are', 'said', 'i', 'in', 'it', 'a', 'u', 'm', 're', 
                 'them', 'they', 'there', 'should', 'over', 'an', 'via', 'up', 'at', 'is', 'as',
                 'was', 'him', 'he', 'can', 'did', 'go', 'by', 'us', 'our', 'their', 'or', 'how', 
                 'now', 'but', 'give', 'my', 'so', 'be', 'out', 'its', 'and', 'any', 'all', 'got', 'then', 'you',
                 'these', 'say', 'on', 'not', 'some', 'me', 'those', 'to', 'of', 'for', 'we', 
                 'why', 'like','https','with','from','para','more','this','when','just','about',
                 'that','what','have','will','your', 'must', 'which', 'pathfinder', 'vbtn', 'msfppreload', 'msfpnav',
                 'also', 'united', 'states', 'color','vallejo', 'cyndi', 'service', 'last', 'same', 'mind', 'fl',
                 'msfphover', 'hippo', 'quinny', 'dreami', 'many', 'even', 'cenicola', 'than',
                 'whether', 'office', 'read']
    
    word_tokens = word_tokenize(line)
    word_tokens = [w.lower() for w in word_tokens]

    filtered_sentence = [w for w in word_tokens if not w in stop_words] 
    filtered_sentence = [w for w in word_tokens if not w in bad_words]

#    for word in filtered_sentence:
#        print('%s\t%s' % (word, "1"))
    
    for word in coocc(filtered_sentence):
        print('%s %s\t%s' % (word[0],word[1], "1"))