#!/usr/bin/env python3

"""wcount.py: count words from an Internet file.

__author__ = "WangYiwen"
__pkuid__  = "1700011805"
__email__  = "wangyiwen@pku.edu.cn"
"""

import sys
from urllib.request import urlopen


def wcount(lines, topn=10):
    dic={}
    for i in """!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~""":
        lines2=lines.replace(i," ")
        lines=lines2
    word_list=lines2.split()
    for word in word_list:
        dic[word]=dic.get(word,0)+1
    alist=list(dic.items())
    all_times=[]
    for (word,times) in alist:
        all_times.append(times)
    all_times=list(set(all_times))
    all_times.sort(reverse=True)
    for i in range(topn):
        for word in dic.keys():
            if dic.get(word)==all_times[i]:
                print(word, "\t",dic.get(word))
        

        

if __name__ == '__main__':

    if  len(sys.argv) == 1:
        print('Usage: {} url [topn]'.format(sys.argv[0]))
        print('  url: URL of the txt file to analyze ')
        print('  topn: how many (words count) to output. If not given, will output top 10 words')
        sys.exit(1)

    try:
        topn = 10
        if len(sys.argv) == 3:
            topn = int(sys.argv[2])
    except ValueError:
        print('{} is not a valid topn int number'.format(sys.argv[2]))
        sys.exit(1)

    try:
        with urlopen(sys.argv[1]) as f:
            contents = f.read()
            lines   = contents.decode()
            wcount(lines, topn)
    except Exception as err:
        print(err)
        sys.exit(1)
