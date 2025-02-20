#{see RQ1}
def file2lst(fname):
    ''' Return a list where each element is a word from fname. '''
    L = []
    f = open(fname)
    for line in f:
        line = line.strip()
        lst = line.split()
        for x in lst:
            L.append(x)
    f.close()
    return L

#{see RQ2}
def lst2dict(lst):
    ''' Return a dictionary given list lst.  Each key is an element in the lst.
    The value is always 1.'''
    d = {}
    for w in lst:
        d[w] = 1 
    return d

def word_frequency(fname, english_dictionary):
    #{see RQ3}
    ''' Return a dictionary where each key is a word both in the file fname and in 
    the dictionary english_dictionary, and the corresponding value is the frequency
    of that word.'''
    d = {}
    L = file2lst(fname) #{see RQ}
    for x in L:
        x = x.lower()
        if x in english_dictionary:
            if not x in d:
                d[x] = 1
            else:
                d[x] += 1
    return d

def sort_by_value(d):
    ''' Return a sorted list of tuples, each tuple containing a key and a value.
        Note that the tuples are order in descending order of the value.'''
    import operator #{see RQ4}
    lst = sorted(d.items(), key=operator.itemgetter(1), reverse=True)    
    return lst

if __name__ == '__main__':    
    ed = lst2dict(file2lst('words.txt')) # from http://greenteapress.com/thinkpython2/code/words.txt
    d = word_frequency('brexit-news.txt', ed)
    print(sort_by_value(d))




