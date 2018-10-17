__author__ = 'mac'
#coding='gbk'impo#coding='gbk'
import csv
import pandas as pd
import jieba

f1 =open("new1.txt",encoding='gbk',errors='ignore')
f2 =open("fenci_result.txt",'a')
lines =f1.readlines()  # 读取全部内容
for line in lines:
    line.replace('\t', '').replace('\n', '').replace(' ','')
    seg_list = jieba.cut(line, cut_all=False)
    f2.write(" ".join(seg_list))

f1.close()
f2.close()