nums = [1, 3, 4, 5, 7, 11]

target = 9

l, r = 0, len(nums) - 1


def twoSum(numbers, target):
    ## Sorted Array DS

    l, r = 0, len(numbers) - 1

    while l < r:
        currentSum = numbers[l] + numbers[r]

        if currentSum > target:
            r -= 1
        elif currentSum < target:
            l += 1
        else:
            return numbers[l] + 1,  numbers[r] + 1

    return []


test = twoSum(nums, target)
print(test)