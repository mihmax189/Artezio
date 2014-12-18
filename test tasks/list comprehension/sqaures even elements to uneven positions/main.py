#!/usr/bin/env python2
#-*- coding: utf-8 -*-

def gen_list(list_args):
    """
    Возвращает квадраты четных элементов на нечетных позициях.
    """
    return [el ** 2 for i, el in enumerate(list_args) if i % 2 != 0]

if __name__ == '__main__':
    L = [1, 2, 2, 4, 10, 9]
    print gen_list(L)
