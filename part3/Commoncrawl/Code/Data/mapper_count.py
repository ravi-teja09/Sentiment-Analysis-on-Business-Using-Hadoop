#!/usr/bin/python3.4
"""mapper.py"""

#import sys
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import re
from nltk.stem import WordNetLemmatizer
wordnet_lemmatizer = WordNetLemmatizer()

with open(0, 'rb') as f:
    line = f.read()       
    
    line = line.decode('utf-8').strip()
    
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
                 'also', 'united', 'states', 'color', 'vallejo', 'cyndi', 'services', 'last','could', 'were',
                 'been', 'than', 'into', 'after', 'other', 'years', 'hippo', 'many', 
                 'even','businesses', 'cenicola','office', 'whether', 'than', 'read']
    
    word_tokens = word_tokenize(line)    
    
    word_tokens = [w.lower() for w in word_tokens]

    filtered_sentence = [w for w in word_tokens if not w in stop_words] 
    filtered_sentence = [w for w in filtered_sentence if not w in bad_words]
    
    for word in filtered_sentence:
        print('%s\t%s' % (word, "1"))