'''Write code to create a list of word lengths for the words in original_str using the accumulation pattern 
and assign the answer to a variable num_words_list. (You should use the len function).'''

original_str = "The quick brown rhino jumped over the extremely lazy fox"

split_string = original_str.split()

count = 0
for word in split_string:
    split_string[count] = len(word)
    count += 1
    
num_words_list = split_string
print(num_words_list)