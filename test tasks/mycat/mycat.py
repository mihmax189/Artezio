#!/usr/bin/env python2
#-*- coding: utf-8 -*-
import sys

if __name__ == '__main__':
    files = sys.argv[1:]		# первый элемент списка argv - имя модуля программы
    for file_name in files:
        # чтение строк файла при помощи итератора
        with open(file_name) as f:
            for line in f:
                print line,		# подавить перевод на следующую строку
