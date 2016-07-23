#http://stackoverflow.com/questions/5278122/checking-if-all-elements-in-a-list-are-unique 

#x="abc" 
#x=list(x)

#if elements hashable 
def allUnique(x):
    seen = set()
    return not any(i in seen or seen.add(i) for i in x)
    
#if elements not hashable
def allUnique(x):
    seen = list()
    return not any(i in seen or seen.append(i) for i in x)
    

