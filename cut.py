#!/usr/bin/env python3
#coding: utf-8

'''
根据关键词将文本分割，并保存为单独的文件.
usage:运行脚本，依次输入待分割文件->分割关键词->输出文件名
Author@LiYihang
<liyihang@shu.edu.cn>
'''

import re                                                              # 正则表达式
import linecache                                                       # 缓存读取文件指定行

def fileParse():
    inputFile = input('Input SourcFile:')                              # 输入源文件，如 A.txt
    fp = open(inputFile, 'r')

    # 输入分割关键词和输出文件名
    number = []                                                        # 定义一个空列表容器，用来保存匹配到关键字的行号
    lineNumber = 1                                                     # 行号从 1 开始
    keyWord = input('Slice KeyWord:')                                  # 输入你要切分的关键字
    outFileName = input('OutFileName:')                                # 输出文件名，如out.txt则写out即可，后续输出的文件是out0.txt,out1.txt...

    # 查找文件中匹配到关键字的所有行，并将行号保存在列表number中
    for eachLine in fp:
        m = re.search(keyWord, eachLine)                               # search()会扫描整个字符串查询关键字，并返回第一个成功的匹配
        if m is not None:                                              # 如果字符串中匹配到关键字，search()方法将返回 None
            number.append(lineNumber)                                  # 将关键字的行号记录在number中
        lineNumber = lineNumber + 1
    size = int(len(number))                                            # 匹配到关键字的数目

    # 将相邻两个匹配关键字所在行之间的文本提取出来保存为一个cif文件
    for i in range(0, size - 1):
        start = number[i]
        end = number[i + 1]
        destLines = linecache.getlines(inputFile)[start - 1 :end - 1]  # 将行号为 start 到 end 的文件内容截取出来
        fp_w = open(outFileName + str(i + 1) + '.cif', 'w')            # 将截取出的内容保存为 .cif 文件
        for key in destLines:
            fp_w.write(key)

        fp_w.close()

if __name__ == "__main__":
    fileParse()
