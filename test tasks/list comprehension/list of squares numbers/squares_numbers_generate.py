#!/usr/bin/env python2
#-*- coding: utf-8 -*-

def gen_list_of_squares_numbers(listArg):
    """
    Генерирует список квадратов элементов аргумента-списка
    """
    return [el ** 2 for el in listArg]

if __name__ == '__main__':
    L = [x for x in range(10)]
    print gen_list_of_squares_numbers(L)
