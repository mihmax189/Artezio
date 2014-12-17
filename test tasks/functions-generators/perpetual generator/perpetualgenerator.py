#!/usr/bin/env python2
#-*- coding: utf-8 -*-

def perpetual_generator(value):
    """
    Функция-генератор: все время возвращает одно и тоже значение
    """
    yield value

if __name__ == '__main__':
    try:
        while True:
            print next(perpetual_generator(10))
    except KeyboardInterrupt:
        pass
