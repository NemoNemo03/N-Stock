# -*- coding: UTF-8 -*-
#_author_ = 'lixiaohua'

#打开要查询的文献,将文献中的单词转换为小写，将文献中其他符号处理为空格
import re
import profile


with open('literature.txt', 'r') as f:
    string = f.read()
str_list = string.lower()

with open('quety.txt', 'r') as f:
    string = f.read()
str_query = string.lower()
word_query = re.split('[^a-zA-Z]+', str_query)

#将文献处理为每个句子集合成的列表，再将句子字符串分割为单词列表
i = 0
words_sum = 0
while i < len(str_list):
    if str_list[i] == '.':
        words_sum += 1
        i += 1
    else:
        i += 1
print('句子数：', words_sum)
words = str_list.split('.', words_sum)

#使用循环语句遍历遍历每个句子与单词，定位查询单词的坐标（x,y）
def a(word_query):
    x = 0
    wordquery_sum = 0                       #将不存在单词的初始值设置为0，如果不存在该单词则该值不会变动
    while x < words_sum:
        word = re.split('[^a-zA-Z]+', words[x])
        y = 0
        while y < len(word):
            if word[y] == word_query:
                y += 1
                wordquery_sum = y
                print( y, '/', x + 1)
            else:
                y += 1
        x += 1
    if wordquery_sum == 0:
        print('None')
def b(word_query):
    i = 0
    while i < len(word_query):
        a(word_query[i])
        i += 1
profile.run("b(word_query)")
