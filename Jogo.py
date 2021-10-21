import random

def embaralhar(peças):
    mesa=peças[:]
    peças.remove(peças[-1])
    print(peças)
    return mesa

print(embaralhar(([[1,2],[3,2],[1,2],[4,2]])))
