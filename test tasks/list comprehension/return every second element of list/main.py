#!/usr/bin/env python2
#-*- coding: utf-8 -*-

def return_every_second_element(list_args):
    """
    Возвращает каждый второй элемент аргумента-списка
    """
    return [el for i, el in enumerate(list_args, 1) if i % 2 == 0]

if __name__ == '__main__':
    print return_every_second_element([el for el in range(-10,1)])
