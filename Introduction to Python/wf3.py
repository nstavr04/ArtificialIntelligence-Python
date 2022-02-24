# Version 3, Sorts the output alphabetically

import sys

freq = {} # Frequency of words in text

for word in input().split(" "):
    freq[word] = 1 + freq.get(word, 0)

for w in sorted(freq.keys()):
    print (w, freq[w])