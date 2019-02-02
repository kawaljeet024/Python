def twosum(nums, target):
    if len(nums) <= 1:
        return False
    aux_dict = {}
    for i in range(len(nums)):
        if nums[i] in aux_dict:
            return[aux_dict[nums[i]], i]
        else:
            aux_dict[target - nums[i]] = i


nums = [1, 3, 2, 7]
target = 9
print(twosum(nums, target))

#9-1 = 8 --> {8:0}
#9-3 = 6 --> {8:0, 6:1}
#9-2 = 7 --> {8:0, 6:1, 7:2}
# now you know next is 7 in nums and i already exist in dict and there was 2 at index 2 so if you add 2 and 7 you get 9
# so we have nums[i] i.e index of value 2 from where we got 7 (9-2) and i index from nums of 7
# so we return nums[i],i i.e [2,3]
