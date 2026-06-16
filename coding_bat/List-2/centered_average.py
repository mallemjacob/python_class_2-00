'''Return the "centered" average of an array of ints, which we'll say is the mean average of the values, except ignoring the largest and smallest values in the array. If there are multiple copies of the smallest value, ignore just one copy, and likewise for the largest value. Use int division to produce the final average. You may assume that the array is length 3 or more.'''


# def centered_average(nums):
#     largest_num = nums[0]
#     smallest_num = nums[0]

#     total = 0
#     length = 0

#     for num in nums:
#         if num >= largest_num:
#             largest_num = num
#         elif num <= smallest_num:
#             smallest_num = num

#     del nums[nums.index(largest_num)]
#     del nums[nums.index(smallest_num)]

#     for num in nums:
#         total = total + num

#     length = len(nums)

#     average = total // length

#     return average


def centered_average(nums):
    return (sum(nums) - max(nums) - min(nums)) // (len(nums) - 2)


print(centered_average([1, 2, 3, 4, 100]))
print(centered_average([1, 1, 5, 5, 10, 8, 7]))
print(centered_average([-10, -4, -2, -4, -2, 0]))
