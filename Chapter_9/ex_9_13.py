'''Write code to create a list of word lengths for the words in original_str using the accumulation pattern 
and assign the answer to a variable num_words_list. (You should use the len function).'''

original_str = "The quick brown rhino jumped over the extremely lazy fox"

num_words_list = []

split_str = original_str.split()

for word in split_str:
    lword = len(word)
    num_words_list.append(lword)

print(num_words_list)