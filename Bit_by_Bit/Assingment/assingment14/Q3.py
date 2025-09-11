# 3. Write a Python program to find all the unique words and count the
# frequency of occurrence from a given list of strings. Use Python set
# data type.
def wap(s):
    freque = {}
    li1 = s.split(' ')
    word_set = set()
    unique_set = set()
    freque = {}
    for word in li1:
        word_set.add(word)
        if word not in unique_set:
            unique_set.add(word)

        if word in freque:
            freque[word]+=1
        else:
            freque[word]= 1
    return word_set,unique_set,freque


s = "Data science is fun Python makes data science easier"
all_words,unique_words,frequency = wap(s)
print(f'All words: {all_words}')
print(f'Unique words: {unique_words}')
print(f'Frequency of words: {frequency}')