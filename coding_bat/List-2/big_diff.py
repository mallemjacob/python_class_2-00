nums = [10, 3, 5, 6, 20, 1, 30, 40, 50, 6, 9, -5]


smallest_num = nums[0]  # 10
largest_num = nums[0]  # 10


for num in nums:
    if num >= largest_num:
        largest_num = num
    elif num <= smallest_num:
        smallest_num = num

print("The smallest number: " + str(smallest_num))
print("The largest number: " + str(largest_num))
