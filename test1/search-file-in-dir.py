#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os,sys,re
def search_file(dir_name, keyword):
    for x in os.listdir(dir_name):
        x = os.path.join(dir_name, x)
        if os.path.isdir(x):
            search_file(x, keyword)
        if os.path.isfile(x):
            if keyword in os.path.splitext(os.path.split(x)[1])[0]:
                print os.path.join(dir_name, x)

if len(sys.argv) != 2:
    print "Please give the keyword, like:\"python search_file.py keyword\""
    sys.exit()
keyword = sys.argv[1]
dir_name = os.path.abspath('.')
search_file(dir_name, keyword)
'''

def fun(path):
    file=[x for x in os.listdir(path) if os.path.isfile(x)]
    k=len(sys.argv)
    for b in range(1,k):
        print "*"*7+"current dir:%s search argv %d" % (path,b)+"*"*7
        i=0
        for  a in file:
            c=re.search(sys.argv[b],file[i])
            if c:
                print os.getcwd()+'/'+file[i]
            i+=1
        print "*"*25

path=os.getcwd()
fun(path)

temp=[x for x in os.listdir(path) if os.path.isdir(x)]
b=0
for a in temp:
    path=os.getcwd()+'/'+temp[b]
    #print path
    fun(path)
    b+=1
'''
