'''Problem - I 

sentence = "Hey I am walking here I am walking here o captain my captain water water everywhere nor a drop to drik"
print(verse, "\n")

# split sentence into list of words
sentence_list =  # You will have to fill out the function 
print(sentence_list, '\n')

# convert list to set to get unique words
sentence_set = 
print(sentence_set, '\n')

# print the number of unique words
num_unique = 
print(num_unique, '\n')'''

n="Hey I am walking here I am walking here o captain my captain water water everywhere nor a drop to drik"
print(n)
sentence_list=[]
sentence_list=n.split()
print(sentence_list)
sentence_set =set(sentence_list)

print(sentence_set)
unique_number=len(sentence_set)
print(unique_number)