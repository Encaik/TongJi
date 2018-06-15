#!/usr/bin/python
# -*- coding: utf-8 -*-

from xlwt import *
import jieba

f = open('lyric.txt', encoding='utf-8')
raw = f.read()
data = jieba.cut(raw)
word_list = []
word_dict = {}
for each in data:
    if len(each) > 1:
        word_list.append(each)

for index in word_list:
    if index in word_dict:
        word_dict[index] += 1
    else:
        word_dict[index] = 1

sorted(word_dict.items(), key=lambda e: e[1], reverse=False)

fc = open("fenci.txt", 'w')
for item in word_dict.items():
    print(item)
    fc.write(item[0]+'\t'+str(item[1])+'\n')

#将分词和词频输出到excel中
    file = Workbook(encoding='utf-8')
    table = file.add_sheet('data')
    ldata = []
    num = [a for a in word_dict]
    num.sort()

    for item in num:
            ldata.append(str(word_dict[item]))

    for i in range(1000):
            table.write(i, 0, num[i])
            table.write(i, 1, ldata[i])
    file.save("fenci.xls")

