#!/usr/bin/env python2
#-*- coding: utf-8 -*-

def perpetual_generator(value):
    """
    Функция-генератор: все время возвращает одно и тоже значение
    """
    while True:
        yield value

if __name__ == '__main__':
    G = perpetual_generator(10)
    for i in range(10):
        print next(G)
