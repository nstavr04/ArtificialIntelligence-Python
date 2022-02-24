# Version 2, Uses a common idiom for default values

import sys
freq = {} # Frequency of words in text

for word in input().split(" "):
    freq[word] = 1 + freq.get(word,0)

print(freq)