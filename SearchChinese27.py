__author__ = 'yluo'
#coding=utf-8

import os, sys
import re

# Usage
# 修改Main函数里root的位置为需要项目的位置
# 修改searchExts里的内容可以匹配不同的文件类型，默认为iOS应用类型


searchExts = ['.m','.xib']

def checkChineseWord(path):

    if os.path.splitext(path)[1] in searchExts:
        fp=open(path, "r");
        lineNumber = 0
        hasFind = False
        for eachline in fp:
            lineNumber = lineNumber + 1
            pchinese = re.compile(ur'.*\"[\u4e00-\u9fa5]+.*') #判断是否为中文的正则表达式
            match = pchinese.search(eachline.decode('utf8'))
            if match :
                print ("lineNumber:"+ str(lineNumber)+" matchString:"+match.group())
                hasFind = True
        if hasFind:
            print ("fileName:"+path)
            print("------------------------------------------------------------------------------")


def traversalFiles(rootDir):
    for lists in os.listdir(rootDir):
        path = os.path.join(rootDir, lists)
        checkChineseWord(path)
        if os.path.isdir(path):
            traversalFiles(path)



if __name__ == '__main__':

    root="you project path"
    traversalFiles(root)

