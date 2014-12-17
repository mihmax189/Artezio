#!/usr/bin/env python2
#-*- coding: utf-8 -*-

def returnEverySecondElement(listArgs):
    """
    Возвращает каждый второй элемент аргумента-списка
    """
    res = [listArgs[indx] for indx in range(0, len(listArgs), 2)]
    return res

if __name__ == '__main__':
    print returnEverySecondElement([el for el in range(-10,1)])
