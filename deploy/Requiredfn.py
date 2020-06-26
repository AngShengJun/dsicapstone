import re
from nltk.stem.porter import PorterStemmer
import pickle

# Instantiate porterstemmer
p_stemmer = PorterStemmer()

#load s_words from disk
s_words2 = pickle.load(open('finalized_stopwords.sav', 'rb'))

def selftext_to_words2(motive_text):
    
    letters_only = re.sub("[^a-zA-Z]", " ", motive_text)

    words = letters_only.split()
    
    meaningful_words = [p_stemmer.stem(w) for w in words]    

    stops = set(s_words2)

    meaningful_words = [w for w in words if w not in stops]
    
    return([" ".join(meaningful_words)])