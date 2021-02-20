nums = [6,2,5,8,3,1,7,4]

def insertSort(num_list):
    for i in range(1, len(nums)):
        x = nums[i]
        for j in range(i-1, -1, -1):
            # print(j)
            if x < nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
                i -= 1
    return nums
print(insertSort(nums))


