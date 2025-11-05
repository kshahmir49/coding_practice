nums1 = [1,2,3,4,0,0,0,0]
nums2 = [1,2,5,6]

def merge(nums1, nums2, m=len(nums2), n=len(nums2)):
    l = len(nums1) - 1
    m -= 1
    n -= 1
    while m>0 and n>0:
        if nums1[m] > nums2[n]:
            nums1[l] = nums1[m]
            m -= 1
        else:
            nums1[l] = nums2[n]
            n -= 1
        l -= 1
    while n>0:
        nums1[l] = nums2[n]
        l -= 1
        n -= 1
    return nums1

print(merge(nums1, nums2))