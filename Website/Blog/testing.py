nums = [1,2,2,4,5,7,9,2,3,2]


def removeElement(nums, val):
    counter = 0
    result = 0
    for i in range(0, len(nums)):
        if nums[i] == val:
            print(';z')
            counter += 1
        else:
            print('x')
            nums[i - counter] = nums[i]
            result += 1
    return result

print (removeElement([2], 3))