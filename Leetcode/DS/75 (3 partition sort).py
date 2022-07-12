def sortColors(nums):
    counting = {0:0,1:0,2:0}
    for num in nums:
        counting[num] += 1
    i = 0
    for num, count in counting.items():
        nums[i:(i+count)] = [num] * count
        i += count

nums = [2,0,2,1,1,0]
sortColors(nums)
print(nums)        


#Other Solution (3 partition sort)

def sortColors1(nums):
    red, white, blue = 0, 0, len(nums)-1
    
    while white <= blue:
        if nums[white] == 0: #encounters red
            nums[red], nums[white] = nums[white], nums[red]
            white += 1
            red += 1
        elif nums[white] == 1: #encounters white
            white += 1
        else:  #encounters blue
            nums[white], nums[blue] = nums[blue], nums[white]
            blue -= 1

nums = [1,0,1,1,1,0]
sortColors1(nums)
print(nums)



