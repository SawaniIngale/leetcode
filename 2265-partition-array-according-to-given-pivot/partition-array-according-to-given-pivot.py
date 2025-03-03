class Solution(object):
    def pivotArray(self, nums, pivot):
        """
        :type nums: List[int]
        :type pivot: int
        :rtype: List[int]
        """
        # count_s, count_e, count_g = 0,0,0

        # for num in nums:
        #     if num < pivot:
        #         count_s += 1
        #     elif num == pivot:
        #         count_e += 1
        #     else:
        #         count_g += 1
        
        # result = [0] * len(nums)

        # i, j = 0, count_s  
        # k = count_s + count_e  

        # for num in nums:
        #     if num < pivot:
        #         result[i] = num
        #         i += 1
        #     elif num == pivot:
        #         result[j] = num
        #         j += 1
        #     else:
        #         result[k] = num
        #         k += 1

        # return result

        less = []
        greater = []

        for num in nums:
            if num < pivot:
                less.append(num)
            elif num > pivot:
                greater.append(num)
            
        count_p = len(nums) - len(less) - len(greater)
        
        return less + [pivot]*count_p + greater