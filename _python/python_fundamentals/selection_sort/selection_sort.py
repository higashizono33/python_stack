nums = [8,5,4,1,2,6,0,7,9,3]
def sort(num_list):
    for i in range(0,len(nums)):
        min = nums[i]
        for j in range(i+1,len(nums)):
            if nums[j] < nums[i]:
                min = nums[j]
                nums[j] = nums[i]
                nums[i] = min
    return nums
print(sort(nums))