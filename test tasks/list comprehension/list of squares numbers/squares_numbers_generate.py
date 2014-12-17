#!/usr/bin/env python2
#-*- coding: utf-8 -*-

def genListOfSquaresNumbers(listArg):
    """
    Генерирует список квадратов элементов аргумента-списка
    """
    res = [el ** 2 for el in listArg]
    return res

if __name__ == '__main__':
    L = [x for x in range(10)]
    print genListOfSquaresNumbers(L)
