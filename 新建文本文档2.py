# Hello, how are you?   Fine.   使得该句子按照单词反转并保留所有的空格
def reverse(str_list, start, end):
    while start < end:
        str_list[start], str_list[end] = str_list[end], str_list[start]
        start +=1
        end -=1                         #预置反转函数 a,b = b,a

setence = ' Hello, how are you?   Fine.   '
str_list = list(setence)
i=0
while i < len(str_list):
    if str_list[i] != ' ':
        start = i
        end = start + 1                 #通过空格识别单词
        while (end < len(str_list)) and str_list[end] != ' ':
            end += 1
        reverse(str_list, start, end - 1)
        i = end                         #先反转单词
    else:   
        i +=1
str_list.reverse()                      #反转整个句子
print(str_list)
print(''.join(str_list))
        
