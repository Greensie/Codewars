# https://www.codewars.com/kata/52988f3f7edba9839c00037d/train/python


def reject(seq, predicate):
    ret_list = []
    for i in range(len(seq)):
        if not predicate(seq[i]):
            ret_list.append(seq[i])
    return ret_list
