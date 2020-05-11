def quickSort(nums,left,right):
    if left==right:
        return
    leftO = left
    rightO=right

    tmp = nums[left]
    while left < right:
        while left<right and nums[right]>tmp:
            right -= 1
        nums[left] = nums[right]
        while left<right and nums[left] < tmp:
            left+=1
        nums[right] = nums[left]
    nums[left] = tmp
    quickSort(nums,leftO,left)
    quickSort(nums,left+1,rightO)
    return nums
