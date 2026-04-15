print()

# check 3 lists. If numbers of same index are equals then return that numbers as a list

def extract_index_ele(l1, l2, l3):
    commonNumbers = []

    for x, y, z in zip(l1, l2, l3):
        if (x == y == z):
            commonNumbers.append(x)
        
    return commonNumbers

nums1 = [1, 4, 3, 4, 5, 6, 2]
nums2 = [0, 4, 2, 3, 4, 5, 2]
nums3 = [0, 4, 2, 3, 4, 5, 2]

print("Original lists:")
print(nums1)
print(nums2)
print(nums3)
print()

print("Common index elements of the said lists:")
print(extract_index_ele(nums1, nums2, nums3))
print()

print("---------")
print()

print(zip(nums1, nums2, nums3))
print(list(zip(nums1, nums2, nums3)))

print()
"""
Example output:

Original lists:
[1, 4, 3, 4, 5, 6, 2]
[0, 4, 2, 3, 4, 5, 2]
[0, 4, 2, 3, 4, 5, 2]

Common index elements of the said lists:
[4, 2]

---------

<zip object at 0x7b455160b300>
[(1, 0, 0), (4, 4, 4), (3, 2, 2), (4, 3, 3), (5, 4, 4), (6, 5, 5), (2, 2, 2)]
"""
