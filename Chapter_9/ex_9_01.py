'''For each word in the list verbs, add an -ing ending. Overwrite the old list so that verbs has the same 
words with ing at the end of each one.'''

verbs = ["kayak", "cry", "walk", "eat", "drink", "fly"]

pos = 0

for verb in verbs:
    iverb = verb + 'ing'
    verbs[pos] = iverb
    pos += 1

print(verbs)