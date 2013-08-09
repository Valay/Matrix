voting_data = list(open("voting_record_dump109.txt"))

## Task 1

def create_voting_dict():
    """
    Input: None (use voting_data above)
    Output: A dictionary that maps the last name of a senator
            to a list of numbers representing the senator's voting
            record.
    Example: 
        >>> create_voting_dict()['Clinton']
        [-1, 1, 1, 1, 0, 0, -1, 1, 1, 1, 1, 1, 1, 1, -1, 1, 1, 1, 1, 1, 1, 1, 1, 1, -1, 1, -1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, -1, 1, 1, 1, 1, -1, 1, 1, 1]

    This procedure should return a dictionary that maps the last name
    of a senator to a list of numbers representing that senator's
    voting record, using the list of strings from the dump file (strlist). You
    will need to use the built-in procedure int() to convert a string
    representation of an integer (e.g. '1') to the actual integer
    (e.g. 1).

    You can use the split() procedure to split each line of the
    strlist into a list; the first element of the list will be the senator's
    name, the second will be his/her party affiliation (R or D), the
    third will be his/her home state, and the remaining elements of
    the list will be that senator's voting record on a collection of bills.
    A "1" represents a 'yea' vote, a "-1" a 'nay', and a "0" an abstention.

    The lists for each senator should preserve the order listed in voting data. 
    """
    voting_dict = {}
    for ii in voting_data:
        data = ii.split()
        voting_dict[data[0]] = list()
        for ab in data[3:]:
            voting_dict[data[0]].append(int(ab))
     
    #print (voting_dict) 
    return voting_dict
  
voting_dict = create_voting_dict()        

## Task 2
def policy_compare(sen_a, sen_b, voting_dict):
    """
    Input: last names of sen_a and sen_b, and a voting dictionary mapping senator
           names to lists representing their voting records.
    Output: the dot-product (as a number) representing the degree of similarity
            between two senators' voting policies
    Example:
        >>> voting_dict = {'Fox-Epstein':[-1,-1,-1,1],'Ravella':[1,1,1,1]}
        >>> policy_compare('Fox-Epstein','Ravella', voting_dict)
        -2
    """
    return sum([voting_dict[sen_a][i]*voting_dict[sen_b][i] for i in range(len(voting_dict[sen_a]))])

## Task 3
def most_similar(sen, voting_dict):
    """
    Input: the last name of a senator, and a dictionary mapping senator names
           to lists representing their voting records.
    Output: the last name of the senator whose political mindset is most
            like the input senator (excluding, of course, the input senator
            him/herself). Resolve ties arbitrarily.
    Example:
        >>> vd = {'Klein': [1,1,1], 'Fox-Epstein': [1,-1,0], 'Ravella': [-1,0,0]}
        >>> most_similar('Klein', vd)
        'Fox-Epstein'

    Note that you can (and are encouraged to) re-use you policy_compare procedure.
    """
    best_match = float("-inf")
    for ii in voting_dict.keys():
        if ii in sen:
            continue
        else:
            score = policy_compare(sen,ii,voting_dict)
            if score > best_match:
                best_match = score
                match = ii
                
    return match if not None else ""
    
## Task 4
def least_similar(sen, voting_dict):
    """
    Input: the last name of a senator, and a dictionary mapping senator names
           to lists representing their voting records.
    Output: the last name of the senator whose political mindset is least like the input
            senator.
    Example:
        >>> vd = {'Klein': [1,1,1], 'Fox-Epstein': [1,-1,0], 'Ravella': [-1,0,0]}
        >>> least_similar('Klein', vd)
        'Ravella'
    """
    best_match = float("inf")
    for ii in voting_dict.keys():
        if ii in sen:
            continue
        else:
            score = policy_compare(sen,ii,voting_dict)
            if score < best_match:
                best_match = score
                match = ii
                
    return match if not None else ""


## Task 5

most_like_chafee    = 'Jeffords'
least_like_santorum = 'Feingold'

# Task 6

def find_average_similarity(sen, sen_set, voting_dict):
    """
    Input: the name of a senator, a set of senator names, and a voting dictionary.
    Output: the average dot-product between sen and those in sen_set.
    Example:
        >>> vd = {'Klein': [1,1,1], 'Fox-Epstein': [1,-1,0], 'Ravella': [-1,0,0]}
        >>> find_average_similarity('Klein', {'Fox-Epstein','Ravella'}, vd)
        -0.5
    """
    score_list = list()
    for ii in sen_set:
        if sen in ii:
            continue
        score_list.append(policy_compare(sen,ii,voting_dict))
    
    return sum(score_list)/float(len(score_list))

def most_average_demo(voting_dict):
    score = float("-inf")
    for ii in voting_dict.keys():
        avg_sim =  find_average_similarity(ii, set(voting_dict.keys()), voting_dict)
        if score < avg_sim:
            score = avg_sim
            name = ii
    
    return name 
    
most_average_Democrat = most_average_demo(voting_dict) # give the last name (or code that computes the last name)

# Task 7

def find_average_record(sen_set, voting_dict):
    """
    Input: a set of last names, a voting dictionary
    Output: a vector containing the average components of the voting records
            of the senators in the input set
    Example: 
        >>> voting_dict = {'Klein': [-1,0,1], 'Fox-Epstein': [-1,-1,-1], 'Ravella': [0,0,1]}
        >>> find_average_record({'Fox-Epstein','Ravella'}, voting_dict)
        [-0.5, -0.5, 0.0]
    """
    
    dummy = voting_dict[sen_set.pop()]
    for ii in sen_set:
        dummy = [x+y for x,y in zip(dummy,voting_dict[ii])]
           
    avg_rec = [ dummy[i]/float(len(sen_set)+1) for i in range(len(dummy))]
    return avg_rec
    

average_Democrat_record = find_average_record(set(voting_dict.keys()),voting_dict) # (give the vector)
#print (average_Democrat_record)
#voting_dict['average_democrat'] = average_Democrat_record

#most_similar_to_avg_democrat_record = most_similar('average_democrat', voting_dict)
#print (most_similar_to_avg_democrat_record)

# Task 8

def bitter_rivals(voting_dict):
    """
    Input: a dictionary mapping senator names to lists representing
           their voting records
    Output: a tuple containing the two senators who most strongly
            disagree with one another.
    Example: 
        >>> voting_dict = {'Klein': [-1,0,1], 'Fox-Epstein': [-1,-1,-1], 'Ravella': [0,0,1]}
        >>> bitter_rivals(voting_dict)
        ('Fox-Epstein', 'Ravella')
    """
    rivals={}
    for key_in in voting_dict.keys():
        for key_out in voting_dict.keys():
            if key_in == key_out:
                continue;
            if (key_in,key_out) in rivals or (key_in,key_out) in rivals:
                continue
            else:
                rivals[(key_in,key_out)] =  policy_compare(key_in,key_out,voting_dict)
                
    l = list(rivals.keys())                     
    return min(l, key=rivals.get)

#print (bitter_rivals(voting_dict))