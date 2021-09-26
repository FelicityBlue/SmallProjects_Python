import random

head = 0
tail = 0

#return either head or tail after getting a random number between
#1 or 0 depends on the random number generator

def flipIt():
    i = random.randint(0, 1)
    if i == 0:
        return 'head'
    else:
        return 'tail'


for i in range(100):

    h = flipIt()
    if h == 'head':
        head += 1
    if h == 'tail':
        tail += 1

print(f"head : {head} tails {tail}")
