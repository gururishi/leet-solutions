class Solution:
    def smallestUniqueSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        MOD = 10**9 + 7
        BASE = 100003
        def check(k):
            power = pow(BASE, k, MOD)
            h = 0
            freq = {}
            for i in range(k):
                h = (h * BASE + nums[i]) % MOD
            freq[h] = 1
            for i in range(k, n):
                h = (h * BASE - nums[i-k] * power + nums[i]) % MOD
                freq[h] = freq.get(h, 0) + 1
            return any(v == 1 for v in freq.values())
        left, right = 1, n
        ans = n
        while left <= right:
            mid = (left + right) // 2
            if check(mid):
                ans = mid
                right = mid - 1
            else:
                left = mid + 1
        return ans