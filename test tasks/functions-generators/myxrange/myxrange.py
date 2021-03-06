#!/usr/bin/env python2
#-*- coding: utf-8 -*-

def myxrange(*args):
    """
    Возвращает итератор, который не создает сразу весь список целых
    чисел в заданном диапазоне, в генерирует их по требованию.
    """

    # анализ количества и значений аргументов
    if len(args) == 1:
        # если передан один аргумент, то он задает верхний предел генерируемой
        # последовательности: в данном случае параметры start и step получают
        # значения по умолчанию
        start, stop, step = 0, args[0], 1
        if stop < 0:
            return
    elif len(args) == 2:
        # если передано два аргумента, то они задают нижний и верхний пределы
        # генерируемой последовательности: в данном случае параметр step получает
        # значение по умолчанию
        start, stop, step = args[0], args[1], 1
        if stop < start:
            # если stop < start, то вернуть пусто список, поскольку в данном
            # случае нельзя построить последовательность
            return
    elif len(args) == 3:
        # если передано три аргумента, то они задают нижний и верхний пределы
        # генерируемой последовательности и шаг, с которым происходит выборка
        # значений
        start, stop, step = args[0], args[1], args[2]
        if stop < start and step > 0:
            # при данных условиях нельзя построить последовательность
            return
        if stop > start and step < 0:
            # при данных условиях нельзя построить последовательность
            return

    else:
        print 'TypeError: myxrange() requires 1-3 int arguments'
        return

    while (start < stop if start < stop else stop < start):
        yield start
        start += step

if __name__ == '__main__':
    print list(myxrange(-3))
