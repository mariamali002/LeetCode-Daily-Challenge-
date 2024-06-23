class Solution(object):
    def subarraysDivByK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        prefix_sum = 0
        remainder_count = {0: 1}  # Initialize with 0 remainder count as 1 to handle the case when prefix_sum % k == 0
        count = 0

        for num in nums:
            prefix_sum += num
            remainder = prefix_sum % k

            # Adjust remainder to be positive if it is negative
            if remainder < 0:
                remainder += k

            if remainder in remainder_count:
                count += remainder_count[remainder]
                remainder_count[remainder] += 1
            else:
                remainder_count[remainder] = 1

        return count