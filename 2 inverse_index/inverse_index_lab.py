from random import randint
from dictutil import *

## Task 1
def movie_review(name):
    """
    Input: the name of a movie
    Output: a string (one of the review options), selected at random using randint
    """
    review_options = ["See it!", "A gem!", "Ideological claptrap!"]
    return review_options[randint(0,len(review_options)-1)]

## Tasks 2 and 3 are in dictutil.py
#dct = {1:1,2:2,3:3,4:4}
#keylist = [1,2,3,4]
#print (dict2list(dct, keylist))
#L = ['one','two','three','four']
#print (list2dict(L, keylist))    
#print (listrange2dict(L))

## Task 4    
def makeInverseIndex(strlist):
    """
    Input: a list of documents as strings
    Output: a dictionary that maps each word in any document to the set consisting of the
            document ids (ie, the index in the strlist) for all documents containing the word.

    Note that to test your function, you are welcome to use the files stories_small.txt
      or stories_big.txt included in the download.
    """
    inv_index = {}
    for index,doc in enumerate(strlist):
        words = doc.split()
        for word in words:
            if word in inv_index:
                inv_index[word].add(index)
            else:
                inv_index[word] = {index}
    
    return inv_index

## Task 5
def orSearch(inverseIndex, query):
    """
    Input: an inverse index, as created by makeInverseIndex, and a list of words to query
    Output: the set of document ids that contain _any_ of the specified words
    """
    doc_set = set()
    for word in query:
        if word in inverseIndex:
            doc_set = doc_set.union(inverseIndex[word])
    return doc_set

## Task 6
def andSearch(inverseIndex, query):
    """
    Input: an inverse index, as created by makeInverseIndex, and a list of words to query
    Output: the set of all document ids that contain _all_ of the specified words
    """
    list_of_sets = []
    for word in query:
        if word in inverseIndex:
            list_of_sets.append(inverseIndex[word])
    
    doc_set = list_of_sets[0]        
    for s in list_of_sets[1:]:
        doc_set = doc_set.intersection(s)
    return doc_set

# Test for task 4, 5 and 6
#with open('stories_small.txt','r') as f:
    #inv_index = makeInverseIndex(list(f))
    #print (inv_index)
    #l = ['The', 'Official', '1994', 'NCAA', 'Championship', 'Video', 'recaptures', 'the', 'excitement', 'of', 'the', 'latest', 'edition', 'of', 'March', 'Madness', 'and', 'Arkansas', 'march', 'to', 'the', 'title', 'with', 'rousing', 'victories', 'over', 'Michigan', ',', 'Arizona', 'and', 'Duke', 'in', 'the', 'three', 'final', 'games.', '$', '19.98', ',', '45', 'minutes', ',', '1-800-747-7999', '.']
    #doc_set = orSearch(inv_index,l)
    #print (doc_set)
    #l = ['in', 'the','Arkansas']
    #doc_set = andSearch(inv_index, l)
    #print (doc_set)