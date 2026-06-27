
from itertools import product


wordlist = set()

with open ("words.txt", "r") as words:
    for line in words:
        wordlist.add(line.strip().lower())


req_letter = input("Required Letter\n").strip()

letters = list(input("all letters\n").strip())

for length in range(4,11):
    
    for perm in product(letters, repeat = length):
        if ''.join(perm) in wordlist and req_letter in perm:
            print(perm)




