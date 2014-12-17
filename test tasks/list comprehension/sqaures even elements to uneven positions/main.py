#!/usr/bin/env python2
#-*- coding: utf-8 -*-

def genList(listArgs):
    """
    Возвращает квадраты четных элементов на нечетных позициях.
    """
    res = [listArgs[indx] ** 2 for indx in range(1, len(listArgs), 2) if listArgs[indx] % 2 == 0]
    return res

if __name__ == '__main__':
    L = [1, 2, 2, 4, 10, 9]
    print genList(L)
