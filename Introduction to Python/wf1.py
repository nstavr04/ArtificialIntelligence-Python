# Count the frequency of each word in text read from the standard input, print results .
# Version 1, Simple start

import sys

freq = {} # frequency of words in text

for word in input().split(" "):
    if word in freq:
        freq[word] = 1 + freq[word]
    else:
        freq[word] = 1

print(freq)
