def removeDups(numlist):
    numlist = set(numlist)
    numlist = list(numlist)
    return numlist

nums = [ 2,3,4,5,4,5,6,7,3,8,9,2,1,6] # a list

print(nums)
print()
nums2 = removeDups(nums)
print(nums2)
