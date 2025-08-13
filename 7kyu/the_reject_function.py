#https://www.codewars.com/kata/52988f3f7edba9839c00037d/train/python

def reject(seq, predicate):
    ret_list = []
    for i in range(len(seq)):
        if predicate(seq[i]) == False:
            ret_list.append(seq[i])
    return ret_list

print(reject([1, 2, 3, 4, 5, 6], lambda x: x%2==0))
print(reject(['a', 'b', 3, 'd'], lambda x: type(x)==int))
print(reject(['a', 'b', 3, 'd'], lambda x: type(x)==str))