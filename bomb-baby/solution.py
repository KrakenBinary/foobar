#!/usr/bin/python
# -*- coding:utf-8 -*-
'''
Lets rock and roll!
'''


def solution(mach, facula):
    '''What are we up to now?'''
    mach = int(mach)
    facula = int(facula)
    if mach - facula == 0:
        print('# R1 #')
        return 0
    return bad_looper(mach, facula)


def bad_looper(mach, facula):
    '''bad idea but it gets me started'''
    count = 0
    while mach != facula:
        if mach == 1 and facula == 1:
            if count > 0:
                print('# R1 #')
                return count
            print('# R2 #')
            return 0
        count = count + 1
        if mach > facula:
            mach = mach - facula
        else:
            facula = facula - mach
    print('# R3 #')
    return count
