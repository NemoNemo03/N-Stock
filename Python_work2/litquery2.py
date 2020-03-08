import re
import profile

with open('document.txt', 'r') as f:
    string = f.read()
str_list = string.lower()
words = str_list.split('.')
words_count = len(words)


with open('quety.txt', 'r') as f:
    string = f.read()
str_query = string.lower()
word_query = re.split('[^a-zA-Z]+', str_query)



def words_xoy(words):
    word_all_list = []
    for x in range(len(words)):
        word_list = re.split('[^a-zA-Z]+', words[x])
        if '' in word_list:
            word_list.remove('')
        word_all_list.append(word_list)
    return word_all_list
#print(words_xoy(words))


def query(words,word_query):
    word=word_query
    for x in range(len(word)):
        if word_query[x] in re.split('[^a-zA-Z]+', str_list):
            word_all_list = words_xoy(words)
            for i in range(len(word_all_list)):
                for j in range(len(word_all_list[i])):
                    if word[x] == word_all_list[i][j]:
                        print(str(i+1)+'/'+str(j+1), end='\n')
        else:
            print('none',end=' ')

profile.run("query(words,word_query)")
















