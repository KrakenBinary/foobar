'''
Time to put on my big boy pants and start predicting the future!
minions dont become an evil genius over night!
'''
from fractions import gcd
from fractions import Fraction
import numpy as np


def solution(m):
    '''
    need to take the matrix and do some not so simple matrix math
    The goal is to pull a triangular matrix and an orthogonal matrix
    do some multiplication in order to divide (turn left to go right)
    then leverage fractions to quicly pull common denominators
    '''
    if m == [[0]]:
        foobar = [1, 1]
        return foobar
    matrix = np.asarray(m)  # convert matrix to array
    rows, cols = matrix.shape[0], matrix.shape[1]  # shape of the array

    zero_tracker = 0
    rq_matrix = []
    combine = []

    init_matrix = np.zeros((1, cols))  # set shape. del this row later
    for i in range(rows):
        if sum(matrix[i]) == 0:  # row is 0 sum
            init_matrix = np.vstack((init_matrix, matrix[i]))  # concat vert
            zero_tracker = zero_tracker + 1  # how many 0 rows? (track)
            combine.append(i)  # add i to combine (track it)
    for i in range(rows):
        if sum(matrix[i]) != 0:
            init_matrix = np.vstack((init_matrix, matrix[i]))
            rq_matrix.append(i)
            combine.append(i)
    init_matrix = np.delete(init_matrix, 0, 0)  # delete first row from init
    init_matrix = init_matrix[:, combine]  # rearrange columns
    rq_matrix = np.delete(init_matrix, range(zero_tracker), 0)  # del 0's

    R = rq_matrix[:, range(zero_tracker)]  # upper triangular matrix
    Q = np.delete(rq_matrix, range(zero_tracker), 1)  # orthoganal matrix
    for i in range(Q.shape[0]):
        for j in range(Q.shape[1]):  # gram schmit process
            Q[i, j] = Q[i, j]/sum(rq_matrix[i])
    F = np.linalg.inv(np.eye(len(Q)) - Q)
    # need to use an inverse matrix to do some division

    for i in range(R.shape[0]):
        for j in range(R.shape[1]):  # gram schmit process
            R[i, j] = R[i, j]/sum(rq_matrix[i])
    FR = np.dot(F, R)  # matrix multiplication
    # the fun bit is now we can use Fraction to fin the reduced fractions.

    numerator = []
    denominator = []

    for i in range(FR.shape[0]):
        for j in range(FR.shape[1]):
            numerator.append(
                Fraction(FR[i, j]).limit_denominator().numerator)
            denominator.append(
                Fraction(FR[i, j]).limit_denominator().denominator)

    numerator = numerator[:zero_tracker]  # trash removal
    denominator = denominator[:zero_tracker]  # trash removal

    denominator2 = list(denominator)

    for i in range(len(denominator2)-1):
        if denominator2[i] == 1:
            denominator2.remove(denominator2[i])

    my_lcm = 1

    for i in denominator2:
        my_lcm = my_lcm*i//gcd(my_lcm, i)

    mult_list = []
    for i in range(len(denominator)):
        div = my_lcm/denominator[i]
        if div == my_lcm:
            mult_list.append(0)
        elif div == 1:
            mult_list.append(1)
        else:
            mult_list.append(int(div))

    result = []
    for i in range(len(numerator)):
        result.append(numerator[i]*mult_list[i])
    result.append(my_lcm)
    return result
