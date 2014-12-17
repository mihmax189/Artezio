#!/usr/bin/env python2
#-*- coding: utf-8 -*-
import sys

if __name__ == '__main__':
    files = sys.argv[1:]		# первый элемент списка argv - имя модуля программы
    for fileName in files:
        # чтение строк файла при помощи итератора
        for line in open(fileName, 'r'):
            print line,			# подавить перевод на следующую строку
