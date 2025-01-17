#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[ ]:





# In[1]:


from nltk.corpus.reader import reviews
from nltk.tokenize import RegexpTokenizer
from nltk.stem.porter import PorterStemmer
from nltk.corpus import stopwords
import sys

# In[12]:


tokenizer = RegexpTokenizer(r'\w+')
en_stopwords = set(stopwords.words('english'))
ps = PorterStemmer()


# In[13]:


def getStemmedReview(review):
    review = review.lower()
    review = review.replace("<br /><br />"," ") # replacing break with space
    
    #Tokenize
    tokens = tokenizer.tokenize(review)
    new_tokens = [token for token in tokens if token not in en_stopwords]
    stemmed_tokens = [ps.stem(token) for token in new_tokens]
    cleaned_review = ' '.join(stemmed_tokens)
    
    return cleaned_review


# In[14]:


sample_text = """I loved this movie since I was 7 and I saw it on the opening day. It was so touching and beautiful. I strongly recommend seeing for all. It's a movie to watch with your family by far.<br /><br />My MPAA rating: PG-13 for thematic elements, prolonged scenes of disastor, nudity/sexuality and some language."""


# In[15]:


getStemmedReview(sample_text)


# In[ ]:
# Doing input file and returning a clean output file of moview reviews
def getStemmedDocument(inputFile,outputFile):

    out = open(outputFile,'w',encoding="utf8")

    with open(inputFile,encoding="utf8") as f:
        reviews=f.readlines()

    for review in reviews:
        cleaned_review = getStemmedReview(review)
        print((cleaned_review),file = out)

    out.close()


# Reading command line input
inputFile = sys.argv[1]
outputFile = sys.argv[2]
getStemmedDocument(inputFile,outputFile)

