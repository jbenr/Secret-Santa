import random

lst = []
reicherts = ['harry', 'ben', 'chuck', 'jacko']
barnes = ['maya', 'sof', 'joe']
breebs = ['nina', 'henry']
sparky = ['sparky']

lst.extend(reicherts)
lst.extend(barnes)
lst.extend(breebs)
#lst.extend(sparky)

print(reicherts)
print(barnes)
print(breebs)
print(sparky)

# lst = []
# print('Insert names into your list of secret santa participants. Press return to finish.')
# inp = ' '
# while inp != '':
#     inp = input("Name: ")
#     if inp != '': lst.append(inp)

def rando(x):
    temp = x.copy()
    print('Giver', '\t----->\t', 'Receiver')
    print('------','\t------\t','------')
    for gifter in x:
        opener = random.choice(temp)
        while gifter == opener or (gifter in reicherts and opener in reicherts) or (gifter in barnes and opener in barnes) or (gifter in breebs and opener in breebs):
            opener = random.choice(temp)
        print(gifter, '\t----->\t', opener)
        temp.remove(opener)
        
print(rando(lst))