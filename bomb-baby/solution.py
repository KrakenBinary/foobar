#!/usr/bin/python
# -*- coding:utf-8 -*-
'''
Lets rock and roll!
'''


def old_solution(mach, facula):
    '''What are we up to now?'''
    mach, facula = int(mach), int(facula)
    if mach - facula == 0:
        print('# R1 #')
        return 0
    return bad_looper(mach, facula)


def bad_looper(mach, facula):
    '''
    bad idea but it gets me started
    cant run the big ones through this :( sad panda
    '''
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


def solution(mach, facula):
    '''
    lets figure out how to run the big numbers now
    while loop worked
        learned that we have to use:
            m-f = m (step.n-1)
            f-m = f (step.n-1)
    use integer division and remainders to determin
    how many times to subtract before we flip to the other
    method. This gives us a nice shortcut.
    '''
    try:
        hcam, alucaf = int(mach), int(facula)
    except Exception:
        return 'impossible'
    if hcam == alucaf or hcam <= 0 or alucaf <= 0:
        return 'impossible'
    true_count = 0
    while hcam != alucaf:
        if hcam > alucaf:
            division = (hcam-alucaf)//alucaf
            true_remainder = ((hcam-alucaf) % alucaf > 0)
            subtractions_count = division + true_remainder
            true_count += subtractions_count
            hcam = hcam - subtractions_count * alucaf
        elif alucaf > hcam:
            division = (alucaf-hcam)//hcam
            true_remainder = (alucaf-hcam) % hcam > 0
            subtractions_count = division + true_remainder
            true_count += subtractions_count
            alucaf = alucaf - subtractions_count * hcam

    return str(true_count) if (hcam, alucaf) == (1, 1) else 'impossible'
