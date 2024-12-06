#https://www.codewars.com/kata/590e03aef55cab099a0002e8

a = [1, 2, 3]

def incrementer(nums):
    for i in range(len(nums)):
        nums[i]+= i+1
        if nums[i] >= 10:
            nums[i] = nums[i]%10

    return nums

print(incrementer(a))